"""Day 3 example: demonstrate variable scope and environment defaults."""

import os  # 'os' lets us talk to the operating system (like reading environment variables)

# This is a GLOBAL variable. It can be seen by any function in this file.
DEFAULT_REGION = "us-east-1"

def resolve_region(env_var: str = "AWS_REGION") -> str:
    """Return a deployment region prioritizing environment configuration."""
    
    # os.getenv() looks for a variable set in your terminal (e.g., export AWS_REGION=us-west-1)
    region = os.getenv(env_var)
    
    # If we found a region in the environment, use it.
    if region:
        return region
        
    # Otherwise, use the default value we defined at the top.
    return DEFAULT_REGION


def main() -> None:
    region = resolve_region()
    print(f"Deploying automation to region: {region}")


if __name__ == "__main__":
    main()
