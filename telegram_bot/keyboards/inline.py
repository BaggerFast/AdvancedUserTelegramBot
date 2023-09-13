from typing import Final
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_bot.utils import TgConfig

KB_CANCEL_SETUP: Final = InlineKeyboardMarkup(1)
KB_CANCEL_SETUP.add(
    InlineKeyboardButton("Отменить", callback_data="cancel_setup")
)

KB_INFO: Final = InlineKeyboardMarkup(1)
KB_INFO.add(
    InlineKeyboardButton("LET'S GO!", url=TgConfig.HELP_COMMANDS_URL)
)
