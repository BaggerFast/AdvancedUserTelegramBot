import os
from abc import ABC
from typing import Final


class PathManager(ABC):
    ROOT: Final = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def get(cls, path: str) -> str:
        return os.path.join(cls.ROOT, path)
