from abc import ABC
from typing import Final


class TgConfig(ABC):
    PRICE: Final = 60
    PREFIX: Final = '.'
    HELPER: Final = '@Gamlet_Omlet'