from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QCheckBox, QLineEdit

from utils import Strings
from widgets.util import centralizate, get_font


class AdminWindowUi:
    class Meta:
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600

    def __init__(self):
        self.test_file_choose_btn = QPushButton(self)
        self.test_file_choose_btn.setText(Strings.AdminUi.test_file_choose_btn)
        self.test_file_choose_btn.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 200), 250, 200, 100)
        self.test_file_choose_btn.setFont(get_font(15))

        self.test_file_choose_label = QLabel(self)
        self.test_file_choose_label.setText(Strings.AdminUi.test_file_choose_label)
        self.test_file_choose_label.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 400), 200, 400, 50)
        self.test_file_choose_label.setFont(get_font(12))
        self.test_file_choose_label.setAlignment(Qt.AlignCenter)

        self.test_file_info_label = QLabel(self)
        self.test_file_info_label.setText(f'{Strings.AdminUi.test_file_info_label} '
                                          f'{Strings.AdminUi.test_file_count_default_label}')
        self.test_file_info_label.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 500), 350, 500, 50)
        self.test_file_choose_label.setFont(get_font(12))
        self.test_file_choose_label.setAlignment(Qt.AlignCenter)

        self.test_file_choose_btn = QPushButton(self)
        self.test_file_choose_btn.setText(Strings.AdminUi.test_file_confirm_btn)
        self.test_file_choose_btn.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 200), 450, 200, 75)
        self.test_file_choose_btn.setFont(get_font(15))

        self.exel_import_checkbox = QCheckBox(self)
        self.exel_import_checkbox.setText(Strings.AdminUi.exel_import_checkbox)
        self.exel_import_checkbox.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 750), 25, 750, 25)
        self.exel_import_checkbox.setFont(get_font(10))
        self.exel_import_checkbox.setChecked(True)

        self.show_complete_info_checkbox = QCheckBox(self)
        self.show_complete_info_checkbox.setText(Strings.AdminUi.show_complete_info_checkbox)
        self.show_complete_info_checkbox.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 750), 50, 750, 25)
        self.show_complete_info_checkbox.setFont(get_font(10))

        self.password_input_label = QLabel(self)
        self.password_input_label.setText(Strings.AdminUi.end_password_label)
        self.password_input_label.setGeometry(500, 15, 300, 25)
        self.password_input_label.setFont(get_font(10))

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText(Strings.AdminUi.end_password_input_hint)
        self.password_input.setGeometry(500, 40, 295, 25)
        self.password_input.setFont(get_font(10))

        self.password_input_checkbox = QCheckBox(self)
        self.password_input_checkbox.setText(Strings.AdminUi.end_password_chackbox)
        self.password_input_checkbox.setGeometry(500, 70, 300, 25)
        self.password_input_checkbox.setFont(get_font(10))