#!/usr/bin/python
from loguru import logger

from misc.path import PathManager
from telegram_bot import start_telegram_bot


def main():
    log_path = PathManager.get('logs/debug.log')
    logger.add(log_path, format="{time} {level} {message}", level="DEBUG", rotation="10:00", compression="zip")
    start_telegram_bot()


if __name__ == '__main__':
    main()
