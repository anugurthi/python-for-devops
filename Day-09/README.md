# Day 9 · Loops & Iteration Patterns

Automation scripts thrive on iteration—looping through servers, log lines, or API responses. Today you’ll sharpen your loop skills and prepare for pagination-heavy API calls next week.

## Learning Goals

- Choose between `for` and `while` loops based on the problem.
- Use `break`, `continue`, and `else` clauses for fine-grained control.
- Iterate safely over nested data structures.

## Agenda

1. Read `01-loops.md` and `02-loop-controls.md` for a refresher.
2. Work through `03-for-loop-devops-usecases.md` and `04-while-loop-devops-usecases.md` examples.
3. Implement a loop inside `examples/` (see `examples/pagination_loop.py`) that paginates through mocked API responses stored in a list.
4. Record takeaways and questions in your notes.

## Practice Prompts

- Iterate over a list of repositories and print which ones need default branches renamed.
- Use a `while` loop to retry an API call up to three times with exponential backoff.
- Combine loops with list comprehensions to flatten nested inventories.

## Deliverable

Commit a script in `examples/` that loops through service definitions, validates required fields, and reports any missing metadata.

## Stretch Goals

- Profile loop performance with Python’s `timeit` module.
- Explore generator functions to stream large datasets without loading them fully into memory.