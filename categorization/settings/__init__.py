from datetime import datetime
from pathlib import Path

# base
BASE_PATH = Path(__file__).resolve().parent  # Root of the package


# logger
LOG_FILENAME = f"categorization_{datetime.now().strftime('%Y_%m_%d_%H_%M')}.log"
LOCAL_LOG_DIR = Path(BASE_PATH) / "log"
LOCAL_LOG_PATH = Path(LOCAL_LOG_DIR) / LOG_FILENAME
