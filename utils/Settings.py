import dataclasses

from utils.Strings import Strings


@dataclasses.dataclass(frozen=True)
class Settings:
    """Датакласс к настройками приложения"""
    DEBUG: bool = False

    DEFAULT_TEST_SETTINGS = {
            'password': '',
            'use_password': False,
            'exel_export': False,
            'show_users': False,
            'welcome_text': Strings.MainUi.start_test_help_text
        }