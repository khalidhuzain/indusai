"""
Optional diagnostic script.
Verifies that AWS credentials are correctly loaded.

This script is NOT required to run the exercises.
"""
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

try:
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()

    print("✅ AWS credentials are valid")
    print(f"Account : {identity['Account']}")
    print(f"ARN     : {identity['Arn']}")

except NoCredentialsError:
    print("❌ No AWS credentials found.")
    print("👉 Please set environment variables and try again.")

except ClientError as e:
    print("❌ AWS credentials are invalid or expired.")
    print(f"Details: {e}")
