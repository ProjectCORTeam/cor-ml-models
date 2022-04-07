"""Utils."""

import codecs
import json
import logging

from sklearn.model_selection import train_test_split

# Set logging config
log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)


def json_dump_unicode(data, file_path, encoding="utf-8"):
    """Store array in file_path as JSON file."""
    with codecs.open(file_path, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def json_load(file_path):
    """Load JSON file.

    Arguments:
        file_path {string} -- JSON file path.
    """
    with open(file_path, "r") as jfile:
        data = json.load(jfile)

    return data


def split_train_val(data, val_size=0.2):
    """
    Split data into train and validation set.

    Args:
        data (list): dataset
        val_size (float): proportion of the dataset to include in the val split.
    Return:
        train and validations set
    """
    X, y = zip(*data)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=val_size)
    train = [(x, y) for x, y in zip(X_train, y_train)]
    val = [(x, y) for x, y in zip(X_val, y_val)]
    return train, val
