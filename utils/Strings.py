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
