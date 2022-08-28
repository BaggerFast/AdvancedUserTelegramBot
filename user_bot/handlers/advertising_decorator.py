from pyrogram import Client
from pyrogram.types import Message
from user_bot.misc.constants import VIP_STATUS


def advert(handler):
    async def wrapper(app: Client, message: Message):
        await handler(app, message)
        if not VIP_STATUS:
            await message.edit('<b>By userbot</b> - <a href="https://t.me/Gosha_developer_bot">Ссылка</a>')
            await message.delete(revoke=False)
    return wrapper
