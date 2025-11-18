"""Provision or update Jenkins pipeline jobs using the REST API.

This script keeps dependencies light (only `requests` and `PyYAML`) and
illustrates how to authenticate, handle crumb issuers, and post XML job
configuration from Python.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import quote

import requests

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore

JENKINS_FOLDER_XML = """<com.cloudbees.hudson.plugins.folder.Folder plugin=\"cloudbees-folder\">\n  <description>{description}</description>\n</com.cloudbees.hudson.plugins.folder.Folder>\n"""


PIPELINE_JOB_TEMPLATE = """<flow-definition plugin=\"workflow-job\">\n  <description>{description}</description>\n  <keepDependencies>false</keepDependencies>\n  <properties/>\n  <definition class=\"org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition\" plugin=\"workflow-cps\">\n    <scm class=\"hudson.plugins.git.GitSCM\" plugin=\"git\">\n      <configVersion>2</configVersion>\n      <userRemoteConfigs>\n        <hudson.plugins.git.UserRemoteConfig>\n          <url>{git_url}</url>\n          <credentialsId>{credentials_id}</credentialsId>\n        </hudson.plugins.git.UserRemoteConfig>\n      </userRemoteConfigs>\n      <branches>\n        <hudson.plugins.git.BranchSpec>\n          <name>{branch}</name>\n        </hudson.plugins.git.BranchSpec>\n      </branches>\n      <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>\n      <submoduleCfg class=\"empty-list\"/>\n      <extensions/>\n    </scm>\n    <scriptPath>{jenkinsfile}</scriptPath>\n    <lightweight>true</lightweight>\n  </definition>\n  <triggers/>\n  <disabled>false</disabled>\n</flow-definition>\n"""


class ConfigError(RuntimeError):
    pass


