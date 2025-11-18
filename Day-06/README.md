# Day 6 · Files, Logging & Operator Refresher

Before we dive into API-heavy automation, we need reliable scripts that can read/write files, emit useful logs, and make decisions with Python’s operators. Use today to combine these fundamentals.

## Learning Goals

- Practice arithmetic, comparison, logical, and bitwise operators in the context of automation.
- Read configuration files, append to log files, and rotate files safely.
- Implement structured logging (timestamps, levels) to aid troubleshooting.

## Agenda

1. Revisit the operator primers under `01-Notes/` to reinforce how each category behaves.
2. Build a `log_writer.py` that records mock deployment events to a file and drop it into `examples/` when you’re done.
3. Open `examples/file-automation/update_server.py` to see an end-to-end example of idempotent config editing, then refactor it with logging and guards.
4. Review the reference answers under `examples/assignment-answers/` after attempting the exercises yourself.
5. Add operator-based conditions (e.g., retry logic using counters) to control flow.
6. Document lessons learned in `notes.md`.

## Practice Prompts

- Parse `examples/file-automation/server.conf` and print warnings when thresholds are exceeded.
- Use membership operators to validate that required keys exist in a configuration dictionary.
- Create a rotating log function that truncates when a file exceeds a given size.

## Deliverable

Commit a script that reads a config file, performs comparisons using operators, and writes structured output to `automation.log`.

## Stretch Goals

- Integrate Python’s `logging` module with JSON output.
- Experiment with bitwise operators to toggle feature flags packed into integers.