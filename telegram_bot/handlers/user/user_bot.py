from datetime import timedelta
from contextlib import suppress

from loguru import logger

from pyrogram import Client
from pyrogram.errors import SessionPasswordNeeded, PhoneCodeInvalid, FloodWait, PhoneCodeExpired, PasswordHashInvalid

from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from misc.path import PathManager
from telegram_bot.database.methods.create import create_session
from telegram_bot.database.methods.delete import delete_session
from telegram_bot.database.methods.get import get_user_by_telegram_id

from telegram_bot.utils import Env, CreateUserBotState
from telegram_bot.handlers.user.util import _user_agreement_text
from telegram_bot.keyboards import KB_CONTACT, KB_CANCEL_SETUP, get_main_keyboard
from telegram_bot.utils.process import start_process_if_sessions_exists, check_process, kill_process

__sessions: dict[int, Client] = {}


# region with State


async def __input_phone(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    phone_number = msg.contact.phone_number
    with suppress(Exception):
        client = Client(
            name=str(msg.from_user.id),
            api_id=Env.API_ID,
            api_hash=Env.API_HASH,
            in_memory=True,
        )
        await client.connect()
    try:
        code = await client.send_code(phone_number)
    except FloodWait as e:
        logger.error(e)
        await bot.send_message(user_id, f"Не удалось отправить смс! ⚠️\n"
                                        f"Повторите попытку через - {timedelta(seconds=e.value)}",
                               reply_markup=get_main_keyboard(user_id))
        await state.finish()
        return

    async with state.proxy() as data:
        data['write_phone'] = phone_number
        data['code'] = code
        __sessions[user_id] = client

    await bot.send_message(user_id, "⚠️ Важно ставить тире после каждой цифры! ⚠️",
                           reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(user_id, "Введите код подтверждения из телеграмма в таком формате 0-0-0-0-0: \n",
                           reply_markup=KB_CANCEL_SETUP)
    await state.set_state(CreateUserBotState.AUTH_CODE)


async def __input_oauth_code(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    user_data = await state.get_data()
    code = "".join(msg.text.split('-'))

    client: Client = __sessions[msg.from_user.id]

    async with state.proxy() as data:
        data["auth_code"] = code

    try:
        await client.sign_in(
            user_data['write_phone'],
            user_data['code'].phone_code_hash,
            code,
        )
    except PhoneCodeInvalid as e:
        logger.error(e)
        await bot.send_message(user_id, "Неверный код!\nПовторите авторизацию заново ⚠️")
        return
    except PhoneCodeExpired as e:
        logger.error(e)
        await bot.send_message(user_id, "Код подтверждения иссек, попробуйте заново ⚠️")
        await state.finish()
        return
    except SessionPasswordNeeded as e:
        await bot.send_message(msg.from_user.id, "Введи пароль двух-этапной аунтефикации:",
                               reply_markup=KB_CANCEL_SETUP)
        await state.set_state(CreateUserBotState.TWO_FA_PASSWORD)
        return

    string_session = await client.export_session_string()

    if user := get_user_by_telegram_id(user_id):
        create_session(user, string_session)

    await client.disconnect()

    start_process_if_sessions_exists(user_id)
    del __sessions[user_id]

    keyboard = get_main_keyboard(user_id)
    await bot.send_message(user_id, "User bot запущен ✅", reply_markup=keyboard)
    await state.finish()


async def __input_2fa_password(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    client: Client = __sessions[user_id]
    try:
        await client.check_password(password=msg.text)
    except PasswordHashInvalid as e:
        await bot.send_message(user_id, "Вы ввели не верный пароль двух-этапной аунтефикации! ⚠️\n"
                                        "Введи пароль ещё раз:")
        return

    string_session = await client.export_session_string()

    if user := get_user_by_telegram_id(msg.from_user.id):
        create_session(user, string_session)

    await client.disconnect()

    start_process_if_sessions_exists(user_id)
    del __sessions[user_id]

    keyboard = get_main_keyboard(user_id)

    await msg.delete()
    await bot.send_message(user_id, "Бот запущен! ✅", reply_markup=keyboard)
    await state.finish()


async def __start_input_user_settings(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id

    user = get_user_by_telegram_id(user_id)

    if check_process(user_id):
        keyboard = get_main_keyboard(user_id)
        await bot.send_message(user_id, "Ваш бот уже запущен!", reply_markup=keyboard)
        return
    if user and user.session:
        start_process_if_sessions_exists(user_id)
        keyboard = get_main_keyboard(user_id)
        await state.finish()
        await bot.send_message(
            user_id,
            "Бот запущен! ✅\n",
            reply_markup=keyboard
        )
        return
    await bot.send_document(user_id, open(PathManager.get('UserAgreement.pdf'), 'rb'), reply_markup=KB_CONTACT)
    await bot.send_message(user_id, _user_agreement_text(msg.from_user.first_name), reply_markup=KB_CANCEL_SETUP)

    await state.set_state(CreateUserBotState.PHONE)


async def __stop_register_user_bot(query: CallbackQuery, state: FSMContext) -> None:
    bot: Bot = query.bot
    user_id = query.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Авторизация бота отменена! ❌", reply_markup=get_main_keyboard(user_id))


# endregion


async def __stop_bot(msg: Message) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id

    if check_process(user_id):
        kill_process(user_id)
        keyboard = get_main_keyboard(user_id)
        await bot.send_message(user_id, "Бот остановлен! ⚠️", reply_markup=keyboard)


async def __delete_session(msg: Message) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    delete_session(user_id)
    kill_process(user_id)
    keyboard = get_main_keyboard(user_id)
    await bot.send_message(user_id, "Ваши данные удалены и User bot остановлен! ⚠️", reply_markup=keyboard)


def _register_user_bot_handlers(dp: Dispatcher) -> None:

    # region Msg handlers

    dp.register_message_handler(__input_phone, content_types=[types.ContentType.CONTACT],
                                state=CreateUserBotState.PHONE)
    dp.register_message_handler(__input_oauth_code, content_types=['text'], state=CreateUserBotState.AUTH_CODE)
    dp.register_message_handler(__input_2fa_password, content_types=['text'], state=CreateUserBotState.TWO_FA_PASSWORD)

    dp.register_message_handler(__start_input_user_settings, content_types=['text'], text="Запустить бота ✅")
    dp.register_message_handler(__stop_bot, content_types=['text'], text="Остановить бота ❌")
    dp.register_message_handler(__delete_session, content_types=['text'], text="Удалить свои данные ⚠️")

    # endregion

    # region Callback handlers

    dp.register_callback_query_handler(__stop_register_user_bot, lambda c: c.data == "cancel_setup", state="*")

    # endregion
