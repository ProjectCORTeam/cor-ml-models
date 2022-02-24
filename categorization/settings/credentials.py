import os

from dotenv import find_dotenv, load_dotenv

# find .env automagically by walking up directories until it's found, then
# load up the .env entries as environment variables
load_dotenv(find_dotenv())


S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY", "")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY", "")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "")

LOCAL_DATA_FOLDER = os.getenv("LOCAL_DATA_FOLDER", "")
LOCAL_DATASET_NAME = os.getenv("LOCAL_DATASET_NAME", "")
VALID_MODELS = os.getenv("VALID_MODELS", "")
VALID_LANGS = os.getenv("VALID_LANGS", "")


