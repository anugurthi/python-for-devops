"""Day 4 example: demonstrate breaking logic into reusable functions."""

from __future__ import annotations

from pathlib import Path

def load_lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]


def summarize_services(services: list[str]) -> str:
    return " | ".join(service.upper() for service in services)


def main() -> None:
    inventory_file = Path("services.txt")
    if not inventory_file.exists():
        print("services.txt missing — create it with one service per line.")
        return

    services = load_lines(inventory_file)
    summary = summarize_services(services)
    print(f"Tracking {len(services)} services: {summary}")


if __name__ == "__main__":
    main()
