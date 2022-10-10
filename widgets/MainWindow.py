import json
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .AdminWindow import AdminWindow
from .UI.MainWindowUi import MainWindowUi
from utils import Strings, Settings
from .util import get_font, centralizate, window_centralizate, show_info, show_warn, show_error, get_question_word


class MainWindow(QWidget, MainWindowUi):
    def __init__(self, debug=False, *args):
        super(MainWindow, self).__init__()

        self.args = args
        self.debug = debug
        logging.info(f'App started in {debug=}')

        self.initUi()

        self.settings = Settings.DEFAULT_TEST_SETTINGS
        self.update_settings()
        self.questions = []
        self.session = []
        self.cleaned_data = {}
        self.complete_count = 0

        self.current_question = {}
        self.current_answers = []

    def initUi(self):
        self.setFixedSize(MainWindowUi.Meta.WINDOW_WIDTH, MainWindowUi.Meta.WINDOW_HEIGHT)
        window_centralizate(self)
        self.setWindowTitle(Strings.main_window_title)

        self.connect_buttons()

        self.show_admin()

    def connect_buttons(self):
        self.start_test_btn.clicked.connect(self.admin_start_test)
        self.load_test_btn.clicked.connect(self.show_admin)

    def show_admin(self):
        logging.info('Launching AdminWindow')
        self.questions, self.settings = AdminWindow(self).exec_()
        if self.questions:
            self.update_settings()

    def update_settings(self):
        texts = {
            False: 'Нет',
            True: 'Да'
        }
        self.is_exel_label.setText(f'{Strings.MainUi.is_exel_label} {texts[self.settings["exel_export"]]}')
        self.is_show_count_label.setText(f'{Strings.MainUi.is_show_count_label} {texts[self.settings["show_users"]]}')
        self.is_use_password_label.setText(f'{Strings.MainUi.is_use_password_label} '
                                           f'{texts[self.settings["use_password"]]}')

        self.set_count_hidden(not self.settings['show_users'])

    def admin_start_test(self):
        if len(self.questions) > 0 or self.debug:
            self.hide_prepare_items()
            self.prepare_new_test(self.format_welcome_text())
        else:
            show_error(self, text=Strings.MainUi.questions_not_load_error)

    def format_welcome_text(self) -> str:
        welcome_text_formatted = self.settings['welcome_text']
        welcome_text_formatted = welcome_text_formatted.replace('%q_count%', str(len(self.questions)))
        welcome_text_formatted = welcome_text_formatted.replace('%q_word%', get_question_word(len(self.questions)))
        return welcome_text_formatted

    def clean_session(self):
        new_data = {'answers': [], 'answers_raw': self.session}
        self.cleaned_data = new_data

    def closeEvent(self, a0) -> None:
        super(MainWindow, self).closeEvent(a0)
        self.clean_session()


