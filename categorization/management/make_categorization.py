"""Make catalog script."""
import os
import click
import logging
import json
import pandas as pd



# Set logging config
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)



@click.command(name='make_catalog')
@click.option('--context_dir', type=click.Path(writable=True, dir_okay=True),
              help='Path dir to store the features')
def make_categorization_cli(context_dir):
    """Make catalog script."""
    pass

if __name__ == '__main__':
    make_categorization_cli()
