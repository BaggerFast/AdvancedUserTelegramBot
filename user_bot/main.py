#!/usr/bin/python
import sys
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from commands import stupid, bombs, kill, night


def main():
    string_session = sys.argv[1]
    telegram_id = sys.argv[2]
    vip_status = int(sys.argv[3])

    client = Client(
        name=telegram_id,
        session_string=string_session,
        in_memory=True,
    )
    handlers = (
        MessageHandler(stupid, filters=(filters.me and filters.command("stupid", "."))),
        MessageHandler(bombs, filters=(filters.me and filters.command("bombs", "."))),
        MessageHandler(kill, filters=(filters.me and filters.command("kill", "."))),
        MessageHandler(night, filters=(filters.me and filters.command("filter", "."))),
    )

    for handler in handlers:
        client.add_handler(handler)

    if vip_status:
        vip_handlers = ()
        for handler in vip_handlers:
            client.add_handler(handler)

    client.run()


if __name__ == "__main__":
    main()
