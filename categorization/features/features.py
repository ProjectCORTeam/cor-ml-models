"""Features declaration."""
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion
from textacy import preprocessing

STOPWORDS_SET = set(stopwords.words("spanish") + stopwords.words("english"))


def remove_stopwords(text):
    """Remove stop words from list of tokenized words."""
    new_words = [word for word in text.split() if word not in STOPWORDS_SET]
    return " ".join(new_words)


def preprocess_text(
    text,
    stopwords=True,
    no_html=True,
    no_unicode=True,
    no_bullets=True,
    no_urls=True,
    no_emails=True,
    no_phones=True,
    no_numbers=True,
    no_currency_symbols=True,
    no_punct=True,
    no_accents=True,
    no_emojis=True,
):
    argsList = []

    if no_html:
        argsList.append(preprocessing.remove.html_tags)
    if no_bullets:
        argsList.append(preprocessing.normalize.bullet_points)
    if no_unicode:
        argsList.append(preprocessing.normalize.unicode)
    if no_urls:
        argsList.append(preprocessing.replace.urls)
    if no_emails:
        argsList.append(preprocessing.replace.emails)
    if no_phones:
        argsList.append(preprocessing.replace.phone_numbers)
    if no_numbers:
        argsList.append(preprocessing.replace.numbers)
    if no_currency_symbols:
        argsList.append(preprocessing.replace.currency_symbols)
    if no_punct:
        argsList.append(preprocessing.remove.punctuation)
    if no_accents:
        argsList.append(preprocessing.remove.accents)
    if no_emojis:
        argsList.append(preprocessing.replace.emojis)

    args = tuple(argsList)

    preproc = preprocessing.make_pipeline(*args)

    clean_text = preproc(text)

    if stopwords:
        clean_text = remove_stopwords(clean_text)

    return clean_text


PREPROCESS_VECTORIZED = np.vectorize(preprocess_text)


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
        stopwords=True,
        no_html=True,
        no_unicode=True,
        no_bullets=True,
        no_urls=True,
        no_emails=True,
        no_phones=True,
        no_numbers=True,
        no_currency_symbols=True,
        no_punct=True,
        no_accents=True,
        no_emojis=True,
    ):
        """Init method.

        Args:
            column (column): dict key. It's used to get
            specific value in a dict array.
        """
        super(TextTransformer, self).__init__()

        self.stopwords = (stopwords,)
        self.no_html = (True,)
        self.no_unicode = (True,)
        self.no_bullets = (True,)
        self.no_urls = (True,)
        self.no_emails = (True,)
        self.no_phones = (True,)
        self.no_numbers = (True,)
        self.no_currency_symbols = (True,)
        self.no_punct = (True,)
        self.no_accents = (True,)
        self.no_emojis = True

    def fit(self, X, y=None):
        """Fit method."""
        return self

    def transform(self, X):
        """Transform input X.

        Args:
            X: array of dictionaries.
        """
        transformed_list = [_imputer(x) for x in X]

        vectorized_list = PREPROCESS_VECTORIZED(
            transformed_list,
            stopwords=self.stopwords,
            no_html=self.no_html,
            no_unicode=self.no_unicode,
            no_bullets=self.no_bullets,
            no_urls=self.no_urls,
            no_emails=self.no_emails,
            no_phones=self.no_phones,
            no_numbers=self.no_numbers,
            no_currency_symbols=self.no_currency_symbols,
            no_punct=self.no_punct,
            no_accents=self.no_accents,
            no_emojis=self.no_emojis,
        )

        Z = np.array(vectorized_list)

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
