import uuid

from aiogram import Dispatcher, Bot
from aiogram.types import PreCheckoutQuery, ContentTypes, Message, LabeledPrice
from loguru import logger
from yookassa import Payment

from telegram_bot.database.main import Database
from telegram_bot.database.methods.create import create_user_payment
from telegram_bot.database.methods.get import get_user_by_telegram_id
from telegram_bot.database.methods.other import is_admin
from telegram_bot.database.methods.update import set_vip
from telegram_bot.utils import Env, TgConfig
from telegram_bot.utils.process import kill_process, start_process_if_sessions_exists
from telegram_bot.utils.util import get_main_keyboard, get_payment_keyboard, get_payment_info


async def __buy_vip(msg: Message) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    user = get_user_by_telegram_id(user_id)
    if user.vip:
        await bot.send_message(user_id, 'Вы уже приобрели vip доступ')
    if user.admin:
        await bot.send_message(user_id, 'Вы являетесь администратором, используйте настройку в Админ меню')
        return
    if user and not user.payment:
        create_user_payment(user, str(uuid.uuid4()))
    payment = Payment.create(get_payment_info(), user.payment.key)
    if  payment.status != 'succeeded':
        keyboard = get_payment_keyboard(payment.confirmation.confirmation_url)
        await bot.send_message(user_id, f'Вы приобретаете <b>VIP</b> доступ.\nК оплате <b>{TgConfig.PRICE}</b> рублей',
                                   reply_markup=keyboard)
        return
    keyboard = get_payment_keyboard('https://github.com/Bagger-sTeam')
    await bot.send_message(user_id, f'Вы приобретаете <b>VIP</b> доступ.\nК оплате <b>{TgConfig.PRICE}</b> рублей',
                           reply_markup=keyboard)


async def __check_buy(msg: Message) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    user = get_user_by_telegram_id(user_id)
    payment_status = Payment.find_one(user.payment.key)
    if payment_status == 'succeeded':
        set_vip(user_id)
        kill_process(user_id)
        start_process_if_sessions_exists(user_id)
        await bot.send_message(user_id, "Вы успешно оформили вип доступ!🥳\n", reply_markup=get_main_keyboard(user_id))
    else:
        await bot.send_message(user_id, "Оплата еще не проведена!\n")


def _register_vip_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__buy_vip, content_types=['text'], text="Купить полную версию 💸")
    dp.register_callback_query_handler(__check_buy, lambda c: c.data == "check_payment")
