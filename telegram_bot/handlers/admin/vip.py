from loguru import logger

from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from telegram_bot.database.methods.update import set_vip
from telegram_bot.database.methods.other import switch_vip
from telegram_bot.filters.main import IsAdmin

from telegram_bot.utils.states import AdminStates
from telegram_bot.keyboards import get_main_keyboard, get_admin_keyboard
from telegram_bot.utils.process import kill_process, start_process_if_sessions_exists, check_process


async def __vip_switcher(query: CallbackQuery, state: FSMContext):
    user_id = query.from_user.id
    switch_vip(user_id)
    kill_process(user_id)
    start_process_if_sessions_exists(user_id)
    await query.message.edit_reply_markup(get_admin_keyboard(user_id))


async def __set_vip(query: CallbackQuery, state: FSMContext):
    bot: Bot = query.bot
    await bot.send_message(query.from_user.id, "Введите telegram_id человека:\n /cancel")
    await state.set_state(AdminStates.SET_VIP)


async def __vip_insert_tg_id(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    other_user_id = int(msg.text)
    # todo remove Exception`
    try:
        set_vip(other_user_id)
        if check_process(user_id):
            kill_process(user_id)
            start_process_if_sessions_exists(user_id)
        await state.finish()
        await bot.send_message(other_user_id, "Администратор выдал вам vip доступ. ✨",
                               reply_markup=get_main_keyboard(other_user_id))
        await bot.send_message(user_id, "Успешно: выдан VIP доступ ✅")
        logger.info(f'{other_user_id} got VIP access from {user_id}')
    except Exception as e:
        logger.critical(e)
        await bot.send_message(user_id, "Произошел сбой ⚠️")
    await bot.send_message(user_id, 'Админ панель', reply_markup=get_admin_keyboard(user_id))
    await state.set_state(AdminStates.ADMIN)


def _get_vip_handlers(dp: Dispatcher) -> None:

    # region Msg handlers

    dp.register_message_handler(__vip_insert_tg_id, IsAdmin(), content_types=['text'], state=AdminStates.SET_VIP)

    # endregion

    # region Callback handlers

    dp.register_callback_query_handler(__vip_switcher, IsAdmin(),
                                       lambda c: c.data == "vip_switcher", state=AdminStates.ADMIN)
    dp.register_callback_query_handler(__set_vip, IsAdmin(),
                                       lambda c: c.data == "give_vip", state=AdminStates.ADMIN)

    # endregion
