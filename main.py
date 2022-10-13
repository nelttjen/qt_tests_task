import csv
import datetime
import json
import logging
import os
import sys

from PyQt5.QtWidgets import QApplication

from widgets import MainWindow
from utils import folder_init, init_logger, Settings, Strings


def on_launch():
    """Создание папок и логгера на старте"""
    folder_init()
    init_logger()

    logging.info('======================================')
    logging.info('= Testing app v1.0, author: NelttjeN =')
    logging.info('======================================')
    logging.info("Initialization done.")


def launch_app(debug=False):
    """Запуск и удержание приложения, возврат ответов с приложения и кода завершения"""

    app = QApplication(sys.argv)
    logging.info('Starting app...')
    wind = MainWindow(debug=debug)
    wind.show()
    return app.exec_(), wind.cleaned_data, wind.settings['exel_export']


def on_destroy(to_csv=False):
    """Cохранить результаты"""

    # logging.info('Deleting temp...')
    # try:
    #     shutil.rmtree('temp')
    # except:
    #     logging.error('Error while deleting temp folder')
    logging.info('Saving answers...')

    date_format = datetime.datetime.now().strftime('%d.%m.%Y_(%H:%M:%S)')
    fp = f'results/{date_format}'
    os.mkdir(fp) if not os.path.isdir(fp) else None

    with open(f'{fp}/results.json', 'w', encoding='utf-8') as f:
        json.dump(answers, f, ensure_ascii=False)

    if to_csv:
        format_csv(answers, fp)

    logging.info('Answers saved')
    logging.info('Exiting app... Bye-bye!')


def format_csv(obj, path):
    """Сохранить результаты в csv формате"""
    csv_row_list = []
    _answers = obj['answers']
    _raw_answers = obj['answers_raw']
    line_3 = ['', ]
    for item in _answers:
        # Количество ответов на каждый вопрос
        q_text = list(item.keys())[0]
        line_1 = [q_text, ]
        line_2 = ['Ответы', ]
        for answer, count in item[q_text].items():
            line_1.append(answer)
            line_2.append(str(count))
        for row in [line_1, line_2, line_3]:
            csv_row_list.append(row)
    csv_row_list = csv_row_list[:-1]
    csv_row_list.append(['', ])
    raw_csw_row = []
    for i, item in enumerate(_raw_answers):
        # Ответы пользователей
        user_rows = [[f'Пользователь {i + 1}', ], ]
        _max = 1
        for answer in item:
            curr_row = [answer['question_text'], ]
            curr_row.extend(answer['question_answers'])
            _max = max(_max, len(answer['question_answers']))
            user_rows.append(curr_row)
        user_rows[0].extend(['Ответ'] * _max)
        user_rows.append(['', ])
        raw_csw_row.append(user_rows)

    with open(f'{path}/results.csv', 'w', encoding='utf-8') as csv_dump:
        writer = csv.writer(csv_dump, delimiter=';')
        writer.writerows(csv_row_list)
        for rows in raw_csw_row:
            writer.writerows(rows)


if __name__ == '__main__':
    on_launch()
    exit_code, answers, to_csv = launch_app(debug=Settings.DEBUG)
    on_destroy(to_csv=to_csv)
    sys.exit(exit_code)
