import dataclasses


@dataclasses.dataclass(frozen=True)
class Strings:
    main_window_title: str = 'Title'
    admin_window_title: str = 'New Test Setup'
    text_dialog_title: str = 'Изменить текст'

    @dataclasses.dataclass(frozen=True)
    class AdminUi:
        test_file_choose_label: str = 'Загрузить вопросы из файла'
        test_file_choose_btn: str = 'Выбрать файл'
        test_file_info_label: str = 'Импортированно вопросов из выбранного файла:'
        test_file_count_default_label: str = 'Файл не загружен'
        test_file_confirm_btn: str = 'Сохранить'

        exel_import_checkbox: str = 'Также экспортировать ответы в exel файл по окончанию опроса'
        show_complete_info_checkbox: str = 'Показывать сколько человек уже прошло тест'
        change_text_btn: str = 'Изменить приветственный текст'

        end_password_input_hint: str = 'Введите пароль (мин. 3 символа)'
        end_password_label: str = 'Задайте пароль для завершения тестирования'
        end_password_chackbox: str = 'Завершение теста только по паролю'

        file_choose_dialog_caption: str = 'Выберите файл...'
        file_permission_error: str = 'Невозможно открыть файл: Ошибка доступа'
        file_read_error: str = 'Невозможно открыть файл: Ошиобка чтения\n' \
                               'Возможно файл не является фалом с данными теста'
        file_empty_warn: str = 'Файл, который вы выбрали, содержит в себе\n' \
                               '0 доступных для импорта вопросов'
        no_password_error: str = 'Задайте пароль для окончания теста\n' \
                                 'Минимальная длинна пароля: 3 символа'

    @dataclasses.dataclass(frozen=True)
    class MainUi:
        complete_count_info_label: str = 'Количество прохождений теста:'

        load_test_btn: str = 'Загрузить тест'
        start_test_btn: str = 'Начать тест'
        admin_end_btn: str = 'Завершить тестирование'

        start_test_user_btn: str = 'Пройти тест'
        start_test_help_text: str = 'Здравствуйте! Вам предложено пройти тест.\n' \
                                    'Тест содержит в себе %q_count% %q_word%.\n' \
                                    'Тест полностью анонимный.'

        current_settings_label: str = 'Текущие настройки теста:'
        is_exel_label: str = 'Экспротировать ответы в Exel:'
        is_show_count_label: str = 'Показывать количество прохождений:'
        is_use_password_label: str = 'Использовать пароль для окончания теста:'

        next_question_btn: str = 'Следующий вопрос'
        last_question_btn: str = 'Завершить тестирование'

        single_question_hint: str = '(Выберите один вариант ответа)'
        multiple_question_hint: str = '(Выберите один или несколько вариантов ответа)'

        questions_not_load_error: str = 'Невозможно начать тест\n' \
                                        'Загружено вопросов: 0'

        agreement_no_pass: str = 'Вы действительно хотите завершить тестирование?'
        agreement_use_pass: str = 'Введите пароль для завершения тестирования'

        answer_not_selected: str = 'Пожалуйста, выберите один или несколько ответов!'

    @dataclasses.dataclass(frozen=True)
    class TextDialog:
        format_label = 'Доступные переменные для форматирования:'
        q_count_label = '%q_count% - Количество загруженных вопросов'
        q_word_label = '%q_word% - Слово "вопрос", падеж синхронизируется с количеством вопросов'
