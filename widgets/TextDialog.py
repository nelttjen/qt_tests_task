from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from utils import Strings
from .util import window_centralizate
from .UI import TextDialogUi


class TextDialog(QDialog, TextDialogUi):
    def __init__(self, parent=None, text=''):
        super(TextDialog, self).__init__(parent, Qt.WindowCloseButtonHint)

        self.initUi(text)
        self.connect_buttons()

        self.is_accepted = False

    def connect_buttons(self):
        self.accept_button.clicked.connect(self.accept)
        self.reject_button.clicked.connect(self.reject)

    def initUi(self, text: str):
        self.setWindowTitle(Strings.text_dialog_title)
        self.setFixedSize(TextDialogUi.Meta.WINDOW_WIDTH, TextDialogUi.Meta.WINDOW_HEIGHT)
        window_centralizate(self)

        self.text_area.setText(text)

    def accept(self) -> None:
        super(TextDialog, self).accept()
        self.is_accepted = True

    def exec_(self) -> str:
        super(TextDialog, self).exec_()
        return self.text_area.toPlainText()
