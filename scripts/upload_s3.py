import os
import boto3
from botocore.exceptions import NoCredentialsError

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED = os.path.join(BASE, "data", "processed")
FILE = os.path.join(PROCESSED, "orders_processed.csv")

BUCKET_NAME = "ecommerce-data-greeshma"

def upload_to_s3():
    s3 = boto3.client("s3")

    try:
        s3.upload_file(FILE, BUCKET_NAME, "orders_processed.csv")
        print("Upload successful")
    except FileNotFoundError:
        print("File not found")
    except NoCredentialsError:
        print("AWS credentials not found")

if __name__ == "__main__":
    upload_to_s3()
