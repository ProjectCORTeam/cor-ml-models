"""Features declaration."""
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion

STOPWORDS_SET = set(stopwords.words("spanish") + stopwords.words("english"))

def remove_stopwords(text):
    """Remove stop words from list of tokenized words."""
    new_words = [word for word in text.split() if word not in STOPWORDS_SET]
    return " ".join(new_words)


def preprocess_text(
    text,
    stopwords=True

):

    clean_text = text.lower()

    if stopwords:
        clean_text = remove_stopwords(clean_text)

    return clean_text


def _imputer(text):
    """Text imputer."""
    if text is None or pd.isna(text):
        return ""
    else:
        return text


class TextTransformer(BaseEstimator, TransformerMixin):
    """Text Transformer.

    Perform text preprocessing each text in a list.
    """

    def __init__(
        self,
        stopwords=True
    ):
        """Init method.

        Args:
            column (column): dict key. It's used to get
            specific value in a dict array.
        """
        super(TextTransformer, self).__init__()

        self.stopwords = stopwords


    def fit(self, X, y=None):
        """Fit method."""
        return self

    def transform(self, X):
        """Transform input X.

        Args:
            X: array of dictionaries.
        """
        transformed_list = [preprocess_text(_imputer(x), self.stopwords) for x in X]

        Z = np.array(transformed_list)

        return list(Z)


features_by_name = {"TEXT_TRANSFORMER": lambda: TextTransformer()}


def get_features(features):
    """Get features by name."""
    names = [f for f in features if isinstance(f, str)]
    # validate that names exists
    if any(n not in features_by_name for n in names):
        raise KeyError(
            "Valid features are: {}".format(", ".join(sorted(features_by_name.keys())))
        )
    # if no features were given, all features by name are included
    if not features:
        names = features_by_name.keys()

    named_features = [(name, features_by_name[name]()) for name in names]
    # make a big union
    return FeatureUnion(transformer_list=named_features)
