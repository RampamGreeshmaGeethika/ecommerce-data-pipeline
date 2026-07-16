import os
import sys
import boto3
from botocore.exceptions import NoCredentialsError

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from pipeline.config import load_config

PROCESSED = os.path.join(BASE, "data", "processed")
FILE = os.path.join(PROCESSED, "orders_processed.csv")

def upload_to_s3():
    config = load_config()
    if not config.s3_bucket:
        raise ValueError("PIPELINE_S3_BUCKET must be set before uploading to S3")

    s3 = boto3.client("s3")

    try:
        key = f"{config.s3_prefix.strip('/')}/orders_processed.csv"
        s3.upload_file(FILE, config.s3_bucket, key)
        print(f"Upload successful: s3://{config.s3_bucket}/{key}")
    except FileNotFoundError:
        print("File not found")
    except NoCredentialsError:
        print("AWS credentials not found")

if __name__ == "__main__":
    upload_to_s3()
