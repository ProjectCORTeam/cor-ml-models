import boto3
import click
from botocore.exceptions import NoCredentialsError

from categorization.settings.constants import (
    S3_FILE_NAME,
    S3_OUTPUTS_FOLDER,
    MODEL_FILE_PATH
)

from categorization.settings.credentials import (
    S3_ACCESS_KEY,
    S3_BUCKET_NAME,
    S3_SECRET_KEY,
)
from categorization.settings.log import logger


@click.command(name="load_model")
@click.option(
    "--model_name",
    "-n",
    default=S3_FILE_NAME,
    show_default=True,
    type=str,
    help="Name of the model pkl file to be stored in S3 bucket.",
)
def upload_to_s3(model_name):
    s3 = boto3.client(
        "s3", aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY
    )

    logger.info("Uploading pickle file...")

    try:
        # s3.upload_file(MODEL_FILE_PATH, S3_BUCKET_NAME, f"/{S3_OUTPUTS_FOLDER}/{model_name}")
        s3.upload_file(MODEL_FILE_PATH, S3_BUCKET_NAME, f"/{S3_OUTPUTS_FOLDER}/{model_name}")
        logger.info("Successful upload to S3 ")
        return True
    except FileNotFoundError:
        logger.info("The file was not found")
        return False
    except NoCredentialsError:
        logger.info("Credentials not available")
        return False


if __name__ == "__main__":
    upload_to_s3()
