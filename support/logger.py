"""File-backed logger factory used by features and step files when
they want a persistent trail in logs/test_automation.log. The existing
BasePage self.log keeps writing to stderr the way it has; this one
is additive and idempotent — calling get_logger twice with the same
name doesn't stack handlers."""

import logging
import os


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "test_automation.log")


def get_logger(name):
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = logging.FileHandler(LOG_FILE)
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )
        )
        logger.addHandler(handler)
    return logger
