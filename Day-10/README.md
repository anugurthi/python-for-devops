# Day 10 · Calling APIs with Python

Today we will learn how to talk to web services (APIs) using Python. This is how you automate tools like GitHub, Jenkins, and AWS.

## What You Will Learn

-   **HTTP Requests:** How to ask a web service for data (GET) or send data toit (POST).
-   **Authentication:** How to prove who you are (using tokens).
-   **JSON:** How to work with data in JSON format.

## Instructions

1.  **Read:** Understand that `requests` is the library we use to call APIs.
2.  **Run Example:** Run the script to get a list of GitHub pull requests.
    ```bash
    cd examples
    python3 list_open_pull_requests.py
    ```
3.  **Experiment:** Set a GitHub token to get higher rate limits:
    ```bash
    export GITHUB_TOKEN="your_token_here"
    python3 list_open_pull_requests.py
    ```

## Checklist

-   [ ] I can make a GET request to an API.
-   [ ] I understand that APIs return data in JSON format.