from aiogram import Bot, Dispatcher, executor
from loguru import logger

from telegram_bot.bot import TgBot
from telegram_bot.bot.handlers import *
from telegram_bot.bot.database import register_models


def register_all_handlers(dp: Dispatcher) -> None:
    register_admin_handlers(dp)
    register_users_handlers(dp)
    register_other_handlers(dp)


def start_telegram_bot():
    bot = Bot(token=TgBot.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)
    register_all_handlers(dp)
    register_models()
    logger.info('Bot starts')
    executor.start_polling(dp, skip_updates=True)
