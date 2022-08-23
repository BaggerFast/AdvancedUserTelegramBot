from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger

from .bot import TgBot
from .bot.database import register_models
from .bot.handlers import register_users_handlers, register_admin_handlers, register_other_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    register_admin_handlers(dp)
    register_users_handlers(dp)
    register_other_handlers(dp)


def start_telegram_bot() -> None:
    bot = Bot(token=TgBot.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_models()
    register_all_handlers(dp)
    logger.info('Bot starts')
    executor.start_polling(dp, skip_updates=True)
