from typing import Final

from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateUserBotState(StatesGroup):
    API_ID: Final = State()
    API_HASH: Final = State()
    PHONE: Final = State()
    AUTH_CODE: Final = State()
