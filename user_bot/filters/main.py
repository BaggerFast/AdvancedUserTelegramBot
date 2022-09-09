from pyrogram import filters
from pyrogram.types.messages_and_media.message import Message

from user_bot.utils import UserConfig


def is_vip_filter():
    async def func(_, __, msg: Message):
        return UserConfig.VIP_STATUS
    return filters.create(func)


def get_free_filters(command: str) -> bool:
    return filters.me & filters.command(command, UserConfig.PREFIX)


def get_vip_filters(command: str) -> bool:
    return is_vip_filter() & get_free_filters(command)
