"""Constants file."""
import os

from pathlib import Path

from categorization.settings import BASE_PATH

PROJECT_PATH = Path(__file__).resolve().parents[0]

S3_INPUTS_FOLDER = "inputs"
S3_OUTPUTS_FOLDER = "outputs"
S3_FILE_NAME = "model.pkl"

# SAVED_MODELS_PATH = BASE_PATH / "models" / "saved_models"

SAVED_MODELS_PATH = "categorization/models/saved_models"
MODEL_FILE_PATH = f"{SAVED_MODELS_PATH}/{S3_FILE_NAME}"