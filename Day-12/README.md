# Day 12 · Jenkins Job Provisioning via Python

With GitHub automation in place, you’ll now define Jenkins jobs programmatically. The objective is to provision or update a pipeline whenever a new repository is created.

## Learning Goals

- Authenticate with Jenkins using API tokens and crumb issuers.
- Create or update freestyle and pipeline jobs via XML definitions.
- Trigger builds and monitor their status from Python.

## Agenda

1. Review Jenkins REST API basics and the `python-jenkins` library.
2. Examine `examples/jenkins_job_provisioner.py` and `jenkins_job_config.sample.yaml` for creating jobs from templates.
3. Build idempotent logic: update the job if it already exists, otherwise create it.
4. Log and verify results through Jenkins UI or API calls.

## Practice Prompts

- Create a parameterized Jenkins job that accepts a Git repository URL.
- Configure post-build actions (e.g., trigger SonarQube analysis) via XML config updates.
- Trigger a build and stream console output in Python.

## Deliverable

Commit `examples/jenkins_job_provisioner.py` plus a sample job template (`pipeline_job.xml.j2`) that provisions a CI pipeline aligned with your GitHub repos.

## Stretch Goals

- Add folder support by creating nested Jenkins folders before job creation.
- Integrate credentials binding for secure secret handling.
