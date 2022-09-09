import functools

from asyncio import sleep
from contextlib import suppress

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import MessageIdInvalid

from telegram_bot.utils import TgConfig
from user_bot.utils.config import UserConfig


def cmd(auto_del: bool = False, time: float = 3):
    def input_func(handler):
        @functools.wraps(handler)
        async def wrapper(app: Client, msg: Message):
            with suppress(MessageIdInvalid):
                await handler(app, msg)
                if not UserConfig.VIP_STATUS:
                    await sleep(time)
                    await msg.edit(f'<b>By userbot</b> - <a href="{TgConfig.BOT_URL}">Ссылка</a>')
                    await msg.delete(revoke=False)
                elif auto_del:
                    await sleep(time)
                    await msg.delete()
        return wrapper
    return input_func


async def play_stroke_anim(msg: Message, anims: tuple[str, ...] | list[str], tick: float | int = 0.1) -> None:
    for i in range(len(anims)):
        data = "\n".join(anims[0:i + 1])
        await msg.edit(data)
        await sleep(tick)


async def play_anim(msg: Message, anims: tuple[str, ...], tick: float | int = 0.1) -> None:
    for anim in anims:
        await msg.edit(anim)
        await sleep(tick)
