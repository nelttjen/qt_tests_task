from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .UI import MainWindowUI
from .util import window_centralizate, show_info, show_warn, show_error


class MainWindow(QWidget, MainWindowUI):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.generated = []
        self.cleaned_data = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Test creator')
        window_centralizate(self)
        self.setWindowFlag()

    def clean_data(self):
        self.cleaned_data = self.generated

    def closeEvent(self, a0) -> None:
        super(MainWindow, self).closeEvent(a0)
        self.clean_data()
