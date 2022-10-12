from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QButtonGroup
from widgets.util import centralizate, get_font
from utils.Strings import Strings


class MainWindowUi:
    class Meta:
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 720

        CHECKBOX_WIDTH_START = 75
        CHECKBOX_HEIGHT_START = 200

    def __init__(self):
        self.current_question_label = QLabel(self)
        self.current_question_label.setFont(get_font(15))
        self.current_question_label.setWordWrap(True)
        self.current_question_label.setAlignment(Qt.AlignCenter)
        self.current_question_label.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 950), 25, 950, 150)

        self.complete_count_info_label = QLabel(self)
        self.complete_count_info_label.setFont(get_font(12))
        self.complete_count_info_label.setText(f'{Strings.MainUi.complete_count_info_label} 0')
        self.complete_count_info_label.setAlignment(Qt.AlignRight)
        self.complete_count_info_label.setGeometry(self.Meta.WINDOW_WIDTH - 350 - 10, self.Meta.WINDOW_HEIGHT - 30,
                                                   350, 30)

        self.action_button = QPushButton(self)
        self.action_button.setFont(get_font(13))
        self.action_button.setText(Strings.MainUi.last_question_btn)
        self.action_button.setGeometry(self.Meta.WINDOW_WIDTH - 265, 575, 235, 100)

        self.load_test_btn = QPushButton(self)
        self.load_test_btn.setText(Strings.MainUi.load_test_btn)
        self.load_test_btn.setFont(get_font(13))
        self.load_test_btn.setGeometry(self.Meta.WINDOW_WIDTH // 2 - 300, centralizate(self.Meta.WINDOW_HEIGHT, 75),
                                       200, 75)

        self.start_test_btn = QPushButton(self)
        self.start_test_btn.setText(Strings.MainUi.start_test_btn)
        self.start_test_btn.setFont(get_font(13))
        self.start_test_btn.setGeometry(self.Meta.WINDOW_WIDTH // 2 + 100, centralizate(self.Meta.WINDOW_HEIGHT, 75),
                                        200, 75)

        self.current_settings = QLabel(self)
        self.current_settings.setText(Strings.MainUi.current_settings_label)
        self.current_settings.setFont(get_font(10))
        self.current_settings.setGeometry(25, 25, 500, 20)

        self.is_exel_label = QLabel(self)
        self.is_exel_label.setText(Strings.MainUi.is_exel_label)
        self.is_exel_label.setFont(get_font(10))
        self.is_exel_label.setGeometry(25, 45, 500, 20)

        self.is_show_count_label = QLabel(self)
        self.is_show_count_label.setText(Strings.MainUi.is_show_count_label)
        self.is_show_count_label.setFont(get_font(10))
        self.is_show_count_label.setGeometry(25, 65, 500, 20)

        self.is_use_password_label = QLabel(self)
        self.is_use_password_label.setText(Strings.MainUi.is_use_password_label)
        self.is_use_password_label.setFont(get_font(10))
        self.is_use_password_label.setGeometry(25, 85, 500, 20)

        self.start_test_user_btn = QPushButton(self)
        self.start_test_user_btn.setText(Strings.MainUi.start_test_user_btn)
        self.start_test_user_btn.setFont(get_font(15))
        self.start_test_user_btn.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 300),
                                             centralizate(self.Meta.WINDOW_HEIGHT, 150),
                                             300, 150)

        self.admin_end_test_button = QPushButton(self)
        self.admin_end_test_button.setText(Strings.MainUi.admin_end_btn)
        self.admin_end_test_button.setFont(get_font(13))
        self.admin_end_test_button.setGeometry(0, self.Meta.WINDOW_HEIGHT - 50, 250, 50)

        self.hide_test_items()
        self.show_prepare_items()

    def hide_test_items(self):
        """Выключает видимость элементов, отвечающих за прохождение теста"""
        self.current_question_label.setHidden(True)
        self.action_button.setHidden(True)
        self.start_test_user_btn.setHidden(True)
        self.admin_end_test_button.setHidden(True)

    def prepare_new_test(self, text: str):
        """Включает видимость элементов для регистрации нового участника"""
        self.current_question_label.setText(text)
        self.current_question_label.setHidden(False)
        self.start_test_user_btn.setHidden(False)
        self.admin_end_test_button.setHidden(False)

    def confirm_new_test(self):
        """Включает видимость элементов, отвечающих за прохождение теста"""
        self.start_test_user_btn.setHidden(True)
        self.admin_end_test_button.setHidden(True)
        self.action_button.setHidden(False)
        self.current_question_label.setHidden(False)

    def set_count_hidden(self, value: bool):
        """Изменяет видимость информационной полоски с количеством прохождений теста"""
        self.complete_count_info_label.setHidden(value)

    def set_count_value(self, value: int):
        self.complete_count_info_label.setText(f'{Strings.MainUi.complete_count_info_label} {value}')

    def hide_prepare_items(self):
        """Выключает видимость элементов, отвечающих за регистрацию нового участника"""
        self.load_test_btn.setHidden(True)
        self.start_test_btn.setHidden(True)
        self.is_exel_label.setHidden(True)
        self.current_settings.setHidden(True)
        self.is_show_count_label.setHidden(True)
        self.is_use_password_label.setHidden(True)

    def show_prepare_items(self):
        """Включает видимость элементов, отвечающих за регистрацию нового участника"""
        self.load_test_btn.setHidden(False)
        self.start_test_btn.setHidden(False)
        self.is_exel_label.setHidden(False)
        self.current_settings.setHidden(False)
        self.is_show_count_label.setHidden(False)
        self.is_use_password_label.setHidden(False)
