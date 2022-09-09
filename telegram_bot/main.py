from contextlib import suppress

from loguru import logger

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import ChatNotFound, BotBlocked

from telegram_bot.database import register_models
from telegram_bot.database.methods.get import get_users_with_sessions
from telegram_bot.filters import register_all_filters

from telegram_bot.utils import Env
from telegram_bot.keyboards import get_main_keyboard
from telegram_bot.handlers import register_all_handlers
from telegram_bot.utils.process import start_process_if_sessions_exists


async def __on_start_up(dp: Dispatcher) -> None:
    logger.info('Bot starts')

    register_models()
    register_all_filters(dp)
    register_all_handlers(dp)

    users = get_users_with_sessions()
    count = 0

    if not users:
        return

    for user in users:
        with suppress(ChatNotFound, BotBlocked):
            if user.session.enable:
                start_process_if_sessions_exists(user.telegram_id)
            await dp.bot.send_message(user.telegram_id, "Бот обновлен!",
                                      reply_markup=get_main_keyboard(user.telegram_id))
            count += 1

    logger.info(f"Было совершено {count} рассылок")


def start_telegram_bot() -> None:
    bot = Bot(token=Env.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
