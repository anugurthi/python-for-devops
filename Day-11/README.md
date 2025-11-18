# Day 11 · Automate GitHub Repository Provisioning

The next three days focus on platform automation. First up: using Python to create and bootstrap GitHub repositories via the REST API.

## Learning Goals

- Authenticate to the GitHub REST API with a personal access token stored in `.env`.
- Create repositories with specific settings (visibility, topics, default branch).
- Initialize repos by committing README/license files or enabling branch protection.

## Agenda

1. Review GitHub’s REST docs for `POST /user/repos` and related endpoints.
2. Study `examples/create_github_repo.py` and `github_repo_config.sample.json` to identify required payload fields.
3. Build helpers for idempotency (skip creation if the repo already exists).
4. Log results clearly so you can verify via the API or GitHub UI.

## Practice Prompts

- Add optional arguments to enable issues, wiki, or secrets scanning.
- Create a function that seeds a repository with starter files using the GitHub Contents API.
- Implement branch protection rules using the `PUT /repos/{owner}/{repo}/branches/{branch}/protection` endpoint.

## Deliverable

Commit `examples/create_github_repo.py` that reads config from a JSON/YAML file, creates the repo, and prints its URL. Include dry-run and verbose modes.

## Stretch Goals

- Integrate with GitHub templates or organization-level default settings.
- Post creation details to Slack or Teams via webhook.