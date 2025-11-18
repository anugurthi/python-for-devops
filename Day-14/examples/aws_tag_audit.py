"""List AWS resources that contain a specific tag key (and optional value).

Usage example:
    export AWS_PROFILE=dev
    python aws_tag_audit.py --tag-key Owner --tag-value platform --services ec2,s3 --region us-east-1
"""

from __future__ import annotations

import argparse
import collections
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

import boto3
from botocore.exceptions import ClientError


@dataclass
class ResourceRecord:
    service: str
    identifier: str
    region: str
    tags: Dict[str, str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan AWS resources for a specific tag")
    parser.add_argument("--tag-key", required=True, help="Tag key to search for")
    parser.add_argument("--tag-value", help="Optional tag value to match")
    parser.add_argument("--services", default="ec2,s3,rds", help="Comma-separated services to scan (ec2,s3,rds)")
    parser.add_argument("--region", help="AWS region to use (defaults to session region)")
    parser.add_argument("--profile", help="AWS CLI profile name")
    parser.add_argument("--include-missing", action="store_true", help="Also report resources missing the tag")
    return parser.parse_args()


def create_session(region: Optional[str], profile: Optional[str]) -> boto3.session.Session:
    if profile:
        return boto3.session.Session(profile_name=profile, region_name=region)
    return boto3.session.Session(region_name=region)


def match_tag(tags: Dict[str, str], key: str, value: Optional[str]) -> bool:
    if key not in tags:
        return False
    if value is None:
        return True
    return tags[key] == value


def gather_ec2(session: boto3.session.Session, key: str, value: Optional[str], include_missing: bool) -> Iterable[ResourceRecord]:
    client = session.client("ec2")
    filters = [
        {"Name": f"tag:{key}", "Values": [value]} if value is not None else {"Name": "tag-key", "Values": [key]}
    ]
    paginator = client.get_paginator("describe_instances")
    seen_ids: set[str] = set()
    for page in paginator.paginate(Filters=filters if value is not None else None):
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instance_id = instance["InstanceId"]
                if instance_id in seen_ids:
                    continue
                seen_ids.add(instance_id)
                tag_map = {t['Key']: t['Value'] for t in instance.get('Tags', [])}
                if match_tag(tag_map, key, value):
                    yield ResourceRecord("ec2", instance_id, session.region_name or "-", tag_map)
    if include_missing:
        paginator = client.get_paginator("describe_instances")
        for page in paginator.paginate():
            for reservation in page.get("Reservations", []):
                for instance in reservation.get("Instances", []):
                    tag_map = {t['Key']: t['Value'] for t in instance.get('Tags', [])}
                    if key not in tag_map:
                        yield ResourceRecord("ec2", instance["InstanceId"], session.region_name or "-", tag_map)


def gather_rds(session: boto3.session.Session, key: str, value: Optional[str], include_missing: bool) -> Iterable[ResourceRecord]:
    client = session.client("rds")
    paginator = client.get_paginator("describe_db_instances")
    for page in paginator.paginate():
        for instance in page.get("DBInstances", []):
            arn = instance["DBInstanceArn"]
            try:
                tags_response = client.list_tags_for_resource(ResourceName=arn)
            except ClientError as exc:
                if exc.response["Error"]["Code"] == "AccessDenied":
                    continue
                raise
            tag_map = {t['Key']: t['Value'] for t in tags_response.get('TagList', [])}
            if match_tag(tag_map, key, value):
                yield ResourceRecord("rds", instance["DBInstanceIdentifier"], session.region_name or "-", tag_map)
            elif include_missing and key not in tag_map:
                yield ResourceRecord("rds", instance["DBInstanceIdentifier"], session.region_name or "-", tag_map)


def gather_s3(session: boto3.session.Session, key: str, value: Optional[str], include_missing: bool) -> Iterable[ResourceRecord]:
    client = session.client("s3")
    response = client.list_buckets()
    for bucket in response.get("Buckets", []):
        name = bucket["Name"]
        try:
            tagging = client.get_bucket_tagging(Bucket=name)
            tag_map = {t['Key']: t['Value'] for t in tagging.get('TagSet', [])}
        except ClientError as exc:
            error_code = exc.response["Error"].get("Code")
            if error_code in {"NoSuchTagSet", "AccessDenied"}:
                tag_map = {}
            else:
                raise
        if match_tag(tag_map, key, value):
            region = client.get_bucket_location(Bucket=name).get("LocationConstraint") or "us-east-1"
            yield ResourceRecord("s3", name, region, tag_map)
        elif include_missing and key not in tag_map:
            region = client.get_bucket_location(Bucket=name).get("LocationConstraint") or "us-east-1"
            yield ResourceRecord("s3", name, region, tag_map)


SERVICE_DISPATCH = {
    "ec2": gather_ec2,
    "s3": gather_s3,
    "rds": gather_rds,
}


def main() -> None:
    args = parse_args()
    services = [svc.strip().lower() for svc in args.services.split(",") if svc.strip()]
    invalid = [svc for svc in services if svc not in SERVICE_DISPATCH]
    if invalid:
        raise SystemExit(f"Unsupported services requested: {', '.join(invalid)}")

    session = create_session(args.region, args.profile)

    all_records: List[ResourceRecord] = []
    for service in services:
        gatherer = SERVICE_DISPATCH[service]
        for record in gatherer(session, args.tag_key, args.tag_value, args.include_missing):
            all_records.append(record)

    if not all_records:
        print("No resources matched the criteria.")
        return

    grouped = collections.defaultdict(list)
    for record in all_records:
        grouped[record.service].append(record)

    for service, records in grouped.items():
        print(f"\nService: {service}  (count={len(records)})")
        for record in records:
            value = record.tags.get(args.tag_key, "<missing>")
            print(f"  - {record.identifier} | region={record.region} | {args.tag_key}={value}")


if __name__ == "__main__":
    main()
