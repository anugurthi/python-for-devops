# Day 10 · HTTP, REST, and Authentication Fundamentals

Before we automate GitHub, Jenkins, or SonarQube, we need to understand how APIs expect requests. Today is about HTTP verbs, status codes, headers, and auth flows.

## Learning Goals

- Issue GET/POST/PUT/DELETE requests using the `requests` library.
- Handle authentication via personal access tokens (PATs) and basic auth.
- Parse JSON responses and deal with pagination or rate limits.

## Agenda

1. Use `requests` to call a public API (e.g., GitHub’s rate limit endpoint) and inspect headers.
2. Practice sending authenticated requests with a dummy token (stored in `.env`).
3. Write helper functions that wrap API calls with retry logic and consolidated error handling.
4. Capture findings in a `notes.md` file.

## Practice Prompts

- Implement a `call_api` utility that logs the URL, status code, and elapsed time.
- Parse JSON into Python dictionaries and extract specific fields (e.g., repo names, job counts).
- Handle `429 Too Many Requests` by respecting `Retry-After` headers.

## Deliverable

Commit a `rest_client.py` that exposes a `request_json(method, url, **kwargs)` helper reused in future days.

## Stretch Goals

- Explore OAuth flows conceptually and outline how you’d integrate them.
- Use `httpx` or `aiohttp` for async API calls and compare performance.