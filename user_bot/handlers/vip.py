import asyncio

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message


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


def get_vip_handlers(vip: bool) -> list[MessageHandler]:
    if not vip:
        return []
    return [
        MessageHandler(stupid, filters=(filters.me and filters.command("stupid", "."))),
    ]
