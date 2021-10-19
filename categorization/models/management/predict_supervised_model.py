"""Predict Supervised Model Script."""
import logging
import click
import os


from categorization.models.sklearn.sk_models import Categorizer


# Set logging config
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


@click.command(name='predict_supervised_model')
@click.option('--context_dir',
              type=click.Path(writable=True, dir_okay=True),
              help='pathname to the context dir')
def predict_supervised_model_cli(context_dir):
    """Predict script to grab attr predictions."""
    pass


if __name__ == '__main__':
    predict_supervised_model_cli()
