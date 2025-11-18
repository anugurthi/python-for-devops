"""Day 7 example: gate deployments using conditional logic."""

from __future__ import annotations

import datetime as dt
import os


def is_approved() -> bool:
    return os.getenv("DEPLOY_APPROVED", "false").lower() == "true"


def within_window(start_hour: int = 8, end_hour: int = 18) -> bool:
    now = dt.datetime.now().hour
    return start_hour <= now < end_hour


def main() -> None:
    if not within_window():
        print("🚫 Deployment blocked: outside maintenance window.")
        return

    if not is_approved():
        print("🚫 Deployment blocked: missing approval flag.")
        return

    print("✅ All checks passed. Proceed with deployment!")


if __name__ == "__main__":
    main()
