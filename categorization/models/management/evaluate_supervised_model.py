"""Evaluate model script."""

import logging

import click

# Set logging config
log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


@click.command(name="evaluate_supervised")
@click.option(
    "--context_dir",
    type=click.Path(writable=True, dir_okay=True),
    help="Path dir to asgstore the features",
)
def evaluate_supervised_cli(context_dir, model_name):
    """Evaluate model script for atribute prediction."""
    pass


if __name__ == "__main__":
    evaluate_supervised_cli()