def load_config(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")

    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            raise ConfigError("PyYAML is required for YAML configs. Install with `pip install pyyaml`.")
        data = yaml.safe_load(text)
    else:
        raise ConfigError("Please provide a YAML config file (see sample in this directory).")

    if not isinstance(data, dict):
        raise ConfigError("Configuration root must be a mapping/dictionary.")

    required = {"job_name", "git_url"}
    missing = required - data.keys()
    if missing:
        raise ConfigError(f"Missing required config keys: {', '.join(sorted(missing))}")

    data.setdefault("description", "Provisioned via Python DevOps Launchpad")
    data.setdefault("branch", "*/main")
    data.setdefault("jenkinsfile", "Jenkinsfile")
    data.setdefault("credentials_id", "")
    return data


def build_job_path(base_url: str, folder: Optional[str], job: str) -> str:
    def append_segments(prefix: str, parts: Optional[str]) -> str:
        url = prefix.rstrip("/")
        if parts:
            for part in parts.split("/"):
                if part:
                    url += f"/job/{quote(part)}"
        return url

    url = append_segments(base_url, folder)
    if job:
        url += f"/job/{quote(job)}"
    return url


def ensure_folder(
    session: requests.Session,
    base_url: str,
    folder: str,
    headers: Dict[str, str],
    auth: requests.auth.AuthBase,
    crumb: Optional[Dict[str, str]],
) -> None:
    if not folder:
        return

    parts = [p for p in folder.split("/") if p]
    for depth in range(1, len(parts) + 1):
        current = "/".join(parts[:depth])
        folder_url = build_job_path(base_url, "/".join(parts[:depth - 1]) if depth > 1 else None, parts[depth - 1])
        api_url = f"{folder_url}/api/json"
        response = session.get(api_url, headers=headers, auth=auth, timeout=15)
        if response.status_code == 200:
            continue
        if response.status_code != 404:
            raise RuntimeError(f"Failed to inspect folder {current}: {response.status_code} {response.text}")
        parent = build_job_path(base_url, "/".join(parts[:depth - 1]) if depth > 1 else None, "")
        parent = parent.rstrip("/")
        create_url = f"{parent}/createItem?name={quote(parts[depth - 1])}"
        payload = JENKINS_FOLDER_XML.format(description=f"Auto-created folder {current}")
        folder_headers = {**headers, "Content-Type": "application/xml"}
        if crumb:
            folder_headers.update(crumb)
        resp = session.post(create_url, headers=folder_headers, auth=auth, data=payload.encode("utf-8"), timeout=15)
        if resp.status_code not in {200, 201}:
            raise RuntimeError(f"Failed to create folder {current}: {resp.status_code} {resp.text}")


def fetch_crumb(session: requests.Session, base_url: str, auth: requests.auth.AuthBase) -> Optional[Dict[str, str]]:
    crumb_url = f"{base_url.rstrip('/')}/crumbIssuer/api/json"
    response = session.get(crumb_url, auth=auth, timeout=10)
    if response.status_code == 404:
        return None
    if response.status_code == 200:
        data = response.json()
        return {data["crumbRequestField"]: data["crumb"]}
    raise RuntimeError(f"Failed to fetch Jenkins crumb: {response.status_code} {response.text}")


def job_exists(session: requests.Session, base_url: str, folder: Optional[str], job_name: str, headers: Dict[str, str], auth: requests.auth.AuthBase) -> bool:
    url = f"{build_job_path(base_url, folder, job_name)}/api/json"
    response = session.get(url, headers=headers, auth=auth, timeout=15)
    if response.status_code == 200:
        return True
    if response.status_code == 404:
        return False
    raise RuntimeError(f"Failed to inspect job {job_name}: {response.status_code} {response.text}")


def create_or_update_job(
    session: requests.Session,
    base_url: str,
    config: Dict[str, Any],
    headers: Dict[str, str],
    auth: requests.auth.AuthBase,
    crumb: Optional[Dict[str, str]],
    dry_run: bool,
) -> None:
    job_name = config["job_name"]
    folder = config.get("folder")
    ensure_folder(session, base_url, folder or "", headers, auth, crumb)

    job_xml = PIPELINE_JOB_TEMPLATE.format(
        description=config.get("description", "Managed via API"),
        git_url=config["git_url"],
        branch=config.get("branch", "*/main"),
        credentials_id=config.get("credentials_id", ""),
        jenkinsfile=config.get("jenkinsfile", "Jenkinsfile"),
    )

    if dry_run:
        print(job_xml)
        return

    item_headers = {**headers, "Content-Type": "application/xml"}
    if crumb:
        item_headers.update(crumb)

    if job_exists(session, base_url, folder, job_name, headers, auth):
        url = f"{build_job_path(base_url, folder, job_name)}/config.xml"
        response = session.post(url, headers=item_headers, auth=auth, data=job_xml.encode("utf-8"), timeout=20)
        action = "updated"
    else:
        if folder:
            parent_url = build_job_path(base_url, folder, "").rstrip("/")
            url = f"{parent_url}/createItem?name={quote(job_name)}"
        else:
            url = f"{base_url.rstrip('/')}/createItem?name={quote(job_name)}"
        response = session.post(url, headers=item_headers, auth=auth, data=job_xml.encode("utf-8"), timeout=20)
        action = "created"

    if response.status_code not in {200, 201}:
        raise RuntimeError(f"Failed to {action} job {job_name}: {response.status_code} {response.text}")

    print(f"Job {action}: {job_name}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Provision Jenkins jobs from config")
    parser.add_argument("--config", required=True, type=Path, help="Path to YAML config file")
    parser.add_argument("--url", default=os.getenv("JENKINS_URL"), help="Base Jenkins URL (defaults to JENKINS_URL env var)")
    parser.add_argument("--user", default=os.getenv("JENKINS_USER"), help="Jenkins username (defaults to JENKINS_USER env var)")
    parser.add_argument("--token", default=os.getenv("JENKINS_TOKEN"), help="Jenkins API token or password (defaults to JENKINS_TOKEN env var)")
    parser.add_argument("--dry-run", action="store_true", help="Print XML instead of calling Jenkins")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.url or not args.user or not args.token:
        raise ConfigError("Provide Jenkins URL, user, and token via arguments or environment variables.")

    config = load_config(args.config)

    session = requests.Session()
    auth = requests.auth.HTTPBasicAuth(args.user, args.token)
    headers = {"User-Agent": "python-devops-launchpad"}

    crumb = fetch_crumb(session, args.url, auth)
    if crumb:
        print("Crumb fetched successfully")

    create_or_update_job(session, args.url, config, headers, auth, crumb, args.dry_run)


if __name__ == "__main__":
    main()
