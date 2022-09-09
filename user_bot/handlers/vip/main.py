from asyncio import sleep
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from misc.html_tags import b
from user_bot.filters.main import get_vip_filters
from user_bot.utils import UserConfig, cmd
from user_bot.handlers.vip.games import _get_game_vip_handlers
from user_bot.handlers.vip.texts import _get_text_vip_handlers
from user_bot.handlers.vip.stickers import _get_sticker_vip_handlers


@cmd()
async def __bagger_fast(app, msg: Message):
    text = ''
    total = 'Pythоn ИМБА, Pythоn ЕДИН. И BaggerFast непобедим!!!'
    for char in total:
        text += char
        if char == ' ':
            continue
        await msg.edit(b(text))
        await sleep(0.1)


def get_vip_handlers() -> tuple | tuple[MessageHandler]:
    if not UserConfig.VIP_STATUS:
        return ()
    return (
        MessageHandler(__bagger_fast, filters=get_vip_filters('bf')),

        *_get_game_vip_handlers(),
        *_get_text_vip_handlers(),
        *_get_sticker_vip_handlers(),

    )
