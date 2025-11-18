# Day 2 · Data Types & Strings in Action

This day sets the foundation for manipulating configuration files, logs, and API payloads. You’ll explore core Python data types, string formatting, and the basics of regular expressions using the resources in this folder.

## Learning Goals

- Differentiate between `str`, `int`, `float`, `bool`, and collections.
- Slice, format, and transform strings to sanitize inputs or craft API requests.
- Use regular expressions to extract signals from log lines.

## Agenda

1. Read `01-data-types.md` and work through the examples.
2. Experiment with `Day-02/examples/` scripts (concat, length, replace, regex operations).
3. Extend `examples/strings.py` with helper functions for masking secrets or normalizing usernames.
4. Capture takeaways in a personal `notes.md`.

## Practice Prompts

- Write a function that redacts values that look like API tokens.
- Parse a simulated log entry and pull out timestamp, severity, and message text.
- Convert a CSV line into a Python dictionary using split operations.

## Deliverable

Commit an updated `examples/strings.py` (or a new `examples/string_utils.py`) implementing at least three utility functions you can reuse later in the course.

## Stretch Goals

- Explore Python’s `pathlib` to sanitize filenames before saving logs.
- Use `re.compile` with named groups to make regex matches easier to read.
