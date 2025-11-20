# Day 3 · Variables & Configuration

Today we will learn how to store data in variables and how to organize settings (configuration) for your scripts.

## What You Will Learn

-   **Variables:** How to name and store data.
-   **Scope:** Where variables can be used (inside or outside functions).
-   **Configuration:** How to use "Environment Variables" to change how your script runs without changing the code.

## Instructions

1.  **Read:** Open `variables.md` to understand how to name things properly.
2.  **Run Example:** Run the script to see how it picks up settings.
    ```bash
    cd examples
    python3 config_scopes.py
    ```
3.  **Experiment:** Try setting an environment variable before running the script:
    ```bash
    export AWS_REGION="us-west-2"
    python3 config_scopes.py
    ```

## Checklist

-   [ ] I understand how to name variables (e.g., `my_variable` instead of `x`).
-   [ ] I know how to read a value from the environment (`os.getenv`).