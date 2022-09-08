import sys
from pyrogram import Client
from user_bot.handlers import register_all_handlers


def start_user_bot() -> None:
    string_session = sys.argv[1]
    telegram_id = sys.argv[2]
    client = Client(
        name=telegram_id,
        session_string=string_session,
        in_memory=True,
    )
    register_all_handlers(client)
    client.run()
