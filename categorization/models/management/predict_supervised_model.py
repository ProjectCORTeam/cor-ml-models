"""Predict Supervised Model Script."""
import click


@click.command(name="predict_supervised_model")
@click.option(
    "--context_dir",
    type=click.Path(writable=True, dir_okay=True),
    help="pathname to the context dir",
)
def predict_supervised_model_cli(context_dir):
    """Predict script to grab attr predictions."""
    pass


if __name__ == "__main__":
    predict_supervised_model_cli()
