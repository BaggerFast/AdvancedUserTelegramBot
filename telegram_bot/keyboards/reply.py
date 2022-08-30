from typing import Final
from aiogram import types

# region Start kb

KB_START_TRIAL: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_START_TRIAL.add(types.KeyboardButton(text="Подключить бота"),
                   types.KeyboardButton(text="Купить полную версию"))

KB_START_PRO: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_START_PRO.add(types.KeyboardButton(text="Подключить бота"))

# endregion

# region Stop kb

KB_STOP_PRO_BOT: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_STOP_PRO_BOT.add(types.KeyboardButton(text="Остановить бота"))

KB_STOP_TRIAL_BOT: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_STOP_TRIAL_BOT.add(types.KeyboardButton(text="Остановить бота"),
                      types.KeyboardButton(text="Купить полную версию"))

# endregion
