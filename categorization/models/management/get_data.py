import boto3
import click
from botocore.exceptions import NoCredentialsError

from categorization.settings.constants import (
    S3_INPUTS_FOLDER
    )

from categorization.settings.credentials import (    
    S3_ACCESS_KEY,
    S3_BUCKET_NAME,
    S3_SECRET_KEY,
    LOCAL_DATA_FOLDER,
    LOCAL_DATASET_NAME,
    VALID_LANGS
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
@click.option(
    "--language",
    "-l",
    type=click.Choice(VALID_LANGS.split(",")),
    help="Language of the model to be stored in S3.",
)


def download_from_s3(dataset_name,language):
    s3 = boto3.client(
        "s3", aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY
    )
    try:
        logger.info(f"Downloading dataset from S3 Bucket")
        s3.download_file(
            S3_BUCKET_NAME,
            f"{S3_INPUTS_FOLDER}/{language}/{dataset_name}",
            f"{LOCAL_DATA_FOLDER}/{language}/{LOCAL_DATASET_NAME}"
        )

        logger.info("Successful download from S3")
        return True
    except FileNotFoundError:
        logger.info("The file was not found")
        return False
    except NoCredentialsError:
        logger.info("Credentials not available")
        return False


if __name__ == "__main__":
    download_from_s3()
