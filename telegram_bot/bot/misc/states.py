from aiogram.dispatcher.filters.state import StatesGroup, State


class StartUserBot(StatesGroup):
    write_api_id = State()
    write_api_hash = State()
    write_phone = State()
    write_auth_code = State()
