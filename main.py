import sys

from PyQt5.QtWidgets import QApplication

from widgets import MainWindow

def launch_app():
    app = QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    return app.exec_()


if __name__ == '__main__':
    exit_code = launch_app()
    sys.exit(exit_code)