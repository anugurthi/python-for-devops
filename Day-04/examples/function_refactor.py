"""Day 4 example: demonstrate breaking logic into reusable functions."""

from __future__ import annotations

from pathlib import Path  # Path helps us work with files easily

# This function takes a file path and returns a list of strings (lines)
def load_lines(path: Path) -> list[str]:
    """Read a file and return a list of non-empty lines."""
    # read_text() reads the whole file
    # splitlines() breaks it into lines
    # strip() removes spaces
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]


def summarize_services(services: list[str]) -> str:
    """Convert a list of services into a single uppercase string."""
    # .upper() makes text UPPERCASE
    # .join() connects them with " | " in between
    return " | ".join(service.upper() for service in services)


def main() -> None:
    inventory_file = Path("services.txt")
    
    # Check if file exists before trying to read it
    if not inventory_file.exists():
        print("services.txt missing — create it with one service per line.")
        return

    services = load_lines(inventory_file)
    summary = summarize_services(services)
    print(f"Tracking {len(services)} services: {summary}")


if __name__ == "__main__":
    main()
