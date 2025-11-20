# Day 7 · Conditional Logic (If/Else)

Today we will learn how to make our scripts "smart" by making decisions.

## What You Will Learn

-   **If/Else:** How to run code only when something is true (like "if it is Monday, send email").
-   **Logic:** Combining conditions (like "if it is Monday AND it is 9am").

## Instructions

1.  **Read:** The examples below show how `if`, `elif`, and `else` work.
2.  **Run Example:** Run the script to see if you are allowed to deploy.
    ```bash
    cd examples
    # Run it (it might fail if you are outside business hours!)
    python3 deployment_gate.py
    ```
3.  **Experiment:** Try "forcing" the deployment by setting an environment variable:
    ```bash
    export DEPLOY_APPROVED="true"
    python3 deployment_gate.py
    ```

## Checklist

-   [ ] I understand `if`, `elif`, and `else`.
-   [ ] I can write a script that says "Good Morning" if it's before noon, and "Good Afternoon" otherwise.

---

# Python Conditionals

## 1. The `if` Statement
Runs code only if the condition is True.
```python
x = 10
if x > 5:
    print("x is big")
```

## 2. The `else` Statement
Runs code if the `if` condition was False.
```python
x = 3
if x > 5:
    print("x is big")
else:
    print("x is small")
```

## 3. The `elif` Statement
Checks another condition if the first one was False.
```python
x = 5
if x > 5:
    print("x is big")
elif x == 5:
    print("x is exactly 5")
else:
    print("x is small")
```
