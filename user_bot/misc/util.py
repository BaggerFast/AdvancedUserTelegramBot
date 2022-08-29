import asyncio
import functools

from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message
from user_bot.misc.constants import VIP_STATUS


def get_me_filters(command: str) -> bool:
    return filters.me and filters.command(command, ".")


def cmd(auto_del=True):
    def input_func(handler):
        @functools.wraps(handler)
        async def wrapper(app: Client, msg: Message):
            await handler(app, msg)
            if not VIP_STATUS:
                await asyncio.sleep(3)
                await msg.edit('<b>By userbot</b> - <a href="https://t.me/Gosha_developer_bot">Ссылка</a>')
                await msg.delete(revoke=False)
            else:
                if auto_del:
                    await msg.delete()

        return wrapper
    return input_func


async def play_stroke_anim(msg: Message, anims: tuple[str, ...], tick: float | int = 0.1):
    for i in range(len(anims)):
        data = "\n".join(anims[0:i+1])
        await msg.edit(data)
        await asyncio.sleep(tick)


async def play_anim(msg: Message, anims: tuple[str, ...], tick: float | int = 0.1):
    for anim in anims:
        await msg.edit(anim)
        await asyncio.sleep(tick)
