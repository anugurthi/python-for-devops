# Day 14 · AWS Inventory & Tag Auditing

Wrap up the 14-day sprint by inspecting AWS environments with Python. You’ll list foundational resources (EC2, S3, RDS) and build a tag-audit report to highlight compliance gaps.

## Learning Goals

- Configure boto3 sessions with profiles and regions.
- Paginate through AWS APIs to aggregate resources reliably.
- Filter resources by tag key/value pairs and flag missing metadata.

## Agenda

1. Review AWS authentication options (environment variables, profiles, IAM roles).
2. Run `examples/aws_inventory.py` to enumerate EC2 instances and S3 buckets in your sandbox account.
3. Study `examples/aws_tag_audit.py` and experiment with different `--services` combinations.
4. Export findings to a CSV/JSON summary for your stakeholders.

## Practice Prompts

- Extend `examples/aws_inventory.py` to include RDS instance identifiers and states.
- Add an option to `examples/aws_tag_audit.py` that writes missing-tag resources to `missing_tags.json`.
- Support multi-region scans by iterating over a list of regions pulled from AWS Organizations or config files.

## Deliverable

Commit updated AWS utilities that can:

- Print a human-readable inventory of EC2 instances and S3 buckets.
- Report resources missing required tags using `--include-missing`.

## Stretch Goals

- Integrate with AWS Organizations or Control Tower to loop through multiple accounts.
- Send audit results to Slack, email, or ticketing systems for follow-up.