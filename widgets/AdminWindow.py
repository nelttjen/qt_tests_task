from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel

from utils import Strings


class AdminWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint)

        self.answers = None
        self.initUi()

    def initUi(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle(Strings.admin_window_title)

        self.test_file_choose_btn = QPushButton(self)
        self.test_file_choose_btn.setText(Strings.AdminUi.test_file_choose_btn)
        self.test_file_choose_btn.setGeometry(400, 400, 200, 100)

    def exec_(self) -> list:
        super(AdminWindow, self).exec_()
        return self.answers
