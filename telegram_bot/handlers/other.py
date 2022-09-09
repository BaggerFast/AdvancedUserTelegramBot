from aiogram import Dispatcher, Bot
from aiogram.types import Message


async def other_messages(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Я вас не понял, напишите /start!")


async def __get_id(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user
    await bot.send_message(user.id, f"{user.username}: {user.id}")


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__get_id, commands=["id"])
    dp.register_message_handler(other_messages, content_types=['text'], state=None)
