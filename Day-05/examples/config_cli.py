"""Day 5 example: combine argparse flags with environment variables."""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    environment: str
    dry_run: bool
    token: str | None


def load_config() -> AppConfig:
    parser = argparse.ArgumentParser(description="Print the current automation context")
    parser.add_argument("--environment", default=os.getenv("ENVIRONMENT", "dev"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    token = os.getenv("API_TOKEN")
    return AppConfig(environment=args.environment, dry_run=args.dry_run, token=token)


def summarize(config: AppConfig) -> str:
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
