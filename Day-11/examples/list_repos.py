"""List repositories for the authenticated user or organization.

Run with:
  export GITHUB_TOKEN=...  # with repo scope
  python list_repos.py --owner my-org --owner-type org
"""

from __future__ import annotations

import argparse
import os

import requests

GITHUB_API_BASE = "https://api.github.com"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", help="GitHub login or organization name")
    parser.add_argument("--owner-type", choices=("user", "org"), default="user")
    parser.add_argument("--token", default=os.getenv("GITHUB_TOKEN"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.token:
        raise SystemExit("Set GITHUB_TOKEN environment variable or pass --token")

    session = requests.Session()
    headers = {
        "Authorization": f"Bearer {args.token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-devops-launchpad",
    }

    if args.owner_type == "org":
        url = f"{GITHUB_API_BASE}/orgs/{args.owner}/repos"
    else:
        url = f"{GITHUB_API_BASE}/user/repos"

    params = {"per_page": 100}
    while url:
        response = session.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        for repo in response.json():
            visibility = repo.get("visibility", repo.get("private"))
            print(f"{repo['full_name']}  |  visibility={visibility}")
        url = response.links.get('next', {}).get('url')
        params = None


if __name__ == "__main__":
    main()
