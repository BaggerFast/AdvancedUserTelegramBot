from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery

from misc import get_vip_commands_help, get_commands_help
from telegram_bot.handlers.user.user_bot import _register_user_bot_handlers
from telegram_bot.handlers.user.buy_vip import _register_vip_handlers
from ...database.methods.create import create_user
from ...utils import TgConfig
from ...utils.util import get_main_keyboard
from ...keyboards import KB_INFO


async def __start(msg: Message) -> None:
    create_user(msg.from_user.id)
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    keyboard = get_main_keyboard(user_id)
    await bot.send_message(user_id, f"Привет, <b>{msg.from_user.first_name}</b>!\n"
                                    f"Это <b>лучший</b> юзер бот с анимациями!😎", reply_markup=keyboard,
                           parse_mode="HTML")


async def __teh_support(msg: Message):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, f"Если у вас возникли проблемы. Напишите нам - {TgConfig.HELPER_URL}")


async def __help(msg: Message):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Выберите категорию комманд:", reply_markup=KB_INFO)


async def __vip_commands(query: CallbackQuery):
    bot: Bot = query.bot
    commands = sorted(get_vip_commands_help())
    message = "Все <b>VIP</b> команды:\n\n"
    for cmd in commands:
        message += f'{TgConfig.PREFIX}<b><i>{cmd.lower()}</i></b>\n'
    await bot.send_message(query.from_user.id, message)


async def __free_commands(query: CallbackQuery):
    bot: Bot = query.bot
    commands = sorted(get_commands_help())
    message = "Все <b>FREE</b> команды:\n\n"
    for cmd in commands:
        message += f'{TgConfig.PREFIX}<b><i>{cmd.lower()}</i></b>\n'
    await bot.send_message(query.from_user.id, message)


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__teh_support, content_types=["text"], text="Тех-поддержка ⚙")
    dp.register_message_handler(__help, content_types=['text'], text="Узнать команды 📌")
    dp.register_callback_query_handler(__vip_commands, lambda c: c.data == "vip_commands")
    dp.register_callback_query_handler(__free_commands, lambda c: c.data == "free_commands")
    _register_vip_handlers(dp)
    _register_user_bot_handlers(dp)
