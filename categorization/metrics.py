"""Metrics module to evaluate predictions."""
from sklearn.metrics import f1_score, matthews_corrcoef, precision_score, recall_score


def precision(y_true, y_pred, average=None):
    """
    Precision.

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Ground truth (true relevance labels).
    y_pred : array-like, shape = [n_samples]
        Predicted elements.
    average (str): This parameter is required for multiclass/multilabel targets.

    Returns
    -------
    precision: float

    """
    precision = precision_score(y_true, y_pred, average=average)
    return precision


def recall(y_true, y_pred, average=None):
    """
    Recall.

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Ground truth (true relevance labels).
    y_pred : array-like, shape = [n_samples]
        Predicted elements.
    average (str): This parameter is required for multiclass/multilabel targets.

    Returns
    -------
    recall: float

    """
    recall = recall_score(y_true, y_pred, average=average)
    return recall


def f1(y_true, y_pred, average=None):
    """
    f1.

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Ground truth (true relevance labels).
    y_pred : array-like, shape = [n_samples]
        Predicted elements.
    average (str): This parameter is required for multiclass/multilabel targets.

    Returns
    -------
    recall: float

    """
    f1 = f1_score(y_true, y_pred, average=average)
    return f1


def matthews(y_true, y_pred):
    """
    Matthews correlation coefficient.

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Ground truth (true relevance labels).
    y_pred : array-like, shape = [n_samples]
        Predicted elements.

    Returns
    -------
    recall: float

    """
    matthews_c = matthews_corrcoef(y_true, y_pred)
    return matthews_c
