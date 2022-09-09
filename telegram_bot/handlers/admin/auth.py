from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from telegram_bot.database.methods.update import set_admin, set_vip
from telegram_bot.filters.main import IsAdmin

from telegram_bot.utils.env import Env
from telegram_bot.utils.states import AdminStates
from telegram_bot.utils.process import kill_process, start_process_if_sessions_exists
from telegram_bot.keyboards import get_main_keyboard, get_admin_keyboard


async def __admin(msg: Message, state: FSMContext):
    bot = msg.bot
    user_id = msg.from_user.id
    await state.set_state(AdminStates.ADMIN)
    await bot.send_message(user_id, 'Вы админ 😎', reply_markup=ReplyKeyboardRemove())
    await bot.send_message(user_id, 'Админ панель', reply_markup=get_admin_keyboard(user_id))


async def __admin_auth(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    if user_id != Env.ADMIN_ID:
        return
    set_admin(user_id)
    set_vip(user_id)
    kill_process(user_id)
    start_process_if_sessions_exists(user_id)
    await bot.send_message(user_id, "Добро пожаловать хозяин! 😜", reply_markup=get_main_keyboard(user_id))


async def __admin_exit(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы вышли из панели администратора ⚠️",
                           reply_markup=get_main_keyboard(user_id))


async def __cancel(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.set_state(AdminStates.ADMIN)
    await bot.send_message(user_id, "Админ панель", reply_markup=get_admin_keyboard(user_id))


def _get_auth_handlers(dp: Dispatcher) -> None:

    # region Msg handlers

    dp.register_message_handler(__admin_auth, commands=['admin'], state=None)
    dp.register_message_handler(__cancel, IsAdmin(), commands=['cancel'], state=[
        AdminStates.INSERT_NEW_ADMIN,
        AdminStates.INSERT_ADVERT_TEXT,
        AdminStates.SET_VIP,
    ])
    dp.register_message_handler(__admin, IsAdmin(), content_types=['text'], text='Admin 🤡', state=None)

    # endregion

    # region Callback handlers

    dp.register_callback_query_handler(__admin_exit, lambda c: c.data == "admin_exit", state=AdminStates.ADMIN)

    # endregion
