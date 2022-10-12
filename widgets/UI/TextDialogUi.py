from PyQt5.QtWidgets import QTextEdit, QPushButton, QLabel

from widgets.util import get_font, centralizate
from utils import Strings, Settings


class TextDialogUi:

    class Meta:
        WINDOW_WIDTH = 400
        WINDOW_HEIGHT = 370

    def __init__(self):

        self.format_info = QLabel(self)
        self.format_info.setText(Strings.TextDialog.format_label)
        self.format_info.setGeometry(25, 5, 350, 20)
        self.format_info.setFont(get_font(9))

        self.q_count_label = QLabel(self)
        self.q_count_label.setText(Strings.TextDialog.q_count_label)
        self.q_count_label.setGeometry(25, 25, 350, 20)
        self.q_count_label.setFont(get_font(9))

        self.q_word_label = QLabel(self)
        self.q_word_label.setText(Strings.TextDialog.q_word_label)
        self.q_word_label.setGeometry(25, 45, 350, 40)
        self.q_word_label.setFont(get_font(9))
        self.q_word_label.setWordWrap(True)

        self.text_area = QTextEdit(self)
        self.text_area.setFont(get_font(12))
        self.text_area.setGeometry(25, 95, 350, 200)

        self.accept_button = QPushButton(self)
        self.accept_button.setText('OK')
        self.accept_button.setFont(get_font(10))
        self.accept_button.setGeometry(self.Meta.WINDOW_WIDTH - 60 - 25, self.Meta.WINDOW_HEIGHT - 30 - 25,
                                       60, 30)

        self.reject_button = QPushButton(self)
        self.reject_button.setText('Cencel')
        self.reject_button.setFont(get_font(10))
        self.reject_button.setGeometry(25, self.Meta.WINDOW_HEIGHT - 30 - 25, 60, 30)

        self.default_button = QPushButton(self)
        self.default_button.setText('Default')
        self.default_button.setFont(get_font(10))
        self.default_button.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 60), self.Meta.WINDOW_HEIGHT - 30 - 25,
                                        60, 30)
        self.default_button.clicked.connect(self.set_default_text)

    def set_default_text(self):
        self.text_area.setText(Settings.DEFAULT_TEST_SETTINGS['welcome_text'])
