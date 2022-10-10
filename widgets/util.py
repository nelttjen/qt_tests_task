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


def get_question_word(count: int) -> str:
    v1 = 'вопрос'
    v2 = 'вопроса'
    v3 = 'вопросов'
    if count % 100 in [11, 12, 13, 14]:
        return v3
    if count % 10 == 1:
        return v1
    if count % 10 in [2, 3, 4]:
        return v2
    return v3
