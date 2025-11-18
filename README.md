# Python for DevOps — 14-Days Schedule

Welcome! This two-week track walks you through the Python skills that power modern DevOps workflows—from simple scripts to cloud automation. Python is the go-to language for AWS and other clouds because it’s readable, batteries-included, and supported by every major provider. You’ll use tools like `boto3` for infrastructure, `requests` for APIs, and lightweight modules that knit CI/CD pipelines together.

Move day by day (`Day-XX/`), try the exercises, and adapt the code to your own environment. By the end you’ll see how one language lets you script local tasks, automate release pipelines, and orchestrate cloud services.

### Why Python matters in DevOps

- **Automation glue:** Python bridges gaps between Terraform plans, shell scripts, and platform APIs without a steep learning curve.
- **Cloud tooling:** AWS, Azure, GCP, and Kubernetes ship first-class SDKs and CLIs in Python, making it easy to automate resource provisioning and audits.
- **CI/CD scripting:** Pipelines use Python for test runners, deployment hooks, and verification steps.
- **Serverless & event-driven:** Services like AWS Lambda support Python out of the box, letting DevOps teams build quick event processors and remediation bots.
- **Community & libraries:** Thousands of open-source modules shorten development time and encourage reusable playbooks.

## Getting Started

1. **Install Python 3.10+** using the OS-specific steps in `Day-01/README.md` (Homebrew, Windows installer, or apt).
2. **Clone the repo** and explore the days sequentially.
3. **Create a virtual environment** before installing dependencies such as `requests`, `boto3`, or `python-jenkins`: `python3 -m venv .venv && source .venv/bin/activate`.
4. **Install common dependencies** once you reach automation week:
	```bash
	pip install -r requirements.txt
	```
5. **Set up environment variables** (API tokens, credentials) with the `.env.example` templates you’ll create in later days.
6. **Capture notes and blockers** in each `Day-XX/notes.md` so you can iterate quickly.

### Recommended Toolkit

- Python 3.10+
- VS Code (Python + REST Client extensions recommended)
- curl/Postman for API exploration
- Access to: GitHub personal access token, Jenkins server (or local instance), SonarQube instance, AWS credentials

## Week 1 — Python Foundations for Automation

| Day | Theme | Repo Guide | Outcomes |
| --- | --- | --- | --- |
| 1 | Environment bootstrap | `Day-01/` | Install Python, configure editor, run first script, document goals. |
| 2 | Data types & strings | `Day-02/` | Work with core types, string formatting, regex for log parsing. |
| 3 | Variables & configuration | `Day-03/` | Manage scope, constants, and configuration patterns. |
| 4 | Functions & modularity | `Day-04/` | Build reusable helpers, packages, and testable modules. |
| 5 | Command-line interfaces | `Day-05/` | Handle env vars, CLI arguments, and `.env` secrets. |
| 6 | Files, logging, and operators | `Day-06/` | Read/write configs, log events, apply Python operators. |
| 7 | Conditional logic | `Day-07/` | Build guard clauses, deployment gates, and decision trees. |

## Week 2 — DevOps Automation Projects

| Day | Theme | Repo Guide | Outcomes |
| --- | --- | --- | --- |
| 8 | Collections & data structures | `Day-08/` | Model inventories with lists, tuples, dictionaries, and sets. |
| 9 | Loops & iteration patterns | `Day-09/` | Master for/while loops, loop controls, and pagination patterns. |
| 10 | HTTP, REST, and auth basics | `Day-10/` | Explore requests, API tokens, pagination, JSON parsing. |
| 11 | Automate GitHub repository creation | `Day-11/` | Use GitHub REST API to create repos, manage descriptions, and initialize files. |
| 12 | Manage Jenkins jobs via API | `Day-12/` | Authenticate with Jenkins, create/update jobs from Python, trigger builds. |
| 13 | Provision SonarQube projects | `Day-13/` | Call SonarQube APIs to create projects, generate tokens, configure quality profiles. |
| 14 | AWS inventory & tag auditing | `Day-14/` | Use boto3 to inventory resources and enforce tagging standards. |

> 🎯 **Capstone idea (optional):** Stitch together the GitHub, Jenkins, SonarQube, and AWS scripts into a single onboarding pipeline once you finish Day 14.

## Hands-On Assets at a Glance

- `Day-11/examples/create_github_repo.py` — Create and configure a GitHub repository via REST API.
- `Day-12/examples/jenkins_job_provisioner.py` — Define or update Jenkins jobs with XML payloads using Python.
- `Day-13/examples/sonarqube_project_setup.py` — Register SonarQube projects and provision tokens for CI.
- `Day-14/examples/aws_tag_audit.py` — Enumerate AWS resources filtered by tag key/value pairs.
- `simple-python-app/app.py` — Lightweight Flask app for CI/CD experiments.

## Study Tips for Beginners

- **Tinker daily.** Adjust arguments, change payloads, and observe API responses to deepen understanding.
- **Secure secrets.** Use `.env` files or secret managers; never commit tokens. Later days include helpers for this.
- **Automate validation.** Pair scripts with smoke tests—e.g., call the GitHub API to verify repo creation succeeded.
- **Reflect often.** Set a daily 5-minute retrospective to note what clicked and what needs review.

## Going Further

- Extend the AWS scripts to remediate resources missing required tags.
- Add Slack or Teams notifications around Jenkins job creation.
- Containerize the tooling and wire it into a self-service developer portal.
- Share progress on LinkedIn or internal wikis to gather feedback and stay accountable.

Happy automating! 🚀
