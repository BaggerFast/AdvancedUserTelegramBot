from aiogram import Dispatcher, Bot
from aiogram.types import Message

from telegram_bot.database.methods import create_user, check_vip
from telegram_bot.handlers.user.user_bot_creator import _register_user_bot_handlers
from telegram_bot.handlers.user.buy_vip import _register_vip_handlers
from telegram_bot.keyboards import main_keyboard_start_pro, main_keyboard_start_trial


async def __start(msg: Message) -> None:
    create_user(msg.from_user.id)
    bot: Bot = msg.bot
    # todo fix
    if check_vip(msg.from_user.id):
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_pro)
    else:
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_trial)


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__start, commands=["start"])
    _register_vip_handlers(dp)
    _register_user_bot_handlers(dp)
