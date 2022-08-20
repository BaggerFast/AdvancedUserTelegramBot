import sys

import loguru
from telethon import TelegramClient

from user_bot.commands import on_he, make_dick


def create_bot():
    try:
        api_id: int = int(sys.argv[0])
        telegram_id: int = int(sys.argv[3])
        auth_code = 0
        try:
            auth_code: int = int(sys.argv[4])
        except Exception:
            auth_code = None
        phone: str = str(sys.argv[2])
        api_hash: str = str(sys.argv[1])

        def get_auth_code():
            return auth_code

        client = TelegramClient(f"{telegram_id}", api_id, api_hash)

        client.add_event_handler(on_he)
        client.add_event_handler(make_dick)

        client.start(phone=phone, code_callback=get_auth_code)
        client.run_until_disconnected()
    except Exception as e:
        loguru.logger.add("logs.txt")
        loguru.logger.error(e)


create_bot()
