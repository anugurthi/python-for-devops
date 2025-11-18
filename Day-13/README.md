# Day 13 · SonarQube Project Automation

Today’s focus is SonarQube: programmatically creating projects, provisioning tokens, and wiring code quality checks into your CI pipelines.

## Learning Goals

- Authenticate to SonarQube’s REST API using admin tokens.
- Provision new projects and generate analysis tokens on demand.
- Configure quality profiles or gates via API calls.

## Agenda

1. Review SonarQube API docs for project creation and token management.
2. Explore `examples/sonarqube_project_setup.py` and `sonarqube_project.sample.yaml` to understand required payloads.
3. Build a helper that checks whether a project exists before creating it (idempotency).
4. Document quality gate requirements for your organization.

## Practice Prompts

- Create a script that assigns a project to a specific quality profile.
- Generate a long-lived token and store it securely (e.g., in a `.env` file or secrets manager).
- Trigger a sample analysis using the generated token and log the result URL.

## Deliverable

Commit `examples/sonarqube_project_setup.py` plus a `config.json` sample describing project key, name, default branch, and quality profile.

## Stretch Goals

- Integrate with Jenkins Job DSL so the token feeds into your CI pipeline automatically.
- Query SonarQube for existing issues and produce a summary report.
