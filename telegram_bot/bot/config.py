import os
from abc import ABC
from typing import Final


class TgBot(ABC):
    TOKEN: Final = os.environ.get('TOKEN', 'define me!')
