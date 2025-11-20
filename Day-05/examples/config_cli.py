"""Day 5 example: combine argparse flags with environment variables."""

from __future__ import annotations

import argparse  # Library for parsing command-line arguments
import os
from dataclasses import dataclass


# @dataclass is a shortcut to create a class that just holds data
@dataclass
class AppConfig:
    environment: str
    dry_run: bool
    token: str | None


def load_config() -> AppConfig:
    # Create the parser
    parser = argparse.ArgumentParser(description="Print the current automation context")
    
    # Add arguments we want to accept
    # --environment: defaults to the 'ENVIRONMENT' env var, or 'dev' if not set
    parser.add_argument("--environment", default=os.getenv("ENVIRONMENT", "dev"))
    
    # --dry-run: a flag that sets the value to True if present
    parser.add_argument("--dry-run", action="store_true")
    
    # Parse the arguments passed to the script
    args = parser.parse_args()

    # Read the API token from environment variables (never hardcode secrets!)
    token = os.getenv("API_TOKEN")
    
    return AppConfig(environment=args.environment, dry_run=args.dry_run, token=token)


def summarize(config: AppConfig) -> str:
    # Check if token exists, but don't print the actual secret!
    token_mask = "set" if config.token else "missing"
    return (
        f"Environment: {config.environment}\n"
        f"Dry run: {'enabled' if config.dry_run else 'disabled'}\n"
        f"API token: {token_mask}"
    )


def main() -> None:
    config = load_config()
    print(summarize(config))


if __name__ == "__main__":
    main()
