from abc import ABC
from typing import Final


class Config(ABC):
    PRICE: Final = 50
    PREFIX: Final = '.'
    HELPER: Final = '@Gamlet_Omlet'
