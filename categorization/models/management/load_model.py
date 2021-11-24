import boto3
import click
from botocore.exceptions import NoCredentialsError

from categorization.settings.constants import S3_FILE_NAME
from categorization.settings.credentials import (
    DATA_FOLDER,
    LOCAL_FILE_NAME,
    S3_ACCESS_KEY,
    S3_BUCKET_NAME,
    S3_SECRET_KEY,
)
from categorization.settings.log import logger


@click.command(name="load_model")
def upload_to_s3():
    s3 = boto3.client(
        "s3", aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY
    )

    try:
        s3.upload_file(f"{DATA_FOLDER}/{LOCAL_FILE_NAME}", S3_BUCKET_NAME, S3_FILE_NAME)
        logger.info("Upload Successful")
        return True
    except FileNotFoundError:
        logger.info("The file was not found")
        return False
    except NoCredentialsError:
        logger.info("Credentials not available")
        return False


if __name__ == "__main__":
    upload_to_s3()
