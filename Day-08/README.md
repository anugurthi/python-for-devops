# Day 8 · Lists & Dictionaries

Today we will learn how to store *collections* of data. Instead of having `server1`, `server2`, `server3`, we can have a single list called `servers`.

## What You Will Learn

-   **Lists:** An ordered list of items (e.g., `["web-server", "db-server"]`).
-   **Dictionaries:** Data stored in key-value pairs (e.g., `{"name": "web-server", "ip": "10.0.0.1"}`).
-   **Sets:** A list where every item is unique (no duplicates allowed).

## Instructions

1.  **Read:** The examples below show how to use Lists and Dictionaries.
2.  **Run Example:** Run the script to list files in different folders.
    ```bash
    cd examples
    # Enter folder names when prompted (e.g., /tmp /var)
    python3 03-list-files-in-folders.py
    ```
3.  **Experiment:** Try passing a folder that doesn't exist to see how the script handles errors.

## Checklist

-   [ ] I can create a list: `my_list = [1, 2, 3]`.
-   [ ] I can create a dictionary: `my_dict = {"key": "value"}`.

---

# Python Collections

## 1. Lists
Great for keeping track of things in order.
```python
servers = ["web-01", "db-01", "cache-01"]
print(servers[0])  # Prints "web-01"
```

## 2. Dictionaries
Great for storing details about a specific thing.
```python
server_config = {
    "hostname": "web-01",
    "ip": "192.168.1.5",
    "active": True
}
print(server_config["ip"])  # Prints "192.168.1.5"
```