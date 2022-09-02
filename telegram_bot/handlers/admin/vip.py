from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from telegram_bot.database.methods import set_vip, switch_vip
from telegram_bot.misc.states import AdminStates
from telegram_bot.misc.util import get_main_keyboard, get_admin_keyboard


async def __vip_switcher(msg: CallbackQuery, state: FSMContext):
    user_id = msg.from_user.id
    switch_vip(user_id)
    await msg.message.edit_reply_markup(get_admin_keyboard(user_id))


async def __set_vip(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Введите telegram_id человека:\n /cancel")
    await state.set_state(AdminStates.SET_VIP)


async def __vip_insert_tg_id(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    other_user_id = int(msg.text)
    # todo remove Exception
    try:
        set_vip(other_user_id)
        await state.finish()
        await bot.send_message(other_user_id, "Вам выдали vip доступ.",
                               reply_markup=get_main_keyboard(other_user_id, False))
        await bot.send_message(user_id, "Успешно")
    except Exception:
        await bot.send_message(user_id, "Произошел сбой")
    await bot.send_message(user_id, 'Админ панель', reply_markup=get_admin_keyboard(user_id))
    await state.set_state(AdminStates.ADMIN)


def _get_vip_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(__vip_switcher, lambda c: c.data == "vip_switcher", state=AdminStates.ADMIN)
    dp.register_callback_query_handler(__set_vip, lambda c: c.data == "give_vip", state=AdminStates.ADMIN)
    dp.register_message_handler(__vip_insert_tg_id, content_types=['text'], state=AdminStates.SET_VIP)
