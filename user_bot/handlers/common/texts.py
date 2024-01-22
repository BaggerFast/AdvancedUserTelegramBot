from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import get_filter
from user_bot.utils import cmd, play_stroke_anim


@cmd()
async def __hello(app: Client, msg: Message):
    text = (
        "╔┓┏╦━━╦┓╔┓╔━━╗",
        "║┗┛║┗━╣┃║┃║╯╰║",
        "║┏┓║┏━╣┗╣┗╣╰╯║",
        "╚┛┗╩━━╩━╩━╩━━╝"
    )
    await play_stroke_anim(msg, text)


@cmd()
async def __bruh(app: Client, msg: Message):
    text = (
        "╭━━╮╱╱╱╱╱╭╮",
        "┃╭╮┃╱╱╱╱╱┃┃",
        "┃╰╯╰┳━┳╮╭┫╰━╮",
        "┃╭━╮┃╭┫┃┃┃╭╮┃",
        "┃╰━╯┃┃┃╰╯┃┃┃┃",
        "╰━━━┻╯╰━━┻╯╰╯",
    )
    await play_stroke_anim(msg, text)


@cmd()
async def __press_f(app: Client, msg: Message):
    text = (
        "████████",
        "██",
        "██",
        "██████",
        "██",
        "██",
        "██"
    )
    await play_stroke_anim(msg, text)


@cmd()
async def __lol(app: Client, msg: Message):
    text = (
        "┏━┓┈┈╭━━━━╮┏━┓┈┈",
        "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈",
        "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓",
        "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃",
        "┗━━━┛╰━━━━╯┗━━━┛",
    )
    await play_stroke_anim(msg, text)


@cmd()
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


def _get_text_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__hello, filters=get_filter('hello')),
        MessageHandler(__bruh, filters=get_filter('bruh')),
        MessageHandler(__press_f, filters=get_filter('f')),
        MessageHandler(__lol, filters=get_filter('lol')),
        MessageHandler(__ban, filters=get_filter('ban')),
    )
