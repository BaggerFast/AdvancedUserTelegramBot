from aiogram import Dispatcher, Bot
from aiogram.types import Message


async def other_messages(msg: Message):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Я вас не понял, напишите /start!")


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(other_messages, content_types=['text'], state=None)