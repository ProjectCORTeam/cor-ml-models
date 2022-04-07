from shutil import copy

import click

dst = "../../../datasets"


@click.command(name="grab data")
@click.option(
    "--path", type=click.Path(writable=True, dir_okay=True), help="Path to csv dataset."
)
def load_dataset(path):
    """Grabs dataset."""
    copy(path, dst)


if __name__ == "__main__":
    load_dataset()
