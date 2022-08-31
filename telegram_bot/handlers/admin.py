from contextlib import suppress

from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from telegram_bot.database.methods import check_admin, set_admin, get_all_users
from telegram_bot.misc.states import AdminStates
from telegram_bot.keyboards import admin_keyboard
from telegram_bot.env import TgBot


async def __admin_auth(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    is_admin = check_admin(msg.from_user.id)
    if is_admin:
        await state.set_state(AdminStates.ADMIN)
        await bot.send_message(msg.from_user.id, "Админ панель", reply_markup=admin_keyboard)
    elif msg.from_user.id == TgBot.ADMIN_ID:
        set_admin(msg.from_user.id)
        await state.set_state(AdminStates.ADMIN)
        await bot.send_message(msg.from_user.id, "Админ панель", reply_markup=admin_keyboard)


async def __add_admin(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Введите telegram_id нового админа:")
    await state.set_state(AdminStates.AddAdmin.INSERT_NEW_ADMIN)


async def __insert_tgid(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    with suppress(Exception):
        set_admin(msg.text)
        await bot.send_message(int(msg.text), "Вас назначили администратором.\n"
                                              "Вот команда для получения админ панели - /admin")
    await bot.send_message(msg.from_user.id, "Админка должна быть выдана")
    await state.set_state(AdminStates.ADMIN)


async def __advertising(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Введите текст для рассылки: ")
    await state.set_state(AdminStates.Advertising.INSERT_ADVERT_TEXT)


async def __do_advertising(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    users = get_all_users()
    for user in users:
        with suppress(Exception):
            await bot.send_message(user[0], msg.text)
    await state.set_state(AdminStates.ADMIN)
    await bot.send_message(msg.from_user.id, "Рассылка выполнена")


async def __exit_admin(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    await state.finish()
    await bot.send_message(msg.from_user.id, "Вы вышли из состояния администратора")


async def __cancel(msg: Message, state: FSMContext):
    bot: Bot = msg.bot
    await state.set_state(AdminStates.ADMIN)
    await bot.send_message(msg.from_user.id, "Отменено")
    await bot.send_message(msg.from_user.id, "Админ панель", reply_markup=admin_keyboard)


def register_admin_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__admin_auth, commands=['admin'], state=None)
    dp.register_callback_query_handler(__add_admin, lambda c: c.data == "add_admin", state=AdminStates.ADMIN)
    dp.register_message_handler(__cancel, commands=['cancel'], state=[AdminStates.AddAdmin.INSERT_NEW_ADMIN,
                                                                      AdminStates.Advertising.INSERT_ADVERT_TEXT])
    dp.register_message_handler(__insert_tgid, content_types=['text'], state=AdminStates.AddAdmin.INSERT_NEW_ADMIN)
    dp.register_callback_query_handler(__advertising, lambda c: c.data == "advertising", state=AdminStates.ADMIN)
    dp.register_message_handler(__do_advertising, content_types=['text'],
                                state=AdminStates.Advertising.INSERT_ADVERT_TEXT)
    dp.register_callback_query_handler(__exit_admin, lambda c: c.data == "exit", state=AdminStates.ADMIN)
