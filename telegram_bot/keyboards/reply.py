from typing import Final
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

KB_START_BOT: Final = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_START_BOT.add(KeyboardButton(text="Подключить бота"))

KB_STOP_BOT: Final = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_STOP_BOT.add(KeyboardButton(text="Остановить бота"))


KB_CONTACT: Final = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_CONTACT.add(
    KeyboardButton("Отправить контакт", request_contact=True)
)
