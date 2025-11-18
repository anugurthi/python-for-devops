# Day 7 · Conditional Logic for Automation

Conditional statements are a fundamental part of programming that allow you to make decisions and execute different blocks of code based on certain conditions. In DevOps tooling, conditional logic guards destructive operations, skips work in dry-run mode, and escalates alerts when thresholds are exceeded. In Python, you can use `if`, `elif`, and `else` to implement these rules.

## Learning Goals

- Chain multiple conditions together to model decision trees.
- Short-circuit execution using `return` and guard clauses.
- Combine conditionals with logging to explain control flow.

## Agenda

1. Work through the refresher below on `if`, `elif`, and `else`.
2. Add conditional checks to the log-writer script from Day 6 (e.g., skip writes in dry-run mode).
3. Write a script in `examples/` (see `examples/deployment_gate.py`) that enforces business rules (time windows, approvals, feature flags).
4. Journal about tricky conditional bugs you’ve hit before and how to avoid them.

---

# Conditional Statements in Python

Conditional statements are a fundamental part of programming that allow you to make decisions and execute different blocks of code based on certain conditions. In Python, you can use `if`, `elif` (short for "else if"), and `else` to create conditional statements.

## `if` Statement

The `if` statement is used to execute a block of code if a specified condition is `True`. If the condition is `False`, the code block is skipped.

```python
if condition:
    # Code to execute if the condition is True
```

- Example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## `elif` Statement

The `elif` statement allows you to check additional conditions if the previous `if` or `elif` conditions are `False`. You can have multiple `elif` statements after the initial `if` statement.

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
elif condition3:
    # Code to execute if condition3 is True
# ...
else:
    # Code to execute if none of the conditions are True
```

- Example:

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is not greater than 5")
```

## `else` Statement

The `else` statement is used to specify a block of code to execute when none of the previous conditions (in the `if` and `elif` statements) are `True`.

```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

- Example:

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```
