from aiogram import Dispatcher, Bot
from aiogram.types import Message

from telegram_bot.handlers.user.buy_vip import _register_vip_handlers
from telegram_bot.handlers.user.user_bot import _register_user_bot_handlers

from telegram_bot.utils import TgConfig
from telegram_bot.database.methods.create import create_user
from telegram_bot.keyboards import KB_INFO, get_main_keyboard


async def __start(msg: Message) -> None:
    create_user(msg.from_user.id)
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    keyboard = get_main_keyboard(user_id)
    await bot.send_message(user_id, f"Привет, <b>{msg.from_user.first_name}</b>!\n"
                                    f"Это <b>лучший</b> юзер бот с анимациями!😎", reply_markup=keyboard)


async def __teh_support(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, f"Если у вас возникли проблемы. Напишите нам - {TgConfig.HELPER_URL}")


async def __help(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Выберите категорию команд:", reply_markup=KB_INFO)


def register_users_handlers(dp: Dispatcher) -> None:

    # region Msg handlers

    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__teh_support, content_types=["text"], text="Тех-поддержка ⚙")
    dp.register_message_handler(__help, content_types=['text'], text="Узнать команды 📌")

    # endregion

    # region Callback handlers

    # endregion

    _register_vip_handlers(dp)
    _register_user_bot_handlers(dp)
