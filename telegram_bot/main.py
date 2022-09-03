from contextlib import suppress

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import ChatNotFound, BotBlocked
from loguru import logger

from telegram_bot.database.methods.get import get_users_with_sessions
from telegram_bot.utils.env import Env
from telegram_bot.database import register_models
from telegram_bot.handlers import register_users_handlers, register_admin_handlers, register_other_handlers
from telegram_bot.utils.util import get_main_keyboard


async def __on_start_up(dp: Dispatcher) -> None:
    logger.info('Bot starts')

    register_models()
    __register_all_handlers(dp)

    users = get_users_with_sessions()
    count = 0

    if not users:
        logger.info("В базе никого нет, я хочу плакать. У меня дипрессия и мне одиноко!")
        return

    for key in users:
        usr = key
        with suppress(ChatNotFound, BotBlocked):
            await dp.bot.send_message(
                usr.telegram_id,
                "Бот обновлен, запустите его заново! ⚠️",
                reply_markup=get_main_keyboard(usr.telegram_id)
            )
            count += 1
    logger.info(f"Было совершено {count} рассылок")


def __register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_admin_handlers,
        register_users_handlers,
        register_other_handlers
    )
    for handler in handlers:
        handler(dp)


def start_telegram_bot() -> None:
    bot = Bot(token=Env.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)


if __name__ == "__main__":
    start_telegram_bot()
