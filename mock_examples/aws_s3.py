from typing import Any
import boto3


def get_my_object(bucket: str, key: str) -> Any:
    """
    Function to get an object from S3
    :param bucket: Bucket name
    :param key: Key name
    :return: Response from S3
    """
    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket=bucket, Key=key)
    return response
