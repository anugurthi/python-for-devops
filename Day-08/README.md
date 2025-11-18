# Day 8 · Collections & Data Structures

Today is a deep dive into Python collections that power most DevOps automation: lists, tuples, dictionaries, and sets. You’ll explore how to build inventory lists, reason about immutability, and model infrastructure metadata with nested dictionaries. We’ll also extend into advanced list comprehensions so you can transform data in a single, expressive line of code.

## Learning Goals

- Build and slice lists representing infrastructure inventories.
- Choose between tuples, dictionaries, and sets for configuration management.
- Apply list and dictionary comprehensions to reshape data quickly.

## Agenda

1. Review `01-Notes/` for foundational list/tuple concepts.
2. Explore `02-Assigment/` exercises to reinforce basic operations.
3. Read through `03-dictionaries-sets/` to master nested dictionaries, set operations, and uniqueness checks.
4. Run the advanced scripts under `examples/` and refactor them with comprehensions.

## Practice Prompts

- Group hosts by environment (`dev`, `stage`, `prod`) using nested lists and summarize counts per environment.
- Merge two configuration dictionaries, preferring overrides from the second one.
- Use a set to detect duplicate SNS topic subscriptions across accounts.
- Rewrite `03-list-files-in-folders.py` with a comprehension that filters out empty directories.

## Deliverable

Commit a utilities module that exposes at least three functions:

- `load_services()` returns a list of service dictionaries.
- `group_by_owner()` accepts that list and returns a dictionary keyed by owner.
- `missing_tags()` accepts a set of required tags and reports the services missing one or more of them.

## Stretch Goals

- Explore `collections.deque` for work queues that need fast pops from both ends.
- Use dictionary comprehensions to shape payloads for upcoming API calls (GitHub or Jenkins).
- Combine sets and comprehensions to surface owners who maintain more than three services.