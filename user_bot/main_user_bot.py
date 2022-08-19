import sys

from telethon import TelegramClient

from user_bot.commands import on_he, make_dick

api_id: int = sys.argv[0]
api_hash: str = sys.argv[1]
phone: str = sys.argv[2]
telegram_id: int = sys.argv[3]
auth_code: int = sys.argv[4]

client = TelegramClient(f"sessions/{telegram_id}", api_id, api_hash)

client.add_event_handler(on_he)
client.add_event_handler(make_dick)


def get_code(code=auth_code):
    return code


client.start(phone="+79206671979", code_callback=get_code)
client.run_until_disconnected()
