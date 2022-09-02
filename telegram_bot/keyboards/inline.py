from typing import Final

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


KB_CANCEL_SETUP: Final = InlineKeyboardMarkup(1)
KB_CANCEL_SETUP.add(
    InlineKeyboardButton("Отменить", callback_data="cancel_setup")
)