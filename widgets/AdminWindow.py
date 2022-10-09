import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from utils import Strings
from .util import window_centralizate
from .UI import AdminWindowUi


class AdminWindow(QDialog, AdminWindowUi):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint)

        self.answers = None
        self.initUi()

    def initUi(self):
        self.setFixedSize(AdminWindowUi.Meta.WINDOW_WIDTH,
                          AdminWindowUi.Meta.WINDOW_HEIGHT)
        window_centralizate(self)
        self.setWindowTitle(Strings.admin_window_title)

    def exec_(self) -> list:
        super(AdminWindow, self).exec_()
        logging.info(f'AdminWindow accepted, returning '
                     f'{len(self.answers) if isinstance(self.answers, list) else 0} questions')
        return self.answers or []
