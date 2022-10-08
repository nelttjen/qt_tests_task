from PyQt5.QtWidgets import QMainWindow

from utils import Settings

class MainWindow(QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__()

        self.args = args

        self.initUi()

    def initUi(self):
        self.setFixedSize(1000, 720)
        self.setWindowTitle(Settings.window_title)
