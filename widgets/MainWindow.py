import json
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .AdminWindow import AdminWindow
from .UI.MainWindowUi import MainWindowUi
from utils import Strings, Settings
from .util import get_font, centralizate, window_centralizate


class MainWindow(QWidget, MainWindowUi):
    def __init__(self, debug=False, *args):
        super(MainWindow, self).__init__()

        self.args = args
        self.debug = debug
        logging.info(f'App started in {debug=}')

        self.initUi()

        self.settings = Settings.DEFAULT_TEST_SETTINGS
        self.questions = None
        self.session = []
        self.complete_count = 0

    def show_admin(self):
        logging.info('Launching AdminWindow')
        self.questions, self.settings = AdminWindow(self).exec_()
        self.update_settings()

    def update_settings(self):
        pass

    def initUi(self):
        self.setFixedSize(MainWindowUi.Meta.WINDOW_WIDTH, MainWindowUi.Meta.WINDOW_HEIGHT)
        window_centralizate(self)
        self.setWindowTitle(Strings.main_window_title)

        self.show_admin()

    def closeEvent(self, a0) -> None:
        super(MainWindow, self).closeEvent(a0)