"""Fetch GitHub pull request creators for the Kubernetes repository.

Requires the `requests` library. For higher rate limits, supply a token via the
`GITHUB_TOKEN` environment variable.
"""

from __future__ import annotations

import os
from typing import Dict

import requests  # Library for making HTTP requests

API_URL = "https://api.github.com/repos/kubernetes/kubernetes/pulls"


def fetch_open_pull_requests(token: str | None = None) -> Dict[str, int]:
    """
    Calls the GitHub API to get all open pull requests and counts them by author.
    """
    # Headers tell the API what format we want
    headers = {"Accept": "application/vnd.github+json"}
    
    # If we have a token, add it to the headers for authentication
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Make a GET request to the API
    response = requests.get(API_URL, headers=headers, timeout=15)
    response.raise_for_status()  # Raise an error if the request failed

    # Convert the JSON response into a Python list
    pull_requests = response.json()
    
    # Count how many PRs each person created
    creators: Dict[str, int] = {}
    for pull in pull_requests:
        creator = pull["user"]["login"]  # Get the username
        creators[creator] = creators.get(creator, 0) + 1  # Increment the count
    return creators


def main() -> None:
    # Check if the user set a GITHUB_TOKEN environment variable
    token = os.getenv("GITHUB_TOKEN")
    creators = fetch_open_pull_requests(token)
    
    print("PR Creators and Counts:")
    for creator, count in creators.items():
        print(f"{creator}: {count} PR(s)")


if __name__ == "__main__":
    main()
