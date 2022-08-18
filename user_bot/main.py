import asyncio

from telethon import TelegramClient

from user_bot.commands import on_he, make_dick

api_id = 14768581
api_hash = '01e109a7eaf55426151d9805906928e7'

client = TelegramClient("anon", api_id, api_hash)

client.add_event_handler(on_he)
client.add_event_handler(make_dick)

client.start(phone="+79206671979")
client.run_until_disconnected()

