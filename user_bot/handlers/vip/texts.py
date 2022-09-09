from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from user_bot.filters import get_vip_filters
from user_bot.utils import cmd, play_stroke_anim


@cmd()
async def __ban(app: Client, msg: Message):
    text = (
        "████╗███╗█╗█╗",
        "█╔══╝█╔█║█║█║",
        "████╗███║███║",
        "█╔═█║█╔█║█╔█║",
        "████║█║█║█║█║",
        "╚═══╝╚╝╚╝╚╝╚╝"
    )
    await play_stroke_anim(msg, text)


def _get_text_vip_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__ban, filters=get_vip_filters('ban')),
    )
