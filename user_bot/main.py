import sys
from pyrogram import Client
from user_bot.handlers import get_common_handlers, get_vip_handlers


def __register_all_handlers(client: Client) -> None:
    handlers = (
        *get_common_handlers(),
        *get_vip_handlers(),
    )
    for handler in handlers:
        client.add_handler(handler)


def start_user_bot() -> None:
    string_session = sys.argv[1]
    telegram_id = sys.argv[2]
    client = Client(
        name=telegram_id,
        session_string=string_session,
        in_memory=True,
    )
    __register_all_handlers(client)
    client.run()
