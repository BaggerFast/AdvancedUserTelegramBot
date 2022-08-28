import asyncio

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.handlers.advertising_decorator import advert
from user_bot.misc.util import get_me_filters


@advert
async def kill(app, message: Message):
    time = 0.1
    await message.edit(f"<b>🔪 На тебя заказали убийство.</b>")  # red
    await asyncio.sleep(3)
    await message.edit(f"<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")  # orange
    await asyncio.sleep(2)
    await message.edit(f"<b>⏳ [ 5s ]</b>")  # orange
    await asyncio.sleep(time)
    await message.edit(f"<b>⌛ [ 4s ]</b>")  # red
    await asyncio.sleep(time)
    await message.edit(f"<b>⏳ [ 3s ]</b>")  # orange
    await asyncio.sleep(time)
    await message.edit(f"<b>⌛ [ 2s ]</b>")  # red
    await asyncio.sleep(time)
    await message.edit(f"<b>⏳ [ 1s ]</b>")  # orange
    await asyncio.sleep(time)
    await message.edit(f"<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")  # orange
    await asyncio.sleep(time)
    await message.edit(f"<b>👀 Поиск.</b>")  # orange
    await asyncio.sleep(time)
    await message.edit(f"<b>👀 Поиск..</b>")  # orange
    await asyncio.sleep(time)
    await message.edit(f"<b>👀 Поиск...</b>")  # orange
    await asyncio.sleep(time)
    await message.edit(f"<b>👀 Поиск.</b>")  # orange
    await asyncio.sleep(time)
    await message.edit(f"<b>👀 Поиск..</b>")
    await asyncio.sleep(time)
    await message.edit(f"<b>👀 Поиск...</b>")
    await asyncio.sleep(time)


@advert
async def night(app, message: Message):
    time = 0.5
    await message.edit(f'<b>спокойной ночи зайка 💚</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи солнышко 💛</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи котёнок ❤</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи цветочек 💙</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи ангелочек 💜</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи принцесса 💓</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи красотка 💕</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи милашка 💖</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи симпатяжка 💗</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>спокойной ночи бусинка 💘</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>❤ я ❤</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>💚 тебя 💚</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>💙 очень 💙</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>💛 сильно 💛</b>')
    await asyncio.sleep(time)
    await message.edit(f'<b>💜 люблю 💜</b>')


@advert
async def bombs(app: Client, message: Message):
    row = '▪️▪️▪️▪️\n'
    bombs = '💣 💣 💣 💣\n'
    fire = '💥 💥 💥 💥\n'
    smile = '😵 😵 😵 😵\n'
    speed = 0.1
    await message.edit_text(f"{row}{row}{row}{row}{row}")
    await asyncio.sleep(speed)
    await message.edit_text(f"{bombs}{row}{row}{row}{row}")
    await asyncio.sleep(speed)
    await message.edit_text(f"{row}{bombs}{row}{row}{row}")
    await asyncio.sleep(speed)
    await message.edit_text(f"{row}{row}{bombs}{row}{row}")
    await asyncio.sleep(speed)
    await message.edit_text(f"{row}{row}{row}{bombs}{row}")
    await asyncio.sleep(speed)
    await message.edit_text(f"{row}{row}{row}{row}{bombs}")
    await asyncio.sleep(speed)
    await message.edit_text(f"{row}{row}{row}{row}{fire}")
    await asyncio.sleep(speed)
    await message.edit_text(f"{row}{row}{row}{fire}{fire}")
    await asyncio.sleep(speed)
    await message.edit_text(f"{row}{row}{row}{row}{smile}")


def get_common_handlers() -> list[MessageHandler]:

    return [
        MessageHandler(bombs, filters=get_me_filters('bombs')),
        MessageHandler(kill, filters=get_me_filters('kill')),
        MessageHandler(night, filters=get_me_filters('night')),
    ]
