import datetime
import json
import sys

from PyQt5.QtWidgets import QApplication

from util import init_logger, folder_init
from widgets import MainWindow


def on_launch():
    folder_init()
    init_logger()


def launch_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_(), window.cleaned_data


def on_destroy(save_data):
    if save_data:
        str_date = datetime.datetime.now().strftime('%d.%m.%Y_(%H:%M:%S)')
        file_name = f'output/questions_{str_date}.json'
        with open(file_name, 'w', encoding='utf=8') as out:
            json.dump(save_data, out, ensure_ascii=False)


if __name__ == '__main__':
    on_launch()
    exit_code, data = launch_app()
    on_destroy(data)
    sys.exit(exit_code)
