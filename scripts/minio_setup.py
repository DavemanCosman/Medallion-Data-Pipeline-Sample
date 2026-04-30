import os
from minio import Minio
from minio.error import S3Error

# set up the minIO connection
client = Minio(
    os.getenv("MINIO_ENDPOINT", "minio:9000"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

# medallion architecture buckets
BUCKETS = ["bronze","silver","gold"]

PREFIXES = {
    "bronze": [
        "weather/"
    ],
    "silver": [
        "weather/current/",
        "weather/hourly/",
        "weather/daily/",
        "weather/alerts/"
    ],
    "gold": [
        "weather/temperature_trends/",
        "weather/precipitation_patterns/",
        "weather/extreme_events/"
    ]
}

def ensure_bucket(bucket: str):
    """Create bucket if it doesn't exist."""
    if not client.bucket_exists(bucket):
        print(f"Creating bucket: {bucket}")
        client.make_bucket(bucket)
    else:
        print(f"Bucket already exists: {bucket}")

def ensure_prefix(bucket: str, prefix: str):
    """Create a folder prefix by uploading an empty placeholder."""
    placeholder = f"{prefix}__init__.keep"
    try:
        client.put_object(
            bucket,
            placeholder,
            data=b"",
            length=0
        )
        print(f"Created prefix: {bucket}/{prefix}")
    except S3Error as e:
        print(f"Error creating prefix {prefix} in {bucket}: {e}")

def main():
    print("Initializing MinIO medallion structure...")

    # Create buckets
    for bucket in BUCKETS:
        ensure_bucket(bucket)

    # Create folder prefixes
    for bucket, prefixes in PREFIXES.items():
        for prefix in prefixes:
            ensure_prefix(bucket, prefix)

    print("MinIO setup complete.")

if __name__ == "__main__":
    main()