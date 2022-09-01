from typing import Final

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

me_telegram_keyboard: Final = InlineKeyboardMarkup(1)
me_telegram_keyboard.add(InlineKeyboardButton("Мои данные", url="https://my.telegram.org"))

admin_keyboard: Final = InlineKeyboardMarkup(1)
admin_keyboard.add(
    InlineKeyboardButton("Добавить администратора", callback_data="add_admin"),
    InlineKeyboardButton("Выйти", callback_data="exit"),
    InlineKeyboardButton("Рассылка", callback_data="advertising"),
)

KB_CANCEL_SETUP: Final = InlineKeyboardMarkup(1)
KB_CANCEL_SETUP.add(
    InlineKeyboardButton("Отменить", callback_data="cancel_setup")
)
