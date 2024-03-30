import sys
from pyrogram import Client
from user_bot.handlers import register_all_handlers
from telegram_bot.utils.util import revoke_session


def start_user_bot() -> None:
    string_session = sys.argv[1]
    telegram_id = sys.argv[2]
    client = Client(
        name=telegram_id,
        session_string=string_session,
        in_memory=True,
        device_model="Emoji Bot Client",
        system_version="The Best Emoji Bot",
        app_version="v1.0.0",
    )
    register_all_handlers(client)
    try:
        client.run()
    except BaseException:
        revoke_session(int(telegram_id))
