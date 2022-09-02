from asyncio import sleep
from random import choice, randint

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.handlers.common.games import _get_game_handlers
from user_bot.misc import get_me_filters, cmd, play_anim
from user_bot.handlers.common.stickers import _get_sticker_handlers
from user_bot.handlers.common.texts import _get_text_handlers


@cmd(False)
async def __kill(app, msg: Message):
    await msg.edit("<b>🔪 На тебя заказали убийство.</b>")  # red
    await sleep(3)
    await msg.edit(f"<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")  # orange
    await sleep(2)

    for i in range(5, 0, -1):
        await msg.edit(f"<b>⏳ [ {i}s ]</b>")
        await sleep(1)

    await msg.edit(f"<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")
    await sleep(1)

    for i in range(6):
        await msg.edit(f"<b>👀 Поиск{'.' * (i % 3 + 1)}</b>")
        await sleep(0.5)

    kill = ["Убийца нашел тебя, к сожалению ты спрятался плохо и был убит",
            "⚔️Убийца не нашел тебя, вы  очень хорошо спрятались"]
    await msg.edit(f'<b>{choice(kill)}.</b>')


@cmd(False)
async def __night(app, msg: Message):
    sleep_words = (
        'зайка 💚', 'солнышко 💛', 'котёнок ❤', 'цветочек 💙', 'ангелочек 💜', 'принцесса 💓',
        'красотка 💕', 'милашка 💖', 'симпатяжка 💗', 'бусинка 💘',
    )
    love_words = (
        '❤ я ❤', '💚 тебя 💚', '💙 очень 💙', '💛 сильно 💛', '💜 люблю 💜',
    )
    for word in sleep_words:
        await msg.edit(f'<b>Cпокойной ночи {word}</b>')
        await sleep(0.5)
    for word in love_words:
        await msg.edit(f'<b>{word}</b>')
        await sleep(0.5)


@cmd()
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


@cmd()
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


@cmd(False)
async def __compli(app: Client, msg: Message):
    words = (
        'удивительная', 'внимательная', 'красивая', 'лучшая', 'успешная', 'заботливая', 'милая', 'прекрасная',
        'умная', 'шикарная', 'обалденная', 'очаровашка', 'любимая', 'весёлая', 'нежная', 'яркая', 'прелестная',
        'приятная', 'сладкая', 'дивная', 'ангельская', 'добрая', 'бесподобная', 'волшебная', 'крутышка', 'смелая',
        'ласковая', 'романтичная', 'великолепная', 'внимательная', 'страстная', 'игривая', 'единственная',
        'стройная', 'безумная', 'симпатичная', 'изящная', 'талантливая', 'элегантная', 'чуткая', 'уникальная',
    )
    await msg.edit(f'<b>Крошечные напоминания того, что ты...</b>')
    await sleep(1)

    for word in words:
        await msg.edit(f'<b>Cамая {word}</b> ✨')
        await sleep(0.5)
    await msg.edit(f'<b>Cамая {choice(words)}</b> ✨')


def get_common_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__bombs, filters=get_me_filters('bombs')),
        MessageHandler(__kill, filters=get_me_filters('kill')),
        MessageHandler(__night, filters=get_me_filters('night')),
        MessageHandler(__stupid, filters=get_me_filters('stupid')),
        MessageHandler(__compli, filters=get_me_filters('compli')),

        *_get_game_handlers(),
        *_get_text_handlers(),
        *_get_sticker_handlers(),


    )
