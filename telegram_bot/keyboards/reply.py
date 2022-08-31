from typing import Final
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# region Start kb

KB_START_TRIAL: Final = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_START_TRIAL.add(
    KeyboardButton(text="Подключить бота"),
    KeyboardButton(text="Купить полную версию")
)

KB_START_PRO: Final = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_START_PRO.add(KeyboardButton(text="Подключить бота"))

# endregion

# region Stop kb

KB_STOP_PRO_BOT: Final = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_STOP_PRO_BOT.add(KeyboardButton(text="Остановить бота"))

KB_STOP_TRIAL_BOT: Final = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_STOP_TRIAL_BOT.add(KeyboardButton(text="Остановить бота"),
                      KeyboardButton(text="Купить полную версию"))

# endregion
