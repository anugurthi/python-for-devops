# Day 6 · Files & Logging

Today we will learn how to read and write files, and how to keep a record (log) of what our script is doing.

## What You Will Learn

-   **File I/O:** How to open, read, and save files.
-   **Logging:** How to write messages to a file so you can see what happened later.
-   **Operators:** Using math (+, -) and comparisons (>, ==) to make decisions.

## Instructions

1.  **Read:** Understand that `open()` is how we access files.
2.  **Run Example:** Run the script to update a configuration file.
    ```bash
    cd examples/file-automation
    # Check the file before
    cat server.conf
    
    # Run the update script
    python3 update_server.py
    
    # Check the file after (MAX_CONNECTIONS should change)
    cat server.conf
    ```
3.  **Experiment:** Change the `key_to_update` in the script to update a different setting.

## Checklist

-   [ ] I can read a file using `with open(...)`.
-   [ ] I can write text to a file.