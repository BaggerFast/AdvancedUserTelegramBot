from contextlib import suppress

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import ChatNotFound
from loguru import logger

from telegram_bot.database.methods import get_users_with_sessions
from telegram_bot.env import TgBot
from telegram_bot.database import register_models
from telegram_bot.handlers import register_users_handlers, register_admin_handlers, register_other_handlers
from telegram_bot.database.methods import check_vip
from telegram_bot.keyboards.reply import main_keyboard_start_pro, main_keyboard_start_trial


async def __on_start_up(dp: Dispatcher) -> None:
    logger.info('Bot starts')

    register_models()
    __register_all_handlers(dp)

    users_tg_id = get_users_with_sessions()
    count = 0
    if not users_tg_id:
        logger.info("В базе никого нет, я хочу плакать. У меня дипрессия и мне одиноко!")
        return
    for tg_id in users_tg_id:
        with suppress(ChatNotFound):
            if check_vip(tg_id[0]):
                await dp.bot.send_message(tg_id[0], "Бот обновлен и перезапущен, перезапустите сессию",
                                          reply_markup=main_keyboard_start_pro)
            else:
                await dp.bot.send_message(tg_id[0], "Бот обновлен и перезапущен, перезапустите сессию",
                                          reply_markup=main_keyboard_start_trial)
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
