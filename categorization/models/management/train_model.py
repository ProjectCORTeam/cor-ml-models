import click
import pandas as pd

from categorization.models.sklearn.sk_models import Categorizer

from categorization.settings.constants import (
    SAVED_MODELS_PATH,
    MODEL_FILE_NAME    
)

from categorization.settings.credentials import (
    LOCAL_DATA_FOLDER,
    LOCAL_DATASET_NAME,
    VALID_MODELS,
    VALID_LANGS,
)

from categorization.settings.log import logger

SELECTED_CATEGORIES = {
    
    es:[
    "ACCOUNT MANAGEMENT",
    "DESIGN",
    "STRATEGY",
    "CREATIVE",
    "SOFTWARE & UX/UI",
    "SOCIAL MEDIA",
],
    en:[
    "ACCOUNT MANAGEMENT",
    "DESIGN",
    "CREATIVE",
    "SOCIAL MEDIA",
    "STRATEGY",
    "BUSINESS INTELLIGENCE",
    "SOFTWARE & UX/UI",
    "RESEARCH",
]
}

@click.command(name="train_model")
@click.option(
    "--model_name",
    "-m",
    type=click.Choice(VALID_MODELS.split(",")),
    help="Name of the model to be trained.",
)

@click.option(
    "--language",
    "-l",
    type=click.Choice(VALID_LANGS.split(",")),
    help="Language of the model to be trained.",
)


def train_model(model_name, language):
    logger.info("Getting data...")

    df = pd.read_csv(f"{LOCAL_DATA_FOLDER}/{language}/{LOCAL_DATASET_NAME}")

    df.columns = [col.upper() for col in df.columns]


    df["CATEGORY_NAME"] = df["CATEGORY_NAME"].apply(
        lambda x: x.upper() if x.upper() in SELECTED_CATEGORIES[language] else "OTHERS"
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

    model.save_model(f"{SAVED_MODELS_PATH}/{language}/{MODEL_FILE_NAME}")

    logger.info(f"Model saved in! {SAVED_MODELS_PATH}/{language}/{MODEL_FILE_NAME}")


if __name__ == "__main__":
    train_model()
