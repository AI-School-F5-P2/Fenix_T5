import logging
from logging.handlers import TimedRotatingFileHandler
import datetime


def setup_logger(log_file):

    logger = logging.getLogger("fenix_logger")

    logger.setLevel(logging.DEBUG)
    if not logger.hasHandlers():
        formatter = logging.Formatter('%(asctime)s - %(levelname)s  %(filename)s %(funcName)s %(lineno)s - %(message)s',
                                      datefmt='%d-%m-%Y %H:%M:%S')

        current_date = datetime.datetime.now()
        month = current_date.strftime('%m')
        year = current_date.strftime('%Y')

        fileHandler = logging.FileHandler(filename='fenix.log')
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(level=logging.INFO)

        logger.addHandler(fileHandler)

    return logger
