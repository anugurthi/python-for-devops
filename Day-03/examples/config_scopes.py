"""Day 3 example: demonstrate variable scope and environment defaults."""

import os

DEFAULT_REGION = "us-east-1"

def resolve_region(env_var: str = "AWS_REGION") -> str:
    """Return a deployment region prioritizing environment configuration."""
    region = os.getenv(env_var)
    if region:
        return region
    return DEFAULT_REGION


def main() -> None:
    region = resolve_region()
    print(f"Deploying automation to region: {region}")


if __name__ == "__main__":
    main()
