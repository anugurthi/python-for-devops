"""Day 1 example: greet a user with input validation."""

import sys  # We import 'sys' to interact with the system, like exiting the program.


def main() -> None:
    """
    This is the main function where our program starts.
    """
    try:
        # 'input' asks the user for text.
        # 'strip' removes spaces from the beginning and end.
        name = input("What's your name? ").strip()
    except EOFError:
        # This block runs if the input stream is cut off unexpectedly.
        print("No input received. Exiting.")
        sys.exit(1)  # Exit with an error code (1 means something went wrong).

    # Check if the name is empty (just an empty string "").
    if not name:
        print("Please enter at least one character next time.")
        sys.exit(1)

    # 'f-strings' (f"...") let you put variables directly inside text.
    print(f"Hello, {name}! You're ready for Python automation.")


# This check ensures the code only runs if you execute this file directly.
# It won't run if you import this file into another script.
if __name__ == "__main__":
    main()
