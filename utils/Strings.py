import dataclasses


@dataclasses.dataclass(frozen=True)
class Strings:
    main_window_title: str = 'Title'
    admin_window_title: str = 'New Test Setup'

    @dataclasses.dataclass(frozen=True)
    class AdminUi:
        test_file_choose_label: str = 'Загрузить вопросы из файла'
        test_file_choose_btn: str = 'Выбрать файл'
        