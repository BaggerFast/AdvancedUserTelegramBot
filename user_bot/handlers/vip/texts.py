from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.utils import cmd, play_stroke_anim, get_me_filters


@cmd(False)
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
        MessageHandler(__ban, filters=get_me_filters('ban')),
    )