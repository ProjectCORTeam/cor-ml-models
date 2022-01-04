import click
import pandas as pd

from categorization.models.sklearn.sk_models import Categorizer
from categorization.settings.constants import MODEL_FILE_PATH
from categorization.settings.credentials import (
    DATA_FOLDER,
    LOCAL_FILE_NAME,
    VALID_MODELS,
)
from categorization.settings.log import logger

SELECTED_CATEGORIES = [
    "ACCOUNT MANAGEMENT",
    "DESIGN",
    "STRATEGY",
    "CREATIVE",
    "SOFTWARE & UX/UI",
    "SOCIAL MEDIA",
]

@click.command(name="train_model")
@click.option(
    "--model_name",
    "-m",
    type=click.Choice(VALID_MODELS.split(",")),
    help="Name of the model to be trained.",
)
def train_model(model_name):
    logger.info("Getting data...")

    df = pd.read_csv(f"{DATA_FOLDER}/{LOCAL_FILE_NAME}")

    df.columns = [col.upper() for col in df.columns]


    df["CATEGORY_NAME"] = df["CATEGORY_NAME"].apply(
        lambda x: x.upper() if x.upper() in SELECTED_CATEGORIES else "Others"
    )

    X = df["DOCUMENT_DIRTY"]

    y = df["CATEGORY_NAME"]

    model = Categorizer(model_name=model_name)

    logger.info("Training model...")

    model.fit(X, y)

    logger.info("Model succesfully trained!")

    logger.info("Model metadata: ", model.get_metadata())

    task = ["campana de marketing digital en redes"]

    prediction = model.predict(task)

    logger.info(
        f"Prediction Test completed:\ntask = {task}, predicted category = {prediction}"
    )

    model.save_model(MODEL_FILE_PATH)

    logger.info(f"Model saved in! {MODEL_FILE_PATH}")


if __name__ == "__main__":
    train_model()
