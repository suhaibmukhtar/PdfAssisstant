import logging
from config import config

LOG_FILE_PATH = config.LOGGING_FILE_PATH


logging.basicConfig(
    format="[ %(asctime)s ] - %(filename)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    logging.info("Logging has started")
