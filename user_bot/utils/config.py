import sys
from abc import ABC
from typing import Final


class UserConfig(ABC):
    VIP_STATUS: Final = bool(int(sys.argv[3]))