"""Day 7 example: gate deployments using conditional logic."""

from __future__ import annotations

import datetime as dt
import os


def is_approved() -> bool:
    """Check if the 'DEPLOY_APPROVED' environment variable is set to 'true'."""
    # os.getenv("VAR", "default") gets the value or uses "default" if missing
    # .lower() converts "True" -> "true" so we can compare easily
    return os.getenv("DEPLOY_APPROVED", "false").lower() == "true"


def within_window(start_hour: int = 8, end_hour: int = 18) -> bool:
    """Check if the current time is between start_hour and end_hour."""
    now = dt.datetime.now().hour
    # This checks if 'now' is greater than or equal to 'start_hour' AND less than 'end_hour'
    return start_hour <= now < end_hour


def main() -> None:
    # Guard Clause: Check if we are OUTSIDE the window
    if not within_window():
        print("🚫 Deployment blocked: outside maintenance window.")
        return  # Stop the function here!

    # Guard Clause: Check if we are NOT approved
    if not is_approved():
        print("🚫 Deployment blocked: missing approval flag.")
        return  # Stop the function here!

    # If we passed both checks above, we are good to go!
    print("✅ All checks passed. Proceed with deployment!")


if __name__ == "__main__":
    main()
