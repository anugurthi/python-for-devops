# Day 9 · Loops (For & While)

Today we will learn how to repeat actions without writing the same code over and over.

## What You Will Learn

-   **For Loops:** Repeat something for every item in a list (e.g., "Restart every server").
-   **While Loops:** Repeat something *while* a condition is true (e.g., "Wait while the server is starting").

## Instructions

1.  **Read:** The examples below show how `for` and `while` loops work.
2.  **Run Example:** Run the script to see how we process data in "pages" (chunks).
    ```bash
    cd examples
    python3 pagination_loop.py
    ```
3.  **Experiment:** Change the `page_size` in the script to see how it changes the output.

## Checklist

-   [ ] I can write a loop to print numbers 1 to 10.
-   [ ] I understand when to use `for` vs `while`.

---

# Python Loops

## 1. For Loop
Best when you have a list of things.
```python
servers = ["web-01", "db-01"]
for server in servers:
    print(f"Checking {server}...")
```

## 2. While Loop
Best when you are waiting for something.
```python
count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1
```