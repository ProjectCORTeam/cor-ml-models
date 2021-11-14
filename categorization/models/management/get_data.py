import click
import boto3
from botocore.exceptions import NoCredentialsError

import os
from dotenv import load_dotenv
load_dotenv()

S3_FOLDER = 'inputs'

@click.command(name='get_data')
@click.option('--dataset_name', '-d',
                default='dataset.csv',
                show_default=True,
                type=str,
                help='Name of the dataset stored in S3 bucket.')

def download_from_s3(dataset_name):
    s3 = boto3.client('s3', aws_access_key_id = os.getenv('S3_ACCESS_KEY'),
                      aws_secret_access_key = os.getenv('S3_SECRET_KEY'))

    try:
        s3.download_file(os.getenv('S3_BUCKET_NAME'),
                        f'{S3_FOLDER}/{dataset_name}',
                        f'{os.getenv("DATA_FOLDER")}/{os.getenv("LOCAL_FILE_NAME")}')

        print("Success")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


if __name__ == '__main__':
    download_from_s3()