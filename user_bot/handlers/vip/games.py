from asyncio import sleep
from random import randint, choice

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from user_bot.filters import get_vip_filters
from user_bot.utils import cmd
from user_bot.handlers.vip.util import _tic_tak_toe_status


@cmd()
async def __tik_tac_toe(app: Client, msg: Message):
    field = [
        ["〰️", "〰️", "〰️"],
        ["〰️", "〰️", "〰️"],
        ["〰️", "〰️", "〰️"],
    ]
    sign = False
    for _ in range(9):
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

    await app.send_message(msg.chat.id, 'У вас: Ничья')


@cmd()
async def __kill(app, msg: Message):
    await msg.edit("<b>🔪 На тебя заказали убийство.</b>")
    await sleep(3)
    await msg.edit("<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")
    await sleep(2)

    for i in range(5, 0, -1):
        await msg.edit(f"<b>⏳ [ {i}s ]</b>")
        await sleep(1)

    await msg.edit("<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")
    await sleep(1)

    for i in range(6):
        await msg.edit(f"<b>👀 Поиск{'.' * (i % 3 + 1)}</b>")
        await sleep(0.5)

    kill = ["Убийца нашел тебя, к сожалению ты спрятался плохо и был убит",
            "⚔️Убийца не нашел тебя, вы  очень хорошо спрятались"]
    await msg.edit(f'<b>{choice(kill)}.</b>')


def _get_game_vip_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__tik_tac_toe, filters=get_vip_filters('tick')),
        MessageHandler(__kill, filters=get_vip_filters('kill')),
    )
