from aiogram import Dispatcher, Bot
from aiogram.types import Message

from telegram_bot.handlers.user.user_bot import _register_user_bot_handlers
from telegram_bot.handlers.user.buy_vip import _register_vip_handlers
from .user_bot import _process
from ...database.methods.create import create_user
from ...misc.util import get_main_keyboard
from ...keyboards import KB_INFO


async def __start(msg: Message) -> None:
    create_user(msg.from_user.id)
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    keyboard = get_main_keyboard(user_id, user_id in _process)
    await bot.send_message(user_id, f"Привет, <b>{msg.from_user.first_name}</b>!\n"
                                    f"Это <b>лучший</b> юзер бот с анимациями!😎", reply_markup=keyboard,
                           parse_mode="HTML")


async def __teh_support(msg: Message):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Если у вас возникли проблемы. Напишите нам - @Gamlet_Omlet")


async def __help(msg: Message):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Выберите категорию комманд:", reply_markup=KB_INFO)


async def __vip_commands(msg: Message):
    bot: Bot = msg.bot
    message = "Все VIP комманды:\n" \
              ".kill"
    await bot.send_message(msg.from_user.id, message)


async def __free_commands(msg: Message):
    bot: Bot = msg.bot
    message = "Все FREE комманды:\n" \
              ".stupid"
    await bot.send_message(msg.from_user.id, message)


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__teh_support, content_types=["text"], text="Тех-поддержка ⚙")
    dp.register_message_handler(__help, content_types=['text'], text="Узнать комманды 📌")
    dp.register_callback_query_handler(__vip_commands, lambda c: c.data == "vip_commands")
    dp.register_callback_query_handler(__free_commands, lambda c: c.data == "free_commands")
    _register_vip_handlers(dp)
    _register_user_bot_handlers(dp)
