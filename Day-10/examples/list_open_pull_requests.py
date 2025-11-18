"""Fetch GitHub pull request creators for the Kubernetes repository.

Requires the `requests` library. For higher rate limits, supply a token via the
`GITHUB_TOKEN` environment variable.
"""

from __future__ import annotations

import os
from typing import Dict

import requests

API_URL = "https://api.github.com/repos/kubernetes/kubernetes/pulls"


def fetch_open_pull_requests(token: str | None = None) -> Dict[str, int]:
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(API_URL, headers=headers, timeout=15)
    response.raise_for_status()

    pull_requests = response.json()
    creators: Dict[str, int] = {}
    for pull in pull_requests:
        creator = pull["user"]["login"]
        creators[creator] = creators.get(creator, 0) + 1
    return creators


def main() -> None:
    token = os.getenv("GITHUB_TOKEN")
    creators = fetch_open_pull_requests(token)
    print("PR Creators and Counts:")
    for creator, count in creators.items():
        print(f"{creator}: {count} PR(s)")


if __name__ == "__main__":
    main()
