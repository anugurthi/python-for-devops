# Day 5 · Command-Line Interfaces & Environment Variables

Infrastructure scripts rarely run in isolation—they accept parameters, honor environment variables, and act differently across environments. Today you’ll practice building robust command-line interfaces (CLIs) and securing configuration secrets.

## Learning Goals

- Parse arguments with `argparse` or `typer`.
- Read environment variables safely and provide sensible defaults.
- Load `.env` files for local development without leaking secrets.

## Agenda

1. Experiment with `os.environ`, `dotenv`, and `argparse` in small snippets (see `examples/config_cli.py` for a reference solution).
2. Convert yesterday’s configuration loader into a CLI that prints the active environment.
3. Create a `.env.example` template listing required variables for future automation scripts.
4. Record decisions in `notes.md`.

## Practice Prompts

- Build a CLI that accepts `--environment` and `--dry-run` flags.
- Implement validation that fails fast when required environment variables are missing.
- Echo masked values (e.g., `TOKEN=****7890`) when running in verbose mode.

## Deliverable

Commit a script inside `examples/` (e.g., `examples/config_cli.py`) that loads env vars, merges them with CLI flags, and prints a structured summary ready for use in later projects.

## Stretch Goals

- Integrate with `click` or `typer` for richer CLI experiences.
- Add unit tests that mock environment variables using `unittest.mock.patch`.
