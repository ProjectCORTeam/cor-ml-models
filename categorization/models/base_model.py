"""Definition of base embedding model."""


class BaseModel:
    """Base model."""

    def __init__(self):
        """Init method."""

    def fit(self):
        """Fit model."""
        raise NotImplementedError

    def predict(self):
        """Predict using a trained model."""
        raise NotImplementedError

    def test(self):
        """Evaluate supervised model using file given by path."""
        return NotImplementedError
