import logging
import os


def folder_init():
    os.mkdir('temp') if not os.path.exists('temp') else None
    os.mkdir('results') if not os.path.exists('results') else None


def init_logger():
    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger()
    logger_handler = logging.StreamHandler()
    logger.removeHandler(logger.handlers[0])
    logger.addHandler(logger_handler)

    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s: %(message)s")
    logger_handler.setFormatter(formatter)