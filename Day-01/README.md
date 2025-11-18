# Day 1 · Kickoff & Environment Setup

Welcome to Day 1 of the 14-day Python DevOps Launchpad! Today is about building solid foundations: setting up your tools, running your first script, and understanding how Python will supercharge your automation work.

## Learning Goals

- Install or verify Python 3.10+
- Configure your preferred editor (VS Code recommended)
- Run the classic `hello world` script in `examples/hello_world.py`
- Compare shell scripts with Python scripts using `01-shell-vs-python.md`
- Capture questions or blockers for tomorrow’s session

## Python Installation Steps

### macOS

1. Install Homebrew if you don’t already have it:
	```bash
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	```
2. Install the latest CPython release (Homebrew keeps it under `/usr/local` or `/opt/homebrew`):
	```bash
	brew install python@3.11
	```
3. Ensure the `python3` binary is on your `PATH`:
	```bash
	echo 'export PATH="$(brew --prefix python@3.11)/bin:$PATH"' >> ~/.zshrc
	source ~/.zshrc
	```
4. Verify everything works:
	```bash
	python3 --version
	python3 -m ensurepip --upgrade
	```

### Windows 10/11

1. Download the latest installer from [python.org/downloads](https://www.python.org/downloads/windows/).
2. Run the installer, check **“Add python.exe to PATH”**, and choose **“Install for all users”**.
3. After installation, open **PowerShell** and verify:
	```powershell
	py --version
	py -m pip install --upgrade pip
	```
4. (Optional) Install the Windows Store “Python 3.11” package if you prefer automatic updates.

### Ubuntu / Debian

1. Update apt indexes:
	```bash
	sudo apt update
	```
2. Install Python plus tooling:
	```bash
	sudo apt install -y python3 python3-pip python3-venv
	```
3. Confirm versions:
	```bash
	python3 --version
	pip3 --version
	```
4. (Optional) Install build deps for compiling packages:
	```bash
	sudo apt install -y build-essential libssl-dev libffi-dev
	```

> 💡 Prefer `pyenv` or `asdf`? Install them now so you can manage multiple Python versions for future projects. The exercises work with any CPython ≥ 3.10.

## Agenda

1. **Read:** `01-shell-vs-python.md` to see where Python shines in DevOps workflows.
2. **Try:** Execute `examples/hello_world.py` with `python examples/hello_world.py`.
3. **Reflect:** Update a learning log (create your own `notes.md`!) with one automation idea you can build after this bootcamp.
4. **Stretch Goal:** Explore the Python REPL and experiment with `print()` or simple math expressions.
5. **Bonus:** Run the scripts in `examples/` (start with `examples/hello_user.py`) to practice capturing input and exiting gracefully.

## Quick Checks

- ✅ Python version shown by `python --version`
- ✅ Virtual environment created (`python -m venv .venv`)
- ✅ Example script runs without errors
- ✅ Bonus example greets you by name without crashing

## Looking Ahead

Tomorrow we’ll dive into data types and string operations. If you have extra time, skim `Day-02/01-data-types.md` so the concepts feel familiar.

Happy hacking! 🚀
