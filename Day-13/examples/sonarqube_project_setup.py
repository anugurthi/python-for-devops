"""Provision SonarQube projects and tokens via REST API calls.

The script creates a project when missing, optionally assigns a quality profile,
and can generate an analysis token for CI usage. Dependencies: `requests` and
`PyYAML` (or JSON).
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

import requests

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore


class ConfigError(RuntimeError):
    pass


def load_config(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")

    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            raise ConfigError("Install PyYAML to read YAML configs (pip install pyyaml).")
        data = yaml.safe_load(text)
    else:
        data = json.loads(text)

    if not isinstance(data, dict):
        raise ConfigError("Configuration root must be a dictionary.")

    required = {"project_key", "project_name"}
    missing = required - data.keys()
    if missing:
        raise ConfigError(f"Missing required config keys: {', '.join(sorted(missing))}")

    data.setdefault("visibility", "private")
    data.setdefault("main_branch", "main")
    return data


def sonar_request(
    session: requests.Session,
    method: str,
    base_url: str,
    path: str,
    auth: requests.auth.AuthBase,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
) -> requests.Response:
    url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
    response = session.request(method, url, auth=auth, params=params, data=data, timeout=20)
    if response.status_code >= 400:
        raise RuntimeError(f"SonarQube API error {response.status_code}: {response.text}")
    return response


def project_exists(session: requests.Session, base_url: str, auth: requests.auth.AuthBase, project_key: str) -> bool:
    response = sonar_request(
        session,
        "GET",
        base_url,
        "/api/projects/search",
        auth,
        params={"projects": project_key},
    )
    data = response.json()
    return any(component["key"] == project_key for component in data.get("components", []))


def create_project(session: requests.Session, base_url: str, auth: requests.auth.AuthBase, config: Dict[str, Any], dry_run: bool) -> None:
    if dry_run:
        print("[dry-run] Would create SonarQube project", config["project_key"])
        return

    sonar_request(
        session,
        "POST",
        base_url,
        "/api/projects/create",
        auth,
        data={
            "project": config["project_key"],
            "name": config["project_name"],
            "visibility": config.get("visibility", "private"),
            "mainBranch": config.get("main_branch", "main"),
        },
    )
    print(f"Project created: {config['project_key']}")


def assign_quality_profile(session: requests.Session, base_url: str, auth: requests.auth.AuthBase, config: Dict[str, Any], dry_run: bool) -> None:
    qp_config = config.get("quality_profile")
    if not qp_config:
        return

    required = {"language", "profile"}
    missing = required - qp_config.keys()
    if missing:
        raise ConfigError(f"Missing quality_profile keys: {', '.join(sorted(missing))}")

    if dry_run:
        print(f"[dry-run] Would assign quality profile {qp_config['profile']} ({qp_config['language']})")
        return

    sonar_request(
        session,
        "POST",
        base_url,
        "/api/qualityprofiles/add_project",
        auth,
        data={
            "project": config["project_key"],
            "qualityProfile": qp_config["profile"],
            "language": qp_config["language"],
        },
    )
    print("Quality profile assigned")


def generate_token(session: requests.Session, base_url: str, auth: requests.auth.AuthBase, config: Dict[str, Any], dry_run: bool) -> Optional[str]:
    token_cfg = config.get("token")
    if not token_cfg:
        return None

    name = token_cfg.get("name")
    if not name:
        raise ConfigError("token config requires a 'name'")

    if dry_run:
        print(f"[dry-run] Would generate token named {name}")
        return None

    data = {"name": name}
    if token_cfg.get("login"):
        data["login"] = token_cfg["login"]

    response = sonar_request(
        session,
        "POST",
        base_url,
        "/api/user_tokens/generate",
        auth,
        data=data,
    )
    token = response.json().get("token")
    print("Generated token", name)
    return token


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Provision SonarQube project from config")
    parser.add_argument("--config", required=True, type=Path, help="Path to YAML or JSON config")
    parser.add_argument("--url", default=os.getenv("SONAR_URL"), help="SonarQube base URL (or set SONAR_URL)")
    parser.add_argument("--token", default=os.getenv("SONAR_TOKEN"), help="SonarQube admin token (or set SONAR_TOKEN)")
    parser.add_argument("--dry-run", action="store_true", help="Log actions without mutating state")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.url or not args.token:
        raise ConfigError("Provide SonarQube URL and token via arguments or environment variables.")

    config = load_config(args.config)
    session = requests.Session()
    auth = requests.auth.HTTPBasicAuth(args.token, "")

    if project_exists(session, args.url, auth, config["project_key"]):
        print(f"Project already exists: {config['project_key']}")
    else:
        create_project(session, args.url, auth, config, args.dry_run)

    assign_quality_profile(session, args.url, auth, config, args.dry_run)
    new_token = generate_token(session, args.url, auth, config, args.dry_run)
    if new_token:
        print("Store this token securely (it won't be shown again):", new_token)


if __name__ == "__main__":
    main()
