import screeninfo

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox

monitor = screeninfo.get_monitors()[0]
user_res_w, user_res_h = monitor.width, monitor.height

centralizate = lambda win_w, obj_w: int(win_w // 2 - obj_w // 2)
window_centralizate = lambda win: win.move(centralizate(user_res_w, win.width()),
                                           centralizate(user_res_h, win.height()))


def get_font(size: int = 8):
    font = QFont()
    font.setPointSize(size)
    return font


def show_info(parrent, caption='Info', text=''):
    QMessageBox.information(parrent, caption, text, QMessageBox.Ok)


def show_warn(parrent, caption='Warning', text=''):
    QMessageBox.warning(parrent, caption, text, QMessageBox.Ok)


def show_error(parrent, caption='Error', text=''):
    QMessageBox.critical(parrent, caption, text, QMessageBox.Ok)
