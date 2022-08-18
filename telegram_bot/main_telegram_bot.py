from aiogram import Bot, Dispatcher, executor
from loguru import logger

from bot import TgBot
from bot.handlers import *
from bot.database import register_models


def register_all_handlers(dp: Dispatcher) -> None:
    register_admin_handlers(dp)
    register_users_handlers(dp)
    register_other_handlers(dp)


def start_telegram_bot():
    bot = Bot(token=TgBot.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)
    register_all_handlers(dp)
    register_models()
    logger.info('Bot start')
    executor.start_polling(dp, skip_updates=True)


