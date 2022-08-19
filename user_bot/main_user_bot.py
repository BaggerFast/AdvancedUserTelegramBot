import asyncio

import os

from telethon import TelegramClient

from user_bot.commands import on_he, make_dick

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")

client = TelegramClient("anon", api_id, api_hash)

client.add_event_handler(on_he)
client.add_event_handler(make_dick)

client.start()
client.run_until_disconnected()

