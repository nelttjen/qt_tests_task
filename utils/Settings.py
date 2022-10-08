import dataclasses

@dataclasses.dataclass(frozen=True)
class Settings:
    window_title: str = 'Title'