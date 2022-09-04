from asyncio import sleep
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from user_bot.handlers.vip.games import _get_game_vip_handlers
from user_bot.handlers.vip.stickers import _get_sticker_vip_handlers
from user_bot.handlers.vip.texts import _get_text_vip_handlers
from user_bot.utils import get_me_filters, UserConfig, cmd


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


def get_vip_handlers() -> tuple | tuple[MessageHandler]:
    if not UserConfig.VIP_STATUS:
        return ()
    return (
        MessageHandler(__bagger_fast, filters=get_me_filters('bf')),

        *_get_game_vip_handlers(),
        *_get_text_vip_handlers(),
        *_get_sticker_vip_handlers(),

    )