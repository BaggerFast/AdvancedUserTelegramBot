import os
from typing import Final


class PathManager:
    ROOT: Final = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def get(cls, path: str) -> str:
        return os.path.join(cls.ROOT, path)
