"""Constants file."""
from pathlib import Path

from categorization.settings import BASE_PATH

PROJECT_PATH = Path(__file__).resolve().parents[0]

S3_FOLDER = "inputs"
S3_FILE_NAME = "outputs/model.pkl"


SAVED_MODELS_PATH = BASE_PATH / "models" / "saved_models"
MODEL_FILE_PATH = SAVED_MODELS_PATH / "model.pkl"
