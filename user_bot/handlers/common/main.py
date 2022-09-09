from asyncio import sleep
from random import choice

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from misc.html_tags import b
from user_bot.filters import get_free_filters
from user_bot.handlers.common.games import _get_game_handlers
from user_bot.utils import cmd, play_anim
from user_bot.handlers.common.stickers import _get_sticker_handlers
from user_bot.handlers.common.texts import _get_text_handlers


@cmd()
async def __night(app, msg: Message):
    sleep_words = (
        'зайка 💚', 'солнышко 💛', 'котёнок ❤', 'цветочек 💙', 'ангелочек 💜', 'принцесса 💓',
        'красотка 💕', 'милашка 💖', 'симпатяжка 💗', 'бусинка 💘',
    )
    love_words = (
        '❤ я ❤', '💚 тебя 💚', '💙 очень 💙', '💛 сильно 💛', '💜 люблю 💜',
    )
    for word in sleep_words:
        await msg.edit(b(f'Cпокойной ночи {word}'))
        await sleep(0.5)
    for word in love_words:
        await msg.edit(b(word))
        await sleep(0.5)


@cmd(True)
async def __bombs(app: Client, msg: Message):
    row = '▪️▪️▪️▪️\n'
    bombs = '💣 💣 💣 💣\n'
    fire = '💥 💥 💥 💥\n'
    smile = '😵 😵 😵 😵\n'
    words = (
        f"{row}{row}{row}{row}{row}",
        f"{bombs}{row}{row}{row}{row}",
        f"{row}{bombs}{row}{row}{row}",
        f"{row}{row}{bombs}{row}{row}",
        f"{row}{row}{row}{bombs}{row}",
        f"{row}{row}{row}{row}{bombs}",
        f"{row}{row}{row}{row}{fire}",
        f"{row}{row}{row}{fire}{fire}",
        f"{row}{row}{row}{row}{smile}"
    )
    await play_anim(msg, words)


@cmd(True)
async def __stupid(app: Client, msg: Message):
    first_str = 'YOUR BRAIN ➡️ 🧠\n\n🧠'
    second_str = 'YOUR BRAIN ➡️ 🧠\n\n'
    words = (
        f'{first_str}         (^_^)🗑',
        f'{first_str}       (^_^)  🗑',
        f'{first_str}     (^_^)    🗑',
        f'{first_str}   (^_^)      🗑',
        f'{first_str} (^_^)        🗑',
        f'{first_str} <(^_^ <)     🗑',
        f'{second_str}(> ^_^)>🧠   🗑',
        f'{second_str} (> ^_^)>🧠  🗑',
        f'{second_str}  (> ^_^)>🧠 🗑',
        f'{second_str}   (> ^_^)>🧠🗑',
        f'{second_str}       (^_^) 🗑',
        f'{second_str}        (3_3)🗑'
    )
    await play_anim(msg, words)


@cmd()
async def __compli(app: Client, msg: Message):
    words = (
        'удивительная', 'внимательная', 'красивая', 'лучшая', 'успешная', 'заботливая', 'милая', 'прекрасная',
        'умная', 'шикарная', 'обалденная', 'очаровашка', 'любимая', 'весёлая', 'нежная', 'яркая', 'прелестная',
        'приятная', 'сладкая', 'дивная', 'ангельская', 'добрая', 'бесподобная', 'волшебная', 'крутышка', 'смелая',
        'ласковая', 'романтичная', 'великолепная', 'внимательная', 'страстная', 'игривая', 'единственная',
        'стройная', 'безумная', 'симпатичная', 'изящная', 'талантливая', 'элегантная', 'чуткая', 'уникальная',
    )
    await msg.edit('<b>Крошечные напоминания того, что ты...</b>')
    await sleep(1)

    for word in words:
        await msg.edit(b(f'Cамая {word}✨'))
        await sleep(0.5)
    await msg.edit(b(f'Cамая {choice(words)}✨'))


def get_common_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__bombs, filters=get_free_filters('bombs')),
        MessageHandler(__night, filters=get_free_filters('night')),
        MessageHandler(__stupid, filters=get_free_filters('stupid')),
        MessageHandler(__compli, filters=get_free_filters('compli')),

        *_get_game_handlers(),
        *_get_text_handlers(),
        *_get_sticker_handlers(),
    )
