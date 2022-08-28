from pyrogram import filters


def get_me_filters(command: str) -> bool:
    return filters.me and filters.command(command, ".")
