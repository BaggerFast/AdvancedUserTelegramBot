from aiogram import Dispatcher
from aiogram.dispatcher.filters import Filter
from aiogram.types import Message

from telegram_bot.database.methods.other import is_admin


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, message: Message) -> bool:
        return is_admin(message.from_user.id)


class NotAdmin(Filter):
    key = "not_admin"

    async def check(self, message: Message) -> bool:
        return False if is_admin(message.from_user.id) else True


def register_all_filters(dp: Dispatcher):
    filters = (
        NotAdmin,
        IsAdmin,
    )
    for filter in filters:
        dp.bind_filter(filter)
