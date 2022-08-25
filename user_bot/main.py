#!/usr/bin/python
import sys
from pyrogram import Client
from user_bot.handlers import get_common_handlers, get_vip_handlers


def __register_all_handlers(client: Client, vip: bool) -> None:
    handlers = []
    handlers.extend(get_common_handlers())
    handlers.extend(get_vip_handlers(vip))
    for handler in handlers:
        client.add_handler(handler)


def main():
    string_session = sys.argv[1]
    telegram_id = sys.argv[2]
    vip_status = bool(int(sys.argv[3]))
    client = Client(
        name=telegram_id,
        session_string=string_session,
        in_memory=True,
    )
    __register_all_handlers(client, vip_status)
    client.run()


if __name__ == "__main__":
    main()
