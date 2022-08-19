from typing import Final

from aiogram.dispatcher.filters.state import StatesGroup, State


class StartUserBot(StatesGroup):
    write_api_id: Final = State()
    write_api_hash: Final = State()
    write_phone: Final = State()
    write_auth_code: Final = State()
