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
    return app.exec_()


def on_destroy():
    pass


if __name__ == '__main__':
    on_launch()
    exit_code = launch_app()
    on_destroy()
    sys.exit(exit_code)
