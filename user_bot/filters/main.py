from pyrogram import filters

from user_bot.utils import UserConfig


def get_filter(command: str) -> bool:
    return filters.me & filters.command(command, UserConfig.PREFIX)

