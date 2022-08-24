#!/usr/bin/python

import sys

import loguru
from pyrogram import Client, filters, types
from pyrogram.handlers import MessageHandler

from commands import stupid


def main():
    string_session = sys.argv[1]
    telegram_id = sys.argv[2]

    client = Client(
        name=telegram_id,
        session_string=string_session,
        in_memory=True,
    )
    client.add_handler(MessageHandler(stupid, filters=(filters.me and filters.command("stupid", "."))))
    client.run()


if __name__ == "__main__":
    main()
