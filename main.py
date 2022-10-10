import datetime
import json
import logging
import shutil
import sys

from art import tprint
from PyQt5.QtWidgets import QApplication

from widgets import MainWindow
from utils import folder_init, init_logger, Settings, Strings


def on_launch():
    """Создание папок и логгера на старте"""

    tprint(Strings.main_window_title)
    folder_init()
    init_logger()


def launch_app(debug=False):
    """Запуск и удержание приложения, возврат ответов с приложения и кода завершения"""

    app = QApplication(sys.argv)
    logging.info('Starting app...')
    wind = MainWindow(debug=debug)
    wind.show()
    return app.exec_(), wind.cleaned_data


def on_destroy():
    """Удалить временные файлы и сохранить результаты"""

    logging.info('Deleting temp...')
    try:
        shutil.rmtree('temp')
    except:
        logging.error('Error while deleting temp folder')
    date_format = datetime.datetime.now().strftime('%d.%m.%Y (%H:%M)')
    if not Settings.DEBUG:
        logging.info('Saving answers...')
        with open(f'results/results {date_format}.json', 'w', encoding='utf-8') as f:
            json.dump(answers, f)
        logging.info('Answers saved')


if __name__ == '__main__':
    on_launch()
    logging.info("Initialization done.")
    exit_code, answers = launch_app(debug=Settings.DEBUG)
    on_destroy()
    logging.info('Exiting app... Bye-bye!')
    sys.exit(exit_code)