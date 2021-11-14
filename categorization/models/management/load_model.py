import click
import boto3
from botocore.exceptions import NoCredentialsError

from dotenv import load_dotenv
import os
load_dotenv()

S3_FILE_NAME = 'outputs/model.pkl'

@click.command(name='load_model')

def upload_to_s3():
    s3 = boto3.client('s3', aws_access_key_id = os.getenv('S3_ACCESS_KEY'),
                      aws_secret_access_key = os.getenv('S3_SECRET_KEY'))

    try:
        s3.upload_file(f'{os.getenv("DATA_FOLDER")}/{os.getenv("LOCAL_FILE_NAME")}',
                        os.getenv("S3_BUCKET_NAME"), S3_FILE_NAME)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

if __name__ == '__main__':
    upload_to_s3()