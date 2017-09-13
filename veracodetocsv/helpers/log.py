# Purpose:  Log utilities

import logging
from datetime import datetime


now = datetime.now().strftime("%Y-%m-%d-%H%M%S")
logging_filename = now + ".log"
format_string = "%(asctime)s %(levelname)s %(message)s"

logging.captureWarnings(True)


def setup_logging(debug=False):
    if debug:
        logging.basicConfig(format=format_string, filename=logging_filename, level=logging.DEBUG)
    else:
        logging.basicConfig(format=format_string, filename=logging_filename, level=logging.INFO)
        requests_logger = logging.getLogger("requests")
        requests_logger.setLevel(logging.WARNING)
