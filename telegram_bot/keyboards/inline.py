from typing import Final

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

me_telegram_keyboard: Final = InlineKeyboardMarkup(1)
me_telegram_keyboard.add(InlineKeyboardButton("Мои данные", url="https://my.telegram.org"))
