from asyncio import sleep

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from user_bot.handlers.vip.util import _get_heart_stickers, _get_pacman_stickers
from user_bot.utils import get_me_filters, play_stroke_anim, cmd


@cmd(False)
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


@cmd(False)
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


@cmd(False)
async def __heart(app: Client, msg: Message):
    # todo: heart
    img = _get_heart_stickers()
    for anim in img:
        await msg.edit('\n'.join(anim))
        await sleep(0.2)


@cmd(False)
async def __pacman(app: Client, msg: Message):
    img = _get_pacman_stickers()
    for anim in img:
        await msg.edit('\n'.join(anim))
        await sleep(0.2)


def _get_sticker_vip_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__like, filters=get_me_filters('like')),
        MessageHandler(__dislike, filters=get_me_filters('dislike')),
        MessageHandler(__heart, filters=get_me_filters('heart')),
        MessageHandler(__pacman, filters=get_me_filters('pacman')),
    )
