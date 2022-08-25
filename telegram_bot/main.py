from contextlib import suppress

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import ChatNotFound
from loguru import logger
from sqlalchemy import select

from telegram_bot.bot.database.main_database import Database
from telegram_bot.bot.database.models import Session, User
from .bot import TgBot
from .bot.database import register_models
from .bot.handlers import register_users_handlers, register_admin_handlers, register_other_handlers


async def __on_start_up(dp: Dispatcher):
    logger.info('Bot starts')
    register_models()
    __register_all_handlers(dp)

    # todo better
    select_query = select(User.telegram_id).where(User.session)
    users_tg_id = Database().session.execute(select_query).fetchone()
    count = 0
    for tg_id in users_tg_id:
        with suppress(ChatNotFound):
            await dp.bot.send_message(tg_id, "Бот обновлен и перезапущен, перезапустите сессию")
            count += 1
    logger.info(f"Было совершено {count} рассылок")


def __register_all_handlers(dp: Dispatcher) -> None:
    register_admin_handlers(dp)
    register_users_handlers(dp)
    register_other_handlers(dp)


def start_telegram_bot() -> None:
    bot = Bot(token=TgBot.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)


if __name__ == "__main__":
    start_telegram_bot()
