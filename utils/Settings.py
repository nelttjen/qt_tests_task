import dataclasses


@dataclasses.dataclass(frozen=True)
class Settings:
    DEBUG: bool = True

