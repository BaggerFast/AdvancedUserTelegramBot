from aiogram import Dispatcher, Bot
from aiogram.types import Message

from telegram_bot.database.methods import create_user
from telegram_bot.handlers.user.user_bot import _register_user_bot_handlers
from telegram_bot.handlers.user.buy_vip import _register_vip_handlers
from .user_bot import _process
from ...misc.util import get_main_keyboard


async def __start(msg: Message) -> None:
    create_user(msg.from_user.id)
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    keyboard = get_main_keyboard(user_id, user_id in _process)
    await bot.send_message(user_id, "Hi, this is super user-bot!", reply_markup=keyboard)


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__start, commands=["start"])
    _register_vip_handlers(dp)
    _register_user_bot_handlers(dp)
