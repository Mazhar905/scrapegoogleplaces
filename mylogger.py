# logger.py

import logging
import os
import datetime


class MyLogger:
    def __init__(self):
        # create logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create file handler and set level to debug
        current_time = datetime.datetime.now().strftime("%y%m%d")
        log_filename = f"log_{current_time}.log"
        fh = logging.FileHandler(log_filename)
        fh.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter(
            '%(asctime)s-%(levelname)s-%(name)s-%(filename)s:%(lineno)d-%(message)s')

        # add formatter to ch and fh
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add ch and fh to logger
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
