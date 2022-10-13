import logging
import os


def folder_init():
    os.mkdir('output') if not os.path.exists('output') else None


def init_logger():
    """Инициализация логера в красивом формате вывода"""
    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger()
    logger_handler = logging.StreamHandler()
    logger.removeHandler(logger.handlers[0])
    logger.addHandler(logger_handler)

    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s: %(message)s")
    logger_handler.setFormatter(formatter)