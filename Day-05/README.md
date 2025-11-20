# Day 5 · Command-Line Tools (CLI)

Today we will learn how to make our scripts interactive so we can pass options to them (like `--dry-run` or `--verbose`).

## What You Will Learn

-   **Arguments:** How to pass information to your script when you run it.
-   **Environment Variables:** How to read secret settings (like passwords) safely.

## Instructions

1.  **Read:** Understand that `argparse` is the tool we use to read command-line arguments.
2.  **Run Example:** Run the script with different flags.
    ```bash
    cd examples
    # Run with default settings
    python3 config_cli.py

    # Run with a specific environment
    python3 config_cli.py --environment production

    # Run in "dry run" mode (simulation)
    python3 config_cli.py --dry-run
    ```
3.  **Experiment:** Try setting an API token before running the script:
    ```bash
    export API_TOKEN="secret123"
    python3 config_cli.py
    ```

## Checklist

-   [ ] I can pass a flag (like `--help`) to a python script.
-   [ ] I understand why we use Environment Variables for secrets (so we don't save passwords in the code).
