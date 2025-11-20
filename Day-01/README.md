# Day 1 · Kickoff & Environment Setup

Welcome to Day 1! Today we will set up your computer so you can write and run Python code.

## Learning Goals

-   Install Python.
-   Set up a code editor (VS Code).
-   Run your first Python script.

## 1. Install Python

### macOS
1.  Open your terminal.
2.  Install Homebrew (if you don't have it):
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
3.  Install Python:
    ```bash
    brew install python
    ```
4.  Check if it worked:
    ```bash
    python3 --version
    ```

### Windows
1.  Download Python from [python.org](https://www.python.org/downloads/).
2.  Run the installer. **IMPORTANT:** Check the box that says **"Add Python to PATH"**.
3.  Open PowerShell and check if it worked:
    ```powershell
    python --version
    ```

### Linux (Ubuntu/Debian)
1.  Open your terminal.
2.  Run these commands:
    ```bash
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv
    ```
3.  Check if it worked:
    ```bash
    python3 --version
    ```

## 2. Run Your First Script

1.  Open your terminal or command prompt.
2.  Navigate to this folder:
    ```bash
    cd Day-01/examples
    ```
3.  Run the "Hello World" script:
    ```bash
    python3 hello_world.py
    ```
    *(Note: On Windows, you might just type `python` instead of `python3`)*

## 3. Try the Interactive Script

We have a script that asks for your name. Try running it:

```bash
python3 hello_user.py
```

## Checklist

-   [ ] I have Python installed.
-   [ ] I can run a python script in my terminal.

See you on Day 2!
