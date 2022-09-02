from contextlib import suppress

from aiogram import Dispatcher, Bot, types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from telegram_bot.database.methods import check_admin, set_admin, get_all_users
from telegram_bot.misc.states import AdminStates
from telegram_bot.keyboards import KB_ADMIN
from telegram_bot.env import TgBot
from telegram_bot.misc.util import get_main_keyboard


async def __admin_auth(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    if user_id == TgBot.ADMIN_ID:
        set_admin(user_id)
        await bot.send_message(user_id, "Добро пожаловать хозяин!")


async def __admin(msg: Message, state: FSMContext):
    bot = msg.bot
    user_id = msg.from_user.id
    if check_admin(user_id):
        await state.set_state(AdminStates.ADMIN)
        await bot.send_message(user_id, 'Вы админ', reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(user_id, 'Админ панель', reply_markup=KB_ADMIN)


async def __exit_admin(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы вышли из состояния администратора",
                           reply_markup=get_main_keyboard(user_id, False))


async def __cancel(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.set_state(AdminStates.ADMIN)
    await bot.send_message(user_id, "Действие отменено")
    await bot.send_message(user_id, "Админ панель", reply_markup=KB_ADMIN)


# region Add admin

async def __add_admin(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Введите telegram_id нового админа:\n /cancel")
    await state.set_state(AdminStates.AddAdmin.INSERT_NEW_ADMIN)


async def __insert_tg_id(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    # todo remove Exception
    try:
        set_admin(msg.text)
        await bot.send_message(int(msg.text), "Вас назначили администратором.\n"
                                              "Вот команда для получения админ панели - /admin")
        await bot.send_message(user_id, "Админка выдана", reply_markup=KB_ADMIN)
    except Exception:
        await bot.send_message(msg.from_user.id, "Админка не выдана. Произошел сбой")
        await bot.send_message(user_id, 'Админ панель', reply_markup=KB_ADMIN)
    await state.set_state(AdminStates.ADMIN)


# endregion

# region Advert

async def __advertising(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Введите текст для рассылки:\n /cancel")
    await state.set_state(AdminStates.Advertising.INSERT_ADVERT_TEXT)


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
    await bot.send_message(user_id, 'Админ панель', reply_markup=KB_ADMIN)

# endregion


def register_admin_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__admin_auth, commands=['admin'], state=None)
    dp.register_message_handler(__cancel, commands=['cancel'], state=[
        AdminStates.AddAdmin.INSERT_NEW_ADMIN,
        AdminStates.Advertising.INSERT_ADVERT_TEXT
    ])

    dp.register_message_handler(__admin, content_types=['text'], text='Admin', state=None)

    dp.register_callback_query_handler(__add_admin, lambda c: c.data == "add_admin", state=AdminStates.ADMIN)
    dp.register_message_handler(__insert_tg_id, content_types=['text'], state=AdminStates.AddAdmin.INSERT_NEW_ADMIN)

    dp.register_callback_query_handler(__advertising, lambda c: c.data == "advertising", state=AdminStates.ADMIN)
    dp.register_message_handler(__do_advertising, content_types=['text'],
                                state=AdminStates.Advertising.INSERT_ADVERT_TEXT)

    dp.register_callback_query_handler(__exit_admin, lambda c: c.data == "admin_exit", state=AdminStates.ADMIN)

