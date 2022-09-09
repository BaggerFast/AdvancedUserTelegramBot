from asyncio import sleep
from random import randint, choice

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import get_free_filters
from user_bot.utils import cmd


@cmd()
async def __coin(app: Client, msg: Message):
    loader = (
        f'{randint(1, 10)}%   █▒▒▒▒▒▒▒▒▒▒▒▒',
        f'{randint(15, 30)}%  ███▒▒▒▒▒▒▒▒▒▒',
        f'{randint(30, 40)}%  █████▒▒▒▒▒▒▒▒',
        f'{randint(45, 55)}%  ███████▒▒▒▒▒▒',
        f'{randint(60, 75)}%  █████████▒▒▒▒',
        f'{randint(80, 90)}%  ███████████▒▒',
        '100% █████████████',
    )
    for i in range(1, 4):
        await msg.edit(f'<b>🪙 Бросаю монетку{"." * i}</b>')
        await sleep(0.5)
    for text in loader:
        await msg.edit(f'{text}')
        await sleep(0.5)
    await sleep(1)
    await msg.edit(f"<b>Мой вердикт: {choice(('Орел', 'Решка'))}</b>")


def _get_game_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__coin, filters=get_free_filters('coin')),
    )
