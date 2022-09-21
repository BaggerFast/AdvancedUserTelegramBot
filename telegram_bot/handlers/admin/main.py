from contextlib import suppress

import loguru

from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from telegram_bot.database.methods.update import set_admin, set_vip
from telegram_bot.database.methods.get import get_all_telegram_id, get_sessions_enable_count, get_user_count, \
    get_sessions_count
from telegram_bot.filters.main import IsAdmin

from telegram_bot.handlers.admin.vip import _get_vip_handlers
from telegram_bot.handlers.admin.auth import _get_auth_handlers

from telegram_bot.utils.states import AdminStates
from telegram_bot.utils.process import kill_process, start_process_if_sessions_exists
from telegram_bot.keyboards import get_main_keyboard, get_admin_keyboard


# region Add admin

async def __add_admin(query: CallbackQuery, state: FSMContext):
    bot: Bot = query.bot
    await bot.send_message(query.from_user.id, "Введите telegram_id нового админа:\n /cancel")
    await state.set_state(AdminStates.INSERT_NEW_ADMIN)


async def __admin_insert_tg_id(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    admin_id = int(msg.text)
    try:
        set_admin(admin_id)
        set_vip(admin_id)
        kill_process(admin_id)
        start_process_if_sessions_exists(admin_id)
        await state.finish()
        await bot.send_message(admin_id, "Вас назначили администратором.🥳\n", reply_markup=get_main_keyboard(admin_id))
        await bot.send_message(user_id, "Успешно: выдана ADMIN доступ ✅")
        loguru.logger.info(f'{admin_id} got ADMIN access from {user_id}')
    except Exception:
        await bot.send_message(user_id, "Админка не выдана. Произошел сбой ⚠️")
    await bot.send_message(user_id, 'Админ панель', reply_markup=get_admin_keyboard(user_id))
    await state.set_state(AdminStates.ADMIN)


# endregion

# region Advert

async def __advertising(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Введите текст для рассылки:\n /cancel")
    await state.set_state(AdminStates.INSERT_ADVERT_TEXT)


async def __do_advertising(query: Message, state: FSMContext):
    bot: Bot = query.bot
    user_id = query.from_user.id
    users = get_all_telegram_id()
    count = 0
    for user in users:
        # todo: remove Exception (ни разу не писал боту или добавил его в бан)
        with suppress(Exception):
            if user_id == user[0]:
                continue
            await bot.send_message(user[0], query.text)
            count += 1
    await state.set_state(AdminStates.ADMIN)
    await bot.send_message(user_id, f"Рассылка выполнена - у {count} пользователей ✅")
    await bot.send_message(user_id, 'Админ панель', reply_markup=get_admin_keyboard(user_id))


# endregion


async def __analytic(query: CallbackQuery, state: FSMContext) -> None:
    users_count = get_user_count()
    user_session_count = get_sessions_count()
    vip_session_enable_count = get_sessions_enable_count(True)
    free_session_enable_count = get_sessions_enable_count(False)
    session_enable_count = vip_session_enable_count + free_session_enable_count

    text = (
        'Отчет:\n',
        f'Кол-во пользователей: {users_count}',
        f'Кол-во сессий: {user_session_count}\n',
        f'VIP онлайн: {vip_session_enable_count}',
        f'Free онлайн: {free_session_enable_count}',
        f'Total онлайн: {session_enable_count}',
    )
    await query.answer('\n'.join(text), show_alert=True, cache_time=0)


def register_admin_handlers(dp: Dispatcher) -> None:
    # region Msg handlers

    dp.register_message_handler(__admin_insert_tg_id, IsAdmin(), content_types=['text'],
                                state=AdminStates.INSERT_NEW_ADMIN)

    dp.register_message_handler(__do_advertising, IsAdmin(), content_types=['text'],
                                state=AdminStates.INSERT_ADVERT_TEXT)

    # endregion

    # region Callback handlers

    dp.register_callback_query_handler(__analytic, IsAdmin(), lambda c: c.data == "analytics",
                                       state=AdminStates.ADMIN)
    dp.register_callback_query_handler(__add_admin, IsAdmin(), lambda c: c.data == "add_admin",
                                       state=AdminStates.ADMIN)
    dp.register_callback_query_handler(__advertising, IsAdmin(), lambda c: c.data == "advertising",
                                       state=AdminStates.ADMIN)

    # endregion

    _get_auth_handlers(dp)
    _get_vip_handlers(dp)
