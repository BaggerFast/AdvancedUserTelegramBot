import os
import subprocess
import sys

from telethon import TelegramClient
from misc.path import PathManager


def start_user_bot(arg):
    subprocess.Popen([sys.executable, "user_bot/main_user_bot.py", *arg])


async def send_code(phone, api_id, api_hash):
    client = TelegramClient(f"telegram_bot/bot/misc/sessions/{phone}", api_id, api_hash)
    await client.connect()
    await client.send_code_request(phone=phone, force_sms=True)
    await client.disconnect()
    os.remove(PathManager.get(f"telegram_bot/bot/misc/sessions/{phone}.session"))


