from asyncio import sleep
from random import choice, randint

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import get_filter
from user_bot.handlers.common.util import _get_heart_stickers
from user_bot.utils import cmd, play_stroke_anim


@cmd()
async def __steve(app: Client, msg: Message):
    img = (
        "🏿🏿🏿🏿🏿🏿🏿🏿",
        "🏿🏿🏽🏽🏽🏽🏿🏿",
        "🏽🏽🏽🏽🏽🏽🏽🏽",
        "🏽⬜️⬛️🏽🏽⬛️⬜️🏽",
        "🏽🏽🏽🏿🏿🏽🏽🏽",
        "🏽🏽🏿🏽🏽🏿🏽🏽",
        "🏽🏽🏿🏿🏿🏿🏽🏽",
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __uno(app: Client, msg: Message):
    img = (
        "⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇"
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __gubka(app: Client, msg: Message):
    img = (
        "╲┏━┳━━━━━━━━┓╲╲",
        "╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲",
        "╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲",
        "╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲",
        "╲┃◯┃╭╮╰╯┏━━━┳╯╲",
        "╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲",
        "╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲",
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __rabbit(app: Client, msg: Message):
    left_eyes = '┈┃▋▏▋▏┃┈'
    right_eyes = '┈┃╱▋╱▋┃┈'
    img = [
        '╭━━╮╭━━╮',
        '╰━╮┃┃╭━╯',
        '┈╭┛┗┛┗╮┈',
        '┈┃╱▋╱▋┃┈',
        '╭┛▔▃▔┈┗╮',
        '╰┓╰┻━╯┏╯',
        '╭┛┈┏┓┈┗╮',
        '╰━━╯╰━━╯',
    ]
    eyes = choice((True, False))
    img[3] = right_eyes if eyes else left_eyes
    await play_stroke_anim(msg, img)
    await sleep(1)

    for _ in range(randint(5, 10)):
        eyes = not eyes
        img[3] = right_eyes if eyes else left_eyes
        await msg.edit('\n'.join(img))
        await sleep(0.5)


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


def _get_sticker_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__steve, filters=get_filter('steve')),
        MessageHandler(__uno, filters=get_filter('uno')),
        MessageHandler(__gubka, filters=get_filter('gubka')),
        MessageHandler(__rabbit, filters=get_filter('rabbit')),
        MessageHandler(__like, filters=get_filter('like')),
        MessageHandler(__dislike, filters=get_filter('dislike')),
        MessageHandler(__heart, filters=get_filter('heart')),
    )
