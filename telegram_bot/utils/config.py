from abc import ABC
from typing import Final


class Config(ABC):
    PRICE: Final = 60
    PREFIX: Final = '.'
    HELPER: Final = '@Gamlet_Omlet'
