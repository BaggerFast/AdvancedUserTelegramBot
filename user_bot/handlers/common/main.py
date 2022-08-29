import asyncio

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.handlers.common.stickers import _get_sticker_handlers
from user_bot.handlers.common.texts import _get_text_handlers
from user_bot.misc.util import get_me_filters, cmd


@cmd()
async def __kill(app, msg: Message):
    time = 0.1
    await msg.edit(f"<b>🔪 На тебя заказали убийство.</b>")  # red
    await asyncio.sleep(3)
    await msg.edit(f"<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")  # orange
    await asyncio.sleep(2)
    await msg.edit(f"<b>⏳ [ 5s ]</b>")  # orange
    await asyncio.sleep(time)
    await msg.edit(f"<b>⌛ [ 4s ]</b>")  # red
    await asyncio.sleep(time)
    await msg.edit(f"<b>⏳ [ 3s ]</b>")  # orange
    await asyncio.sleep(time)
    await msg.edit(f"<b>⌛ [ 2s ]</b>")  # red
    await asyncio.sleep(time)
    await msg.edit(f"<b>⏳ [ 1s ]</b>")  # orange
    await asyncio.sleep(time)
    await msg.edit(f"<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")  # orange
    await asyncio.sleep(time)
    await msg.edit(f"<b>👀 Поиск.</b>")  # orange
    await asyncio.sleep(time)
    await msg.edit(f"<b>👀 Поиск..</b>")  # orange
    await asyncio.sleep(time)
    await msg.edit(f"<b>👀 Поиск...</b>")  # orange
    await asyncio.sleep(time)
    await msg.edit(f"<b>👀 Поиск.</b>")  # orange
    await asyncio.sleep(time)
    await msg.edit(f"<b>👀 Поиск..</b>")
    await asyncio.sleep(time)
    await msg.edit(f"<b>👀 Поиск...</b>")
    await asyncio.sleep(time)


@cmd()
async def __night(app, msg: Message):
    time = 0.5
    await msg.edit(f'<b>спокойной ночи зайка 💚</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи солнышко 💛</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи котёнок ❤</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи цветочек 💙</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи ангелочек 💜</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи принцесса 💓</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи красотка 💕</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи милашка 💖</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи симпатяжка 💗</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>спокойной ночи бусинка 💘</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>❤ я ❤</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>💚 тебя 💚</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>💙 очень 💙</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>💛 сильно 💛</b>')
    await asyncio.sleep(time)
    await msg.edit(f'<b>💜 люблю 💜</b>')


@cmd()
async def __bombs(app: Client, msg: Message):
    row = '▪️▪️▪️▪️\n'
    bombs = '💣 💣 💣 💣\n'
    fire = '💥 💥 💥 💥\n'
    smile = '😵 😵 😵 😵\n'
    speed = 0.1
    await msg.edit_text(f"{row}{row}{row}{row}{row}")
    await asyncio.sleep(speed)
    await msg.edit_text(f"{bombs}{row}{row}{row}{row}")
    await asyncio.sleep(speed)
    await msg.edit_text(f"{row}{bombs}{row}{row}{row}")
    await asyncio.sleep(speed)
    await msg.edit_text(f"{row}{row}{bombs}{row}{row}")
    await asyncio.sleep(speed)
    await msg.edit_text(f"{row}{row}{row}{bombs}{row}")
    await asyncio.sleep(speed)
    await msg.edit_text(f"{row}{row}{row}{row}{bombs}")
    await asyncio.sleep(speed)
    await msg.edit_text(f"{row}{row}{row}{row}{fire}")
    await asyncio.sleep(speed)
    await msg.edit_text(f"{row}{row}{row}{fire}{fire}")
    await asyncio.sleep(speed)
    await msg.edit_text(f"{row}{row}{row}{row}{smile}")


def get_common_handlers() -> list[MessageHandler]:
    handlers = [
        MessageHandler(__bombs, filters=get_me_filters('bombs')),
        MessageHandler(__kill, filters=get_me_filters('kill')),
        MessageHandler(__night, filters=get_me_filters('night')),
    ]
    handlers.extend(_get_sticker_handlers())
    handlers.extend(_get_text_handlers())
    return handlers
