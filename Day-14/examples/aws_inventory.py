"""Quick inventory script that lists EC2 instances and S3 buckets.

This sample is intentionally lightweight so you can expand it with additional
services or fields.
"""

from __future__ import annotations

import argparse
from typing import Iterable

import boto3


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List EC2 instances and S3 buckets")
    parser.add_argument("--region", help="AWS region (defaults to environment/session)")
    parser.add_argument("--profile", help="AWS CLI profile name")
    return parser.parse_args()


def create_session(region: str | None, profile: str | None) -> boto3.session.Session:
    if profile:
        return boto3.session.Session(profile_name=profile, region_name=region)
    return boto3.session.Session(region_name=region)


def list_ec2(session: boto3.session.Session) -> Iterable[str]:
    client = session.client("ec2")
    paginator = client.get_paginator("describe_instances")
    for page in paginator.paginate():
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                name_tag = next((t["Value"] for t in instance.get("Tags", []) if t["Key"] == "Name"), None)
                yield f"EC2: {instance['InstanceId']} | state={instance['State']['Name']} | name={name_tag or '-'}"


def list_s3(session: boto3.session.Session) -> Iterable[str]:
    client = session.client("s3")
    response = client.list_buckets()
    for bucket in response.get("Buckets", []):
        yield f"S3: {bucket['Name']}"


def main() -> None:
    args = parse_args()
    session = create_session(args.region, args.profile)
    for line in list_ec2(session):
        print(line)
    for line in list_s3(session):
        print(line)


if __name__ == "__main__":
    main()
