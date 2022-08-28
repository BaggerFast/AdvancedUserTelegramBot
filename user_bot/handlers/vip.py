import asyncio
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from user_bot.misc.constants import VIP_STATUS
from user_bot.misc.util import get_me_filters


async def stupid(app: Client, message: Message):
    speed = 0.1
    first_str = 'YOUR BRAIN ➡️ 🧠\n\n🧠'
    await message.edit(f'{first_str}         (^_^)🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}       (^_^)  🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}     (^_^)    🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}   (^_^)      🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str} (^_^)        🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}<(^_^ <)      🗑')
    await asyncio.sleep(speed)

    first_str = 'YOUR BRAIN ➡️ 🧠\n\n'
    await message.edit(f'{first_str}(> ^_^)>🧠    🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str} (> ^_^)>🧠   🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}  (> ^_^)>🧠  🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}   (> ^_^)>🧠 🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}    (> ^_^)>🧠🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}     (> ^_^)> 🗑')
    await asyncio.sleep(speed)
    await message.edit(f'{first_str}     (> 3_3)> 🗑')
    await asyncio.sleep(1)


def get_vip_handlers() -> list[MessageHandler]:
    if not VIP_STATUS:
        return []
    return [
        MessageHandler(stupid, filters=get_me_filters("stupid"))
    ]
