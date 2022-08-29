from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from user_bot.misc.util import cmd, get_me_filters, play_stroke_anim


@cmd(False)
async def __hello(app: Client, msg: Message):
    text = (
        "╔┓┏╦━━╦┓╔┓╔━━╗",
        "║┗┛║┗━╣┃║┃║╯╰║",
        "║┏┓║┏━╣┗╣┗╣╰╯║",
        "╚┛┗╩━━╩━╩━╩━━╝"
    )
    await play_stroke_anim(msg, text)


@cmd(False)
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


@cmd(False)
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


@cmd(False)
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


@cmd(False)
async def __lol(app: Client, msg: Message):
    text = (
        "┏━┓┈┈╭━━━━╮┏━┓┈┈",
        "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈",
        "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓",
        "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃",
        "┗━━━┛╰━━━━╯┗━━━┛",
    )
    # todo: like this in stikers and texts
    await play_stroke_anim(msg, text)


def _get_text_handlers() -> list[MessageHandler]:
    return [
        MessageHandler(__hello, filters=get_me_filters('hello')),
        MessageHandler(__ban, filters=get_me_filters('ban')),
        MessageHandler(__bruh, filters=get_me_filters('bruh')),
        MessageHandler(__press_f, filters=get_me_filters('f')),
        MessageHandler(__lol, filters=get_me_filters('lol')),
    ]
