"""Scikit-learn models."""
import os
import pickle

from sklearn.base import BaseEstimator
from sklearn.dummy import DummyClassifier
from sklearn.exceptions import NotFittedError
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC, LinearSVC

from categorization.features.features import TextTransformer
from categorization.utils import json_dump_unicode

TEXT_PREPROCESS_PARAMS = {
    "stopwords": False,
    "no_html": True,
    "no_unicode": True,
    "no_bullets": True,
    "no_urls": True,
    "no_emails": True,
    "no_phones": True,
    "no_numbers": True,
    "no_currency_symbols": True,
    "no_punct": True,
    "no_accents": True,
    "no_emojis": True,
}

VECTORIZER_PARAMS = {
    "ngram_range": (1, 2),
    "max_df": 1.0,
    "min_df": 1,
    "lowercase": True,
}

LOGISTIC = "logistic"
SVC_MODEL = "svc"
LINEAR_SVC = "linearSvc"
DUMMY_CLASSIFIER = "DUMMY_CLASSIFIER"

# LOGISTIC_PARAMS = {'C': 1000,
#                    'penalty': 'l2'}
# DUMMY_CLASSIFIER = 'dummy_classifier'
# SVM_CLASSIFIER = 'svc_classifier'
# SVM_CLASSIFIER_PARAMS = {'C': 10,
#                         'probability': True}

PARAMS_BY_NAME = {
    LOGISTIC: {"C": 1000, "penalty": "l2"},
    DUMMY_CLASSIFIER: {},
    SVC: {"C": 10, "probability": True},
    LINEAR_SVC: {"max_iter": 10000},
}

MODELS_BY_NAME = {
    LOGISTIC: lambda: LogisticRegression(),
    DUMMY_CLASSIFIER: lambda: DummyClassifier(),
    SVC_MODEL: lambda: SVC(),
    LINEAR_SVC: lambda: LinearSVC(),
}


class Categorizer(BaseEstimator):
    """Sklearn classifier model abstraction to predict categories."""

    def __init__(
        self,
        vectorizer_params=VECTORIZER_PARAMS,
        model_name=LOGISTIC,
        preprocess_params=TEXT_PREPROCESS_PARAMS,
        last_train_ts=0,
        model_path=None,
    ):
        """Init method.


        Keyword Arguments:
            vectorizer_params {dict} -- CountVectorizer params
            (default:
                {'ngram_range': (1, 2),
                'max_df':  1.0,
                'min_df': 1,
                })
            model_name {str} -- Model to use (default: {'logistic'})
            model_params {dict} -- Model params (default: {{'C': 1000, 'penalty': 'l2'}})
            last_train_ts {int} -- timestamp of last training (default: {0})
            model_path {str} -- pathname where the model is stored (default: {None})

        Raises:
            ValueError: Invalid model.

        """
        super().__init__()

        if model_name in MODELS_BY_NAME.keys():
            self.model_name = model_name
        else:
            msg = "Invalid model. Please choose from {}".format(MODELS_BY_NAME.keys())
            raise ValueError(msg)

        self.preprocess_params = preprocess_params
        self.vectorizer_params = vectorizer_params
        self.model_params = PARAMS_BY_NAME[self.model_name]
        self.model_path = "" if model_path is None else model_path
        self.last_train_ts = last_train_ts
        self.model = None

    def get_pipeline(self):
        """Retrieve sklearn pipeline."""

        pipeline = Pipeline(
            [
                # text_preprocess
                ("normalize", TextTransformer()),
                # vectorizer
                ("feats", TfidfVectorizer()),
                # Classifier
                ("class", MODELS_BY_NAME[self.model_name]()),
            ]
        )

        params = {"feats__" + k: val for k, val in self.vectorizer_params.items()}
        params.update({"class__" + k: val for k, val in self.model_params.items()})
        params.update(
            {"normalize__" + k: val for k, val in self.preprocess_params.items()}
        )
        pipeline.set_params(**params)
        self.model = pipeline

    def fit(self, X, y):
        """Fit the model.

        Arguments:
            X {list} -- list of texts
            y {list} -- list of labels
        """
        self.get_pipeline()
        self.model.fit(X, y)

    def predict(self, feat):
        """Predict samples.

        Arguments:
            feat {list} -- List of texts

        Raises:
            NotFittedError: Model is not fitted.

        Returns:
            list -- list of predictions

        """
        preds = []
        if self.model:
            preds = self.model.predict(feat)
        else:
            raise NotFittedError("Model is not fitted or loaded yet ")
        return preds

    def predict_proba(self, feat):
        """Predict samples.

        Arguments:
            feat {list} -- List of texts

        Raises:
            NotFittedError: Model is not fitted.

        Returns:
            tuple -- tuple with (predictions, probabilities)

        """
        preds = []
        proba = []
        if self.model:
            preds = self.model.predict(feat)
            proba = self.model.predict_proba(feat)
            proba = [max(p) for p in proba]
        else:
            raise NotFittedError("Model is not fitted or loaded yet ")
        return preds, proba

    def get_metadata(self):
        """Get model metadata."""
        return {
            "class_name": self.__class__.__name__,
            "module_name": self.__module__,
            "model_path": self.model_path,
            "vectorizer_params": self.vectorizer_params,
            "classifier_name": self.model_name,
            "classifier_params": self.model_params,
            "timestamp": self.last_train_ts,
        }

    def get_metadata_path(self, context_dir):
        """Get path of model metadata."""
        meta_name = "sk_model_metadata_ts_{}.json".format(self.last_train_ts)
        metadata_path = os.path.join(context_dir, meta_name)

        return metadata_path

    def dump_metadata(self, output_path):
        """Dump model metadata."""
        metadata = self.get_metadata()
        json_dump_unicode(metadata, output_path)

    def save_model(self, path: str) -> None:
        with open(path, "wb") as f:
            pickle.dump(self, f, protocol=4)

    @classmethod
    def load_model(cls, path: str) -> "Categorizer":
        with open(path, "rb") as f:
            model = pickle.load(f)  # nosec
        if model.__class__ != cls:
            raise Exception(
                f"Object loaded is instance of {model.__class__}."
                f" Expected instance of {cls}"
            )
        return model
