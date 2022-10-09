import json
import logging
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog

from utils import Strings
from .util import window_centralizate, show_info, show_warn, show_error
from .UI import AdminWindowUi


class AdminWindow(QDialog, AdminWindowUi):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint)

        self.questions = []
        self.options = {
            'password': '',
            'use_password': False,
            'exel_export': False,
            'show_users': False
        }
        self.initUi()

    def initUi(self):
        self.setFixedSize(AdminWindowUi.Meta.WINDOW_WIDTH,
                          AdminWindowUi.Meta.WINDOW_HEIGHT)
        window_centralizate(self)
        self.setWindowTitle(Strings.admin_window_title)

        self.connect_actions()

    def connect_actions(self):
        self.test_file_choose_btn.clicked.connect(self.choose_file_btn)
        self.test_file_confirm_btn.clicked.connect(self.confirm_file_btn)

    def choose_file_btn(self):
        file = QFileDialog.getOpenFileName(parent=self, caption=Strings.AdminUi.file_choose_dialog_caption,
                                           directory='./', filter='JSON (*.json);;All files (*.*)')[0]
        f_path = Path(file)
        if not f_path.is_file():
            return
        try:
            with open(file, 'r', encoding='utf-8') as f_input:
                data = json.load(f_input)
        except PermissionError:
            show_error(self, text=Strings.AdminUi.file_permission_error)
            return
        except (json.JSONDecodeError, UnicodeDecodeError):
            show_error(self, text=Strings.AdminUi.file_read_error)
            return
        if not isinstance(data, list) or len(data) == 0:
            show_warn(self, text=Strings.AdminUi.file_empty_warn)
            self.set_question_count(0)
            return
        checked_questions = []
        for item in data:
            # Проверка что есть все ключи и эти ключи правильных типов данных
            if all([i in item.keys() for i in ['id', 'text', 'answers', 'is_multiple']]) and \
                all([isinstance(item['id'], int), isinstance(item['text'], str),
                     isinstance(item['answers'], list), isinstance(item['is_multiple'], bool)]):

                checked_questions.append(item)
        if len(checked_questions) == 0:
            show_warn(self, text=Strings.AdminUi.file_empty_warn)
        self.set_question_count(len(checked_questions))
        self.questions = checked_questions
        logging.info(f'File selected, found questions: {len(self.questions)}')

    def confirm_file_btn(self):
        if self.password_input_checkbox.isChecked() and len(self.password_input.text()) < 3:
            show_error(self, text=Strings.AdminUi.no_password_error)
            return
        self.options['password'] = self.password_input.text()
        self.options['use_password'] = self.password_input_checkbox.isChecked()
        self.options['exel_export'] = self.exel_export_checkbox.isChecked()
        self.options['show_users'] = self.show_complete_info_checkbox.isChecked()
        self.accept()

    def set_question_count(self, number: int):
        self.test_file_info_label.setText(f'{Strings.AdminUi.test_file_info_label} {number}')
        self.test_file_info_label.setAlignment(Qt.AlignCenter)

    def exec_(self) -> tuple:
        super(AdminWindow, self).exec_()
        logging.info(f'AdminWindow accepted, returning '
                     f'{len(self.questions)} questions')
        return self.questions, self.options
