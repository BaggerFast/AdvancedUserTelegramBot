from typing import Final

from aiogram import types

main_keyboard_start_trial: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
main_keyboard_start_trial.add(types.KeyboardButton(text="Подключить бота"),
                              types.KeyboardButton(text="Купить полную версию"))

main_keyboard_start_pro: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
main_keyboard_start_pro.add(types.KeyboardButton(text="Подключить бота"))

