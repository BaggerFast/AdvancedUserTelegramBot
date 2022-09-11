from asyncio import sleep
from random import choice, randint

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import get_free_filters
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
async def __gg(app: Client, msg: Message):
    img = (
        '░░░░░░░░░░░░░░',
        "░░█▀▀█░░█▀▀█░░",
        "░░█░▄▄░░█░▄▄░░",
        "░░█▄▄█░░█▄▄█░░",
        "░░░░░░░░░░░░░░",
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __bye(app: Client, msg: Message):
    img = (
        "╭━━┳╮╱╱╭┳━━━╮",
        "┃╭╮┃╰╮╭╯┃╭━━╯",
        "┃╰╯╰╮╰╯╭┫╰━━╮",
        "┃╭━╮┣╮╭╯┃╭━━╯",
        "┃╰━╯┃┃┃╱┃╰━━╮",
        "╰━━━╯╰╯╱╰━━━╯",
    )
    await play_stroke_anim(msg, img)


def _get_sticker_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__steve, filters=get_free_filters('steve')),
        MessageHandler(__uno, filters=get_free_filters('uno')),
        MessageHandler(__gubka, filters=get_free_filters('gubka')),
        MessageHandler(__rabbit, filters=get_free_filters('rabbit')),
        MessageHandler(__gg, filters=get_free_filters('gg')),
        MessageHandler(__bye, filters=get_free_filters('bye')),
    )
