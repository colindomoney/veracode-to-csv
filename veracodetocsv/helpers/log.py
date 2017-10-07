# Purpose:  Log utilities

import logging
import time
from datetime import datetime


now = datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
logging_filename = now + ".log"
format_string = "%(asctime)s %(levelname)s %(message)s"
datetime_format = '%Y-%m-%d %H:%M:%S'

logging.captureWarnings(True)


def setup_logging(debug=False):
    logging.Formatter.converter = time.gmtime
    if debug:
        logging.basicConfig(format=format_string, datefmt=datetime_format, filename=logging_filename, level=logging.DEBUG)
    else:
        logging.basicConfig(format=format_string, datefmt=datetime_format, filename=logging_filename, level=logging.INFO)
        requests_logger = logging.getLogger("requests")
        requests_logger.setLevel(logging.WARNING)
