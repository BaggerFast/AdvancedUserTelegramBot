#!/usr/bin/python

import sys
import loguru
from telethon import TelegramClient
from user_bot.commands import on_he, make_dick


def main():
    try:
        api_id = int(sys.argv[1])
        api_hash = str(sys.argv[2])
        phone = str(sys.argv[3])
        auth_code = int(sys.argv[4])
        telegram_id = int(sys.argv[5])

        client = TelegramClient(f"{telegram_id}", api_id, api_hash)

        client.add_event_handler(on_he)
        client.add_event_handler(make_dick)

        client.start(phone=phone, code_callback=lambda: auth_code)
        client.run_until_disconnected()
    except Exception as e:
        loguru.logger.add("logs.txt")
        loguru.logger.error(e)


if __name__ == "__main__":
    main()
