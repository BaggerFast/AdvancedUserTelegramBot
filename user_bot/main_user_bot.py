import sys
from telethon import TelegramClient
from user_bot.commands import on_he, make_dick


def create_bot():
    api_id: int = sys.argv[0]
    auth_code: int = sys.argv[4]
    telegram_id: int = sys.argv[3]

    phone: str = sys.argv[2]
    api_hash: str = sys.argv[1]

    client = TelegramClient(f"sessions/{telegram_id}", api_id, api_hash)

    client.add_event_handler(on_he)
    client.add_event_handler(make_dick)

    client.start(phone="+79206671979", code_callback=lambda: auth_code)
    client.run_until_disconnected()


create_bot()
