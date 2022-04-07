"""Train supervised model script."""

import logging

import click

from categorization.settings.constants import VALID_MODELS

# Set logging config
log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


@click.command(name="train_supervised_model")
@click.option(
    "--context_dir",
    type=click.Path(writable=True, dir_okay=True),
    help="pathname to the context dir",
)
@click.option("--model_name", type=click.Choice(VALID_MODELS))
def train_supervised_model_cli(context_dir, model_name):
    """Train and dump the model."""
    pass


if __name__ == "__main__":
    train_supervised_model_cli()
