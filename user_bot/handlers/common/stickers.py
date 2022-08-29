from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from user_bot.misc.util import cmd, get_me_filters, play_stroke_anim


@cmd(False)
async def __russia(app: Client, msg: Message):
    img = (
        "⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️",
        "⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️",
        "🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await play_stroke_anim(msg, img)


@cmd(False)
async def __germany(app: Client, msg: Message):
    img = (
        "⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️",
        "⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️",
        "🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨",
    )
    await play_stroke_anim(msg, img)


@cmd(False)
async def __ukraine(app: Client, msg: Message):
    img = (
        "🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨",
    )
    await play_stroke_anim(msg, img)


@cmd(False)
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


@cmd(False)
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


@cmd(False)
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


@cmd(False)
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


@cmd(False)
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


def _get_sticker_handlers() -> list[MessageHandler]:
    return [
        MessageHandler(__russia, filters=get_me_filters('russia')),
        MessageHandler(__germany, filters=get_me_filters('germany')),
        MessageHandler(__ukraine, filters=get_me_filters('ukraine')),
        MessageHandler(__steve, filters=get_me_filters('steve')),
        MessageHandler(__uno, filters=get_me_filters('uno')),
        MessageHandler(__gubka, filters=get_me_filters('gubka')),
        MessageHandler(__like, filters=get_me_filters('like')),
        MessageHandler(__dislike, filters=get_me_filters('dislike')),
    ]
