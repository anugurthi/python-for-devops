"""Create or update GitHub repositories via the REST API.

This script is intentionally beginner-friendly: it uses the `requests` library,
reads configuration from JSON or YAML, and supports dry-run / verbose modes so
you can practice safely before automating production repositories.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import requests

try:
    import yaml
except ImportError:  # pragma: no cover - optional dependency until installed
    yaml = None  # type: ignore

GITHUB_API_BASE = "https://api.github.com"


class ConfigError(RuntimeError):
    """Raised when the configuration file is invalid."""


def load_config(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")

    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            raise ConfigError("PyYAML is required to read YAML configs. Install with `pip install pyyaml`. ")
        data = yaml.safe_load(text)
    else:
        data = json.loads(text)

    if not isinstance(data, dict):
        raise ConfigError("Configuration root must be an object/dictionary.")

    required_keys = {"name", "owner", "owner_type"}
    missing = required_keys - data.keys()
    if missing:
        raise ConfigError(f"Missing required config keys: {', '.join(sorted(missing))}")

    owner_type = str(data["owner_type"]).lower()
    if owner_type not in {"user", "org"}:
        raise ConfigError("owner_type must be either 'user' or 'org'.")

    return data


def build_headers(token: str, preview: bool = False) -> Dict[str, str]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-devops-launchpad",
    }
    if preview:
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    return headers


def repo_exists(session: requests.Session, owner: str, repo: str, headers: Dict[str, str]) -> bool:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = session.get(url, headers=headers, timeout=15)
    if response.status_code == 200:
        return True
    if response.status_code == 404:
        return False
    raise RuntimeError(f"Failed to determine repo status ({response.status_code}): {response.text}")


def create_repo(
    session: requests.Session,
    config: Dict[str, Any],
    headers: Dict[str, str],
    dry_run: bool = False,
) -> Dict[str, Any]:
    owner = config["owner"]
    owner_type = config["owner_type"].lower()
    payload = {
        "name": config["name"],
        "description": config.get("description", ""),
        "private": bool(config.get("private", True)),
        "homepage": config.get("homepage"),
        "visibility": config.get("visibility", "private"),
        "auto_init": bool(config.get("auto_init", True)),
        "has_issues": bool(config.get("has_issues", True)),
        "has_wiki": bool(config.get("has_wiki", False)),
        "has_projects": bool(config.get("has_projects", False)),
        "delete_branch_on_merge": bool(config.get("delete_branch_on_merge", True)),
    }

    if dry_run:
        return {"dry_run": True, "payload": payload}

    if owner_type == "org":
        url = f"{GITHUB_API_BASE}/orgs/{owner}/repos"
    else:
        url = f"{GITHUB_API_BASE}/user/repos"

    response = session.post(url, headers=headers, json=payload, timeout=15)
    if response.status_code not in {201, 202}:
        raise RuntimeError(f"Repo creation failed ({response.status_code}): {response.text}")
    return response.json()


def update_topics(session: requests.Session, owner: str, repo: str, topics: Iterable[str], headers: Dict[str, str], dry_run: bool) -> None:
    if not topics:
        return
    if dry_run:
        return
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/topics"
    response = session.put(url, headers={**headers, "Accept": "application/vnd.github+json"}, json={"names": list(topics)}, timeout=15)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to update topics ({response.status_code}): {response.text}")


def ensure_files(
    session: requests.Session,
    owner: str,
    repo: str,
    files: Iterable[Dict[str, Any]],
    headers: Dict[str, str],
    default_branch: str,
    dry_run: bool,
) -> None:
    for file_config in files:
        path = file_config.get("path")
        content = file_config.get("content")
        message = file_config.get("message", f"Add {path}")
        if not path or content is None:
            raise ConfigError("Each file entry requires 'path' and 'content'.")

        if dry_run:
            continue

        encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
        payload = {
            "message": message,
            "content": encoded,
            "branch": file_config.get("branch", default_branch),
        }
        response = session.put(url, headers=headers, json=payload, timeout=15)
        if response.status_code not in {201, 200}:
            raise RuntimeError(f"Failed to push {path} ({response.status_code}): {response.text}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create or update a GitHub repository from config")
    parser.add_argument("--config", required=True, type=Path, help="Path to JSON or YAML config file")
    parser.add_argument("--token", type=str, default=os.getenv("GITHUB_TOKEN"), help="GitHub personal access token (defaults to GITHUB_TOKEN env var)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without calling the API")
    parser.add_argument("--verbose", action="store_true", help="Log payloads and responses")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    token = args.token
    if not token:
        raise ConfigError("Provide a GitHub token via --token or the GITHUB_TOKEN environment variable.")

    config = load_config(args.config)
    owner = config["owner"]
    repo_name = config["name"]
    default_branch = config.get("default_branch", "main")

    headers = build_headers(token)
    session = requests.Session()

    exists = repo_exists(session, owner, repo_name, headers)
    if args.verbose:
        print(f"Repository exists: {exists}")

    if exists and not args.dry_run:
        if args.verbose:
            print("Skipping creation; repository already exists.")
    else:
        result = create_repo(session, config, headers, dry_run=args.dry_run)
        if args.verbose:
            print(json.dumps(result, indent=2, sort_keys=True, default=str))

    topics = config.get("topics", [])
    update_topics(session, owner, repo_name, topics, headers, args.dry_run)

    initial_files = config.get("initial_files", [])
    ensure_files(session, owner, repo_name, initial_files, headers, default_branch, args.dry_run)

    print(f"Repository ready: https://github.com/{owner}/{repo_name}")


if __name__ == "__main__":
    main()
