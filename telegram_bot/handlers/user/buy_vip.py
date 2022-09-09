from uuid import uuid4

from yookassa import Payment
from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery

from misc.html_tags import b
from telegram_bot.database.methods.update import set_vip
from telegram_bot.database.methods.create import create_user_payment
from telegram_bot.database.methods.get import get_user_by_telegram_id
from telegram_bot.filters.main import NotAdmin, NotVip

from telegram_bot.utils.util import get_payment_info
from telegram_bot.handlers.user.util import _buy_vip_text
from telegram_bot.utils.process import kill_process, start_process_if_sessions_exists
from telegram_bot.keyboards import get_main_keyboard, get_payment_keyboard


async def __buy_vip(msg: Message) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    user = get_user_by_telegram_id(user_id)

    if user and not user.payment:
        payment = Payment.create(get_payment_info(), uuid4())
        create_user_payment(user, payment.id)
    else:
        payment = Payment.find_one(user.payment.key)
    if payment.status != 'succeeded':
        keyboard = get_payment_keyboard(payment.confirmation.confirmation_url)
        await bot.send_message(user_id, _buy_vip_text(), reply_markup=keyboard)
    else:
        keyboard = get_payment_keyboard()
        await bot.send_message(user_id, f"{b('VIP')} доступ уже оплачен. Проверьте оплату", reply_markup=keyboard)


async def __check_buy(query: CallbackQuery) -> None:
    bot: Bot = query.bot
    user_id = query.from_user.id
    user = get_user_by_telegram_id(user_id)

    payment = Payment.find_one(user.payment.key)
    if payment.status == 'succeeded':
        set_vip(user_id)
        kill_process(user_id)
        start_process_if_sessions_exists(user_id)
        await bot.send_message(user_id, "Вы успешно оформили вип доступ!🥳\n", reply_markup=get_main_keyboard(user_id))
    else:
        await query.answer("Оплата еще не проведена!\n", cache_time=0)


def _register_vip_handlers(dp: Dispatcher) -> None:

    # region Msg handlers

    dp.register_message_handler(__buy_vip, NotAdmin(), NotVip(), content_types=['text'], text="Купить полную версию 💸")

    # endregion

    # region Callback handlers

    dp.register_callback_query_handler(__check_buy, text_contains="check_payment")

    # endregion
