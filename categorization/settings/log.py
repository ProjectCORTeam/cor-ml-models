import logging
import os
import time
from functools import wraps
from logging.config import dictConfig
from typing import Any

from categorization.settings.constants import LOCAL_LOG_DIR, LOCAL_LOG_PATH

if not os.path.exists(LOCAL_LOG_DIR):
    os.makedirs(LOCAL_LOG_DIR)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,  # disable third party libraries
    "formatters": {
        "standard": {
            "format": "🌎 - %(levelname)s %(processName)s(pid=%(process)d) - "
            "%(module)s - %(message)s"
        },
        "verbose": {
            "format": "🔴 - %(levelname)s %(processName)s(pid=%(process)d) - "
            "%(module)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "level": "INFO",
        },
        "log_file": {
            "formatter": "verbose",
            "filename": LOCAL_LOG_PATH,
            "mode": "w",
            "class": "logging.FileHandler",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "entities_matching": {
            "handlers": ["console", "log_file"],
            "level": "INFO",
            "propagate": False,
        }
    },
}

dictConfig(LOGGING)
logger = logging.getLogger("Categorization")


def timed(func: Any) -> Any:
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(self, *args, **kwargs)
        end = time.time()
        logger.info(f"{self.__class__.__name__} ran in {round(end - start, 4)}s")
        return result

    return wrapper
