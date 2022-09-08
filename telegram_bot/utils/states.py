from typing import Final
from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateUserBotState(StatesGroup):
    API_ID: Final = State()
    API_HASH: Final = State()
    PHONE: Final = State()
    AUTH_CODE: Final = State()
    TWO_FA_PASSWORD: Final = State()


class AdminStates(StatesGroup):
    ADMIN: Final = State()
    INSERT_NEW_ADMIN: Final = State()
    INSERT_ADVERT_TEXT: Final = State()
    SET_VIP: Final = State()
