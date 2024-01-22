import os
from abc import ABC
from typing import Final


class Env(ABC):
    TOKEN: Final = os.environ.get('TOKEN', 'define me!')
    API_ID: Final = os.environ.get("API_ID", "define me!")
    API_HASH: Final = os.environ.get("API_HASH", "define me!")
    ADMIN_ID: Final = int(os.environ.get("ADMIN_ID", "define me!"))
