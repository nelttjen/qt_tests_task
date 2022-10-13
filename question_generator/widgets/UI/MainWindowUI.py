from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QRadioButton, QPushButton, QLabel

from widgets.util import centralizate, get_font


class MainWindowUI:
    class Meta:
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 720

        ANS_START_X = 25
        ANS_START_Y = 230

        ANS_W, ANS_H = 400, 30
        ANS_MARGIN_TOP = 5

    def __init__(self):
        self.add_answer_button = QPushButton(self)
        self.add_answer_button.setText('Добавить ответ')
        self.add_answer_button.setFont(get_font(12))

        self.pop_answer_button = QPushButton(self)
        self.pop_answer_button.setText('Убрать ответ')
        self.pop_answer_button.setFont(get_font(12))

        self.reset_current_button = QPushButton(self)
        self.reset_current_button.setText('Сброс вопроса')
        self.reset_current_button.setFont(get_font(12))

        self.question_text = QTextEdit(self)
        self.question_text.setFont(get_font(12))
        self.question_text.setPlaceholderText('Текст вопроса')

        self.question_id = QLineEdit(self)
        self.question_id.setFont(get_font(12))
        self.question_id.setPlaceholderText('Номер вопроса (число)')

        self.button_single = QRadioButton(self)
        self.button_single.setFont(get_font(12))
        self.button_single.setText('Один ответ')

        self.button_multiple = QRadioButton(self)
        self.button_multiple.setFont(get_font(12))
        self.button_multiple.setText('Несколько ответов')

        self.radio_group = [self.button_single, self.button_multiple]

        self.next_button = QPushButton(self)
        self.next_button.setText('Добавить вопрос')
        self.next_button.setFont(get_font(12))

        self.save_button = QPushButton(self)
        self.save_button.setText('Сохранить вопросы')
        self.save_button.setFont(get_font(12))

        self.total_count = QLabel(self)
        self.total_count.setText('Всего вопросов: 0')
        self.total_count.setFont(get_font(12))
        self.total_count.setAlignment(Qt.AlignCenter)

        self.pop_last_button = QPushButton(self)
        self.pop_last_button.setText('Удалить ласт вопрос')
        self.pop_last_button.setFont(get_font(12))

        self.reset_all()

    def reset_all(self):
        self.button_single.setChecked(True)
        self.button_multiple.setChecked(False)
        self.question_id.setText('')
        self.question_text.setText('')

        self.question_id.setGeometry(25, 25, 250, 30)
        self.question_text.setGeometry(25, 60, 950, 160)
        self.add_answer_button.setGeometry(self.Meta.ANS_START_X + self.Meta.ANS_W + 15, self.Meta.ANS_START_Y,
                                           250, self.Meta.ANS_H)
        self.pop_answer_button.setGeometry(self.Meta.ANS_START_X + self.Meta.ANS_W + 15,
                                           self.Meta.ANS_START_Y + self.Meta.ANS_H + self.Meta.ANS_MARGIN_TOP,
                                           250, self.Meta.ANS_H)
        self.button_single.setGeometry(self.Meta.WINDOW_WIDTH - 250 - 25, 230,
                                       150, 30)
        self.button_multiple.setGeometry(self.Meta.WINDOW_WIDTH - 250 - 25, 260,
                                         250, 30)

        self.save_button.setGeometry(self.Meta.WINDOW_WIDTH - 200 - 25, self.Meta.WINDOW_HEIGHT - 50 - 25,
                                     200, 50)
        self.next_button.setGeometry(self.Meta.WINDOW_WIDTH - 250 - 25, 300,
                                     250, 75)
        self.reset_current_button.setGeometry(25, self.Meta.WINDOW_HEIGHT - 50 - 25,
                                              200, 50)
        self.pop_last_button.setGeometry(self.Meta.WINDOW_WIDTH - 250 - 25, 390,
                                         250, 75)

        self.total_count.setGeometry(centralizate(self.Meta.WINDOW_WIDTH, 300), self.Meta.WINDOW_HEIGHT - 55,
                                     300, 30)
