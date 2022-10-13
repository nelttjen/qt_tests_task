from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLineEdit

from .UI import MainWindowUI
from .util import window_centralizate, show_info, show_warn, show_error, get_font
from widgets.AgreementDialog import AgreementDialog


class MainWindow(QWidget, MainWindowUI):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.answers = []

        self.generated = []
        self.cleaned_data = []

        self.initUI()

    def initUI(self):
        self.setFixedSize(self.Meta.WINDOW_WIDTH, self.Meta.WINDOW_HEIGHT)
        self.setWindowTitle('Test creator')
        window_centralizate(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.connect_buttons()

    def connect_buttons(self):
        self.add_answer_button.clicked.connect(self.add_answer)
        self.pop_answer_button.clicked.connect(self.pop_last)

        self.reset_current_button.clicked.connect(self.new_question)
        self.next_button.clicked.connect(self.save_question)
        self.save_button.clicked.connect(self.close_window)
        self.pop_last_button.clicked.connect(self.pop_last_added)

    def new_question(self):
        for text_edit in self.answers:
            text_edit.hide()
            text_edit.deleteLater()
        self.answers = []
        self.reset_all()

    def add_answer(self):
        MAX = 10
        if len(self.answers) < MAX:
            new_line = QLineEdit(self)
            new_line.setPlaceholderText('Вариант ответа')
            new_line.setFont(get_font(12))
            new_line.setGeometry(self.Meta.ANS_START_X,
                                 self.Meta.ANS_START_Y + self.Meta.ANS_H * len(self.answers) +
                                 self.Meta.ANS_MARGIN_TOP * len(self.answers),
                                 self.Meta.ANS_W, self.Meta.ANS_H)
            new_line.setHidden(False)
            # self.add_answer_button.setGeometry(self.Meta.ANS_START_X,
            #                                    self.Meta.ANS_START_Y + self.Meta.ANS_H * (len(self.answers) + 1) +
            #                                    self.Meta.ANS_MARGIN_TOP * (len(self.answers) + 1),
            #                                    self.Meta.ANS_W, self.Meta.ANS_H)
            # self.pop_answer_button.setGeometry(self.Meta.ANS_START_X,
            #                                    self.Meta.ANS_START_Y + self.Meta.ANS_H * (len(self.answers) + 2) +
            #                                    self.Meta.ANS_MARGIN_TOP * (len(self.answers) + 2),
            #                                    self.Meta.ANS_W, self.Meta.ANS_H)
            self.answers.append(new_line)
        else:
            show_warn(self, text=f'Максимум вариантов ответа: {MAX}')

    def save_question(self):
        if len(self.answers) == 0:
            show_error(self, text='Невозможно сохранить вопрос с 0 вариантами ответа')
            return
        answer_list = []
        for answer in self.answers:
            answer_list.append(answer.text())

        _id = self.question_id.text()
        _text = self.question_text.toPlainText()
        _is_multiple = self.button_multiple.isChecked()

        if not all(answer_list) or _id == '' or _text == '':
            show_error(self, text='Заполните все пустые поля для сохранения вопроса!')
            return
        try:
            _id = int(_id)
            if _id <= 0:
                raise ValueError
        except ValueError:
            show_error(self, text='id должен быть числом, большим 0')
            return
        obj = {
            'id': _id,
            'text': _text,
            'answers': answer_list,
            'is_multiple': _is_multiple
        }
        self.generated.append(obj)
        self.new_question()
        self.update_count()

    def update_count(self):
        self.total_count.setText(f'Всего вопросов: {len(self.generated)}')

    def pop_last(self):
        if len(self.answers) > 0:
            text_edit = self.answers.pop(-1)
            text_edit.hide()
            text_edit.deleteLater()

    def pop_last_added(self):
        agreement = AgreementDialog(self, 'Удалить последний добавленный вопрос?').exec_()
        if agreement:
            if len(self.generated) > 0:
                self.generated.pop(-1)
                self.update_count()

    def close_window(self):
        agree = AgreementDialog(self, 'Сохранить вопросы и выйти из программы?').exec_()
        if agree:
            self.close()
            self.destroy()

    def clean_data(self):
        self.cleaned_data = self.generated

    def closeEvent(self, a0) -> None:
        super(MainWindow, self).closeEvent(a0)
        self.clean_data()
