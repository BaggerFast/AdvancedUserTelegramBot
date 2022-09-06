from abc import ABC
from typing import Final


class TgConfig(ABC):
    PRICE: Final = 60
    PREFIX: Final = '.'
    HELPER_URL: Final = '@Gamlet_Omlet'
    BOT_URL: Final = 'https://t.me/PronimBot'
