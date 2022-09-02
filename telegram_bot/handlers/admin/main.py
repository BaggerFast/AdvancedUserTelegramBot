from contextlib import suppress
from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from telegram_bot.database.methods.get import get_all_users
from telegram_bot.database.methods.update import set_admin, set_vip
from telegram_bot.handlers.admin.auth import _get_auth_handlers
from telegram_bot.handlers.admin.vip import _get_vip_handlers
from telegram_bot.misc.states import AdminStates
from telegram_bot.misc.util import get_main_keyboard, get_admin_keyboard


# region Add admin

async def __add_admin(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Введите telegram_id нового админа:\n /cancel")
    await state.set_state(AdminStates.INSERT_NEW_ADMIN)


async def __admin_insert_tg_id(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    admin_id = int(msg.text)
    # todo remove Exception
    try:
        set_admin(admin_id)
        set_vip(admin_id)
        await state.finish()
        await bot.send_message(admin_id, "Вас назначили администратором.\n",
                               reply_markup=get_main_keyboard(admin_id, False))
        await bot.send_message(user_id, "Успешно")
    except Exception:
        await bot.send_message(user_id, "Админка не выдана. Произошел сбой")
    await bot.send_message(user_id, 'Админ панель', reply_markup=get_admin_keyboard(user_id))
    await state.set_state(AdminStates.ADMIN)


# endregion

# region Advert

async def __advertising(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Введите текст для рассылки:\n /cancel")
    await state.set_state(AdminStates.INSERT_ADVERT_TEXT)


async def __do_advertising(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    users = get_all_users()
    count = 0
    for user in users:
        # todo: remove Exception (ни разу не писал боту или добавил его в бан)
        with suppress(Exception):
            if user_id == user[0]:
                continue
            await bot.send_message(user[0], msg.text)
            count += 1
    await state.set_state(AdminStates.ADMIN)
    await bot.send_message(user_id, f"Рассылка выполнена - у {count} пользователей")
    await bot.send_message(user_id, 'Админ панель', reply_markup=get_admin_keyboard(user_id))


# endregion


def register_admin_handlers(dp: Dispatcher) -> None:
    _get_auth_handlers(dp)
    _get_vip_handlers(dp)

    dp.register_callback_query_handler(__add_admin, lambda c: c.data == "add_admin", state=AdminStates.ADMIN)
    dp.register_message_handler(__admin_insert_tg_id, content_types=['text'], state=AdminStates.INSERT_NEW_ADMIN)

    dp.register_callback_query_handler(__advertising, lambda c: c.data == "advertising", state=AdminStates.ADMIN)
    dp.register_message_handler(__do_advertising, content_types=['text'], state=AdminStates.INSERT_ADVERT_TEXT)
