import json
import logging
import copy

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QButtonGroup, QCheckBox, QRadioButton

from .AdminWindow import AdminWindow
from .AgreementDialog import AgreementDialog
from .PasswordDialog import PasswordDialog
from .UI.MainWindowUi import MainWindowUi
from utils import Strings, Settings
from .util import get_font, centralizate, window_centralizate, show_info, show_warn, show_error, get_question_word


class MainWindow(QWidget, MainWindowUi):
    def __init__(self, debug=False, *args):
        super(MainWindow, self).__init__()

        self.args = args
        self.debug = debug
        logging.info(f'App started in {debug=}')

        self.settings = copy.deepcopy(Settings.DEFAULT_TEST_SETTINGS)
        self.update_settings()

        self.questions = []
        self.session = []
        self.cleaned_data = {}
        self.complete_count = 0

        self.current_question = {}
        self.current_question_index = 0
        self.current_answers = []

        self.button_group = []

        self.initUi()

    def initUi(self):
        self.setFixedSize(MainWindowUi.Meta.WINDOW_WIDTH, MainWindowUi.Meta.WINDOW_HEIGHT)
        window_centralizate(self)
        self.setWindowTitle(Strings.main_window_title)

        self.connect_buttons()

        self.show_admin()

    def connect_buttons(self):
        self.start_test_btn.clicked.connect(self.admin_start_test)
        self.load_test_btn.clicked.connect(self.show_admin)
        self.admin_end_test_button.clicked.connect(self.end_test)

        self.start_test_user_btn.clicked.connect(self.start_test)
        self.action_button.clicked.connect(self.next_question)

    def show_admin(self):
        logging.info('Launching AdminWindow')
        window = AdminWindow(parent=self, current_text=self.settings['welcome_text'])
        val1, val2 = copy.deepcopy(window.exec_())
        if window.is_accepted:
            logging.info(f'AdminWindow accepted, returning '
                         f'{len(val1)} questions')
            self.questions, self.settings = copy.deepcopy(val1), copy.deepcopy(val2)
            self.update_settings()
        else:
            logging.info('AdminWindow was closed, no changes to commit')

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
        logging.info(f'Starting test with {len(self.questions)} questions')
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

    def start_test(self):
        self.confirm_new_test()
        self.next_question()

    def next_question(self):
        if self.current_question:
            user_answer = {
                'question_id': self.current_question['id'],
                'question_text': self.current_question['text'],
                'question_answers': [i.text() for i in self.button_group if i.isChecked()]
            }
            if len(user_answer['question_answers']) == 0:
                show_warn(self, text=Strings.MainUi.answer_not_selected)
                return
            self.current_answers.append(user_answer)

        self.clear_previous_buttons()

        if self.current_question_index == len(self.questions):
            self.save_test()
            return

        new_question = self.questions[self.current_question_index]
        self.set_new_question(new_question)
        self.current_question_index += 1
        self.current_question = new_question
        button_text = Strings.MainUi.last_question_btn if self.current_question_index == len(self.questions) \
            else Strings.MainUi.next_question_btn
        self.action_button.setText(button_text)

    def clear_previous_buttons(self):
        for button in self.button_group:
            button.deleteLater()
        self.button_group = []

    def set_new_question(self, q_object):
        q_id = q_object['id']
        text = q_object['text']
        answer_list = q_object['answers']
        is_multiple = q_object['is_multiple']
        button_type = QRadioButton if not is_multiple else QCheckBox

        box_w, box_h = 250, 45
        box_x, box_y = self.Meta.CHECKBOX_WIDTH_START, self.Meta.CHECKBOX_HEIGHT_START

        for i, cell in enumerate(answer_list):
            new_button = button_type(self)
            new_button.setFont(get_font(12))
            new_button.setText(cell)
            new_button.setGeometry(box_x, box_y + box_h * i, box_w, box_h)
            new_button.setHidden(False)
            self.button_group.append(new_button)

        # self.button_group

        hint_text = Strings.MainUi.multiple_question_hint if is_multiple else Strings.MainUi.single_question_hint

        self.current_question_label.setText(f'{q_id}. {text} {hint_text}')

    def save_test(self):
        self.current_question_index = 0
        self.current_question = {}
        self.session.append(copy.deepcopy(self.current_answers))
        self.current_answers = []

        self.complete_count += 1
        self.set_count_value(self.complete_count)

        self.hide_test_items()
        self.prepare_new_test(self.format_welcome_text())

        logging.info(f'Answers have been saved, current completes: {self.complete_count}')

    def end_test(self):
        logging.info('Close MainWindow triggered')
        if self.settings['use_password']:
            window = PasswordDialog(self)
            result = window.exec_()
            password = window.password_input.text()
            if not result:
                return
            if password == self.settings['password']:
                logging.info('Password is correct.')
                self.close_on_agree()
            else:
                logging.warning('Password is incorrect')
                show_error(self, text='Неправильный пароль')

        else:
            self.close_on_agree()

    def close_on_agree(self):
        agreement = AgreementDialog(self, Strings.MainUi.agreement_no_pass).exec()
        if not agreement:
            logging.info('Close was rejected')
            return
        logging.info('Closing MainWindow')
        self.close()
        self.destroy()

    def clean_session(self):
        new_data = {'answers': [], 'answers_raw': self.session}
        self.cleaned_data = new_data

    def closeEvent(self, a0) -> None:
        super(MainWindow, self).closeEvent(a0)
        self.clean_session()


