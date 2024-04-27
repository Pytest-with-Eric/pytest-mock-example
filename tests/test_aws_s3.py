from moto import mock_aws
from mock_examples.aws_s3 import get_my_object


@mock_aws
def test_get_my_object_mocked(aws_s3):
    """
    Function to test get my object
    :param s3: pytest-mock fixture
    :return: None
    """
    # Create a mock S3 bucket.
    aws_s3.create_bucket(Bucket="mock-bucket")

    # Create a mock object in the mock S3 bucket.
    aws_s3.put_object(Bucket="mock-bucket", Key="mock-key", Body="mock-body")

    # Get the mock object from the mock S3 bucket.
    response = get_my_object(bucket="mock-bucket", key="mock-key")
    assert response["Body"].read() == b"mock-body"
