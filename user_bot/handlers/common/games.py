from asyncio import sleep
from random import randint, choice

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.handlers.common.util import _tic_tak_toe_status
from user_bot.misc import cmd, get_me_filters


@cmd(False)
async def __tik_tac_toe(app: Client, msg: Message):
    field = [
        ["〰️", "〰️", "〰️"],
        ["〰️", "〰️", "〰️"],
        ["〰️", "〰️", "〰️"],
    ]
    sign = False
    for i in range(9):
        data = []

        rand_x, rand_y = randint(0, 2), randint(0, 2)
        while field[rand_y][rand_x] != '〰️':
            rand_x, rand_y = randint(0, 2), randint(0, 2)
        move = '❌' if sign else '⭕️'
        field[rand_y][rand_x] = move
        status = _tic_tak_toe_status(field, move)

        for value in field:
            data.append("❗".join(value))

        await sleep(0.5)

        await msg.edit("\n➖➕➖➕➖\n".join(data))
        if status:
            await app.send_message(msg.chat.id, f'Выиграл: {move}')
            return

        sign = not sign

    await app.send_message(msg.chat.id, f'У вас: Ничья')


@cmd(False)
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
        MessageHandler(__tik_tac_toe, filters=get_me_filters('tick')),
        MessageHandler(__coin, filters=get_me_filters('coin')),
    )
