from pyrogram import Client
from pyrogram.types import Message


def advert(vip: bool):
    def input_func(func):
        async def wrapper(app: Client, message: Message):
            await func(app, message)
            if not vip:
                await message.edit('<b>By userbot</b> - <a href="https://t.me/Gosha_developer_bot">Ссылка</a>')
                await message.delete(revoke=False)

        return wrapper

    return input_func
