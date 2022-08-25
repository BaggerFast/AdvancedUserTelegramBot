from typing import Final

from aiogram import types

main_keyboard_start_trial: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
main_keyboard_start_trial.add(types.KeyboardButton(text="Подключить бота"),
                              types.KeyboardButton(text="Купить полную версию"))

main_keyboard_start_pro: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
main_keyboard_start_pro.add(types.KeyboardButton(text="Подключить бота"))

main_keyboard_pro_bot_started: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
main_keyboard_pro_bot_started.add(types.KeyboardButton(text="Остановить бота"))

main_keyboard_trial_bot_started: Final = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
main_keyboard_trial_bot_started.add(types.KeyboardButton(text="Остановить бота"),
                                    types.KeyboardButton(text="Купить полную версию"))
