import dataclasses


@dataclasses.dataclass(frozen=True)
class Strings:
    main_window_title: str = 'Title'
    admin_window_title: str = 'New Test Setup'

    @dataclasses.dataclass(frozen=True)
    class AdminUi:
        test_file_choose_label: str = 'Загрузить вопросы из файла'
        test_file_choose_btn: str = 'Выбрать файл'
        test_file_info_label: str = 'Импортированно вопросов из выбранного файла:'
        test_file_count_default_label: str = 'Файл не загружен'
        test_file_confirm_btn: str = 'Сохранить'

        exel_import_checkbox: str = 'Также экспортировать ответы в exel файл по окончанию опроса'
        show_complete_info_checkbox: str = 'Показывать сколько человек уже прошло тест'

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
