"""Day 1 example: greet a user with input validation."""

import sys


def main() -> None:
    try:
        name = input("What's your name? ").strip()
    except EOFError:
        # Mirror the behaviour of CLI tools that fail gracefully when piped input ends early.
        print("No input received. Exiting.")
        sys.exit(1)

    if not name:
        print("Please enter at least one character next time.")
        sys.exit(1)

    print(f"Hello, {name}! You're ready for Python automation.")


if __name__ == "__main__":
    main()
