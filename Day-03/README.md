# Day 3 · Variables, Scope & Configuration Data

Today you’ll learn how Python stores data, how scope works, and how to organize configuration values so they’re easy to reuse across automation scripts.

## Learning Goals

- Distinguish between global, local, and nonlocal scope.
- Apply naming conventions that make automation scripts readable.
- Store environment-specific values in dictionaries or data classes.

## Agenda

1. Review `variables.md` and `keywords.md`.
2. Refactor yesterday’s string utilities to use constants for regex patterns.
3. Create a `examples/config_scopes.py` (or similar) showing how to load settings from `.env` files.
4. Document best practices in a personal note.

## Practice Prompts

- Write a function that returns configuration for a given environment (dev/stage/prod).
- Demonstrate the difference between mutating a global list versus copying it.
- Replace magic numbers in earlier scripts with clearly named constants.

## Deliverable

Add a short script inside `examples/` that prints which configuration file would be loaded based on an `ENVIRONMENT` environment variable.

## Stretch Goals

- Explore Python’s `dataclasses` to model configuration payloads.
- Use `typing.TypedDict` to add lightweight type hints.