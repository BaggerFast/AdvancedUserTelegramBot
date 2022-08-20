import os

from telethon import TelegramClient
from misc.path import PathManager


async def send_code(phone, api_id, api_hash):
    client = TelegramClient(f"telegram_bot/bot/misc/sessions/{phone}", api_id, api_hash)
    await client.connect()
    await client.send_code_request(phone=phone, force_sms=True)
    await client.disconnect()
    os.remove(PathManager.get(f"telegram_bot/bot/misc/sessions/{phone}.session"))


