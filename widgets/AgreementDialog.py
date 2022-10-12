# Forked from https://github.com/nelttjen/PyQT_project/blob/main/Dialog/AgreementDialog.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from widgets.UI.AgreementDialogUi import AgreementDialogUi


class AgreementDialog(QDialog, AgreementDialogUi):
    def __init__(self, parrent=None, text=''):
        super().__init__(parrent, Qt.WindowCloseButtonHint)

        self.setWindowTitle('Подтверждение')

        self.label.setText(text)
        self.label.move(20, 13)
        self.label.resize(self.label.sizeHint())
        self.setFixedSize(self.label.sizeHint().width() + 40, 101)
        self.buttonBox.move((self.size().width() - self.buttonBox.size().width()) // 2, 61)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
