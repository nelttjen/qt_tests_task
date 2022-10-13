
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialogButtonBox, QLabel, QLineEdit


class AgreementDialogUi:
    def __init__(self):
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(30, 60, 161, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 0, 221, 61))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")


class PasswordDialogUi(AgreementDialogUi):
    def __init__(self):
        super().__init__()
        self.label.setGeometry(0, 0, 221, 31)

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(20, 30, 221 - 40, 30)
        font = QFont()
        font.setPointSize(12)
        self.password_input.setFont(font)
        self.password_input.setPlaceholderText('Введите пароль')