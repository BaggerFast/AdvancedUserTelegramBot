from asyncio import sleep
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from user_bot.misc.util import cmd, get_me_filters
from user_bot.misc.constants import VIP_STATUS


@cmd(False)
async def __bagger_fast(app, msg: Message):
    text = ''
    total = 'Pythоn ИМБА, Pythоn ЕДИН. И BaggerFast непобедим!!!'
    for char in total:
        text += char
        if char == ' ':
            continue
        await msg.edit(f"<b>{text}</b>")
        await sleep(0.1)


def get_vip_handlers() -> list[MessageHandler]:
    if not VIP_STATUS:
        return []
    return [
        MessageHandler(__bagger_fast, filters=get_me_filters('bf')),
    ]
