from asyncio import sleep

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from user_bot.filters import get_vip_filters
from user_bot.handlers.vip.util import _get_heart_stickers
from user_bot.utils import play_stroke_anim, cmd


@cmd()
async def __like(app: Client, msg: Message):
    img = (
        "🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦🟦🟦🟦⬜️🟦🟦🟦",
        "🟦🟦⬜️⬜️⬜️🟦⬜️🟦",
        "🟦🟦⬜️⬜️⬜️🟦⬜️🟦",
        "🟦🟦⬜️⬜️⬜️🟦⬜️🟦",
        "🟦🟦🟦🟦🟦🟦🟦🟦",
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __dislike(app: Client, msg: Message):
    img = (
        "🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟥🟥⬜️⬜️⬜️🟥⬜️🟥",
        "🟥🟥⬜️⬜️⬜️🟥⬜️🟥",
        "🟥⬜️⬜️⬜️⬜️🟥⬜️🟥",
        "🟥🟥🟥🟥⬜️🟥🟥🟥",
        "🟥🟥🟥🟥🟥🟥🟥🟥",
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __heart(app: Client, msg: Message):
    img = _get_heart_stickers()
    for anim in img:
        await msg.edit('\n'.join(anim))
        await sleep(0.5)


def _get_sticker_vip_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__like, filters=get_vip_filters('like')),
        MessageHandler(__dislike, filters=get_vip_filters('dislike')),
        MessageHandler(__heart, filters=get_vip_filters('heart')),
    )
