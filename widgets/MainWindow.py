import json
import logging

from PyQt5.QtWidgets import QWidget

from .AdminWindow import AdminWindow
from utils import Strings


class MainWindow(QWidget):
    def __init__(self, debug=False, *args):
        super(MainWindow, self).__init__()

        self.args = args
        self.debug = debug
        logging.info(f'App started in {debug=}')

        self.initUi()

        self.questions = None
        self.answers = []

    def show_admin(self):
        result = AdminWindow(self).exec_()
        return result

    def initUi(self):
        self.setFixedSize(1000, 720)
        self.setWindowTitle(Strings.main_window_title)

        self.questions = self.show_admin()