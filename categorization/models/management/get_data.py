import boto3
import click
from botocore.exceptions import NoCredentialsError

from categorization.settings.constants import S3_FOLDER
from categorization.settings.credentials import (
    DATA_FOLDER,
    LOCAL_FILE_NAME,
    S3_ACCESS_KEY,
    S3_BUCKET_NAME,
    S3_SECRET_KEY,
)
from categorization.settings.log import logger


@click.command(name="get_data")
@click.option(
    "--dataset_name",
    "-d",
    default="dataset.csv",
    show_default=True,
    type=str,
    help="Name of the dataset stored in S3 bucket.",
)
def download_from_s3(dataset_name):
    s3 = boto3.client(
        "s3", aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY
    )

    try:
        s3.download_file(
            S3_BUCKET_NAME,
            f"{S3_FOLDER}/{dataset_name}",
            f"{DATA_FOLDER}/{LOCAL_FILE_NAME}",
        )

        logger.info("S3 loggin success")
        return True
    except FileNotFoundError:
        logger.info("The file was not found")
        return False
    except NoCredentialsError:
        logger.info("Credentials not available")
        return False


if __name__ == "__main__":
    download_from_s3()
