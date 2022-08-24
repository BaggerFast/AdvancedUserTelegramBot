import datetime

import loguru
from pyrogram import Client
from pyrogram.errors import FloodWait, PhoneCodeInvalid, SessionPasswordNeeded
from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import LabeledPrice, PreCheckoutQuery, ContentTypes, Message

from telegram_bot.bot import TgBot
from telegram_bot.bot.misc import CreateUserBotState, start_user_bot
from telegram_bot.bot.keyboards import main_keyboard_start_pro, main_keyboard_start_trial, me_telegram_keyboard
from telegram_bot.bot.database.methods import create_user, check_vip, set_vip, create_user_bot_session, \
    get_user_by_id_telegram_id

sessions = {}


async def start(msg: Message) -> None:
    create_user(msg.from_user.id)
    bot: Bot = msg.bot
    if check_vip(msg.from_user.id):
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_pro)
    else:
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_trial)


# region User setup

async def start_input_user_settings(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    user = get_user_by_id_telegram_id(user_id)
    if user:
        if user.session:
            start_user_bot(user.session.session, msg.from_user.id)
            await state.finish()
            await bot.send_message(msg.from_user.id, "Ваш прошлый сеанс ещё активен!")
            return
    else:
        create_user(user_id)
    await bot.send_message(user_id, 'Узнать данные можно 👇', reply_markup=me_telegram_keyboard)
    await bot.send_message(user_id, "Введите ваш api-id:")
    await state.set_state(CreateUserBotState.API_ID)


async def input_api_id(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    if msg.text.isdigit():
        async with state.proxy() as data:
            data['write_api_id'] = int(msg.text)
    else:
        await bot.send_message(msg.from_user.id, "api-id должен состоять только из цифр! Вы где-то ошиблись!")
        return
    await bot.send_message(msg.from_user.id, "Введите api-hash:")
    await state.set_state(CreateUserBotState.API_HASH)


async def input_api_hash(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    if len(msg.text) == 32:
        async with state.proxy() as data:
            data['write_api_hash'] = msg.text
    else:
        await bot.send_message(msg.from_user.id, "api-hash должен состоять из 32 символов! Вы где-то ошиблись!")
        return
    await bot.send_message(msg.from_user.id, "Введите ваш номер телефона:")
    await state.set_state(CreateUserBotState.PHONE)


async def input_phone(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_data = await state.get_data()
    try:
        client = Client(
            name=str(msg.from_user.id),
            api_id=user_data["write_api_id"],
            api_hash=user_data["write_api_hash"],
            in_memory=True
        )
        await client.connect()
        code = await client.send_code(msg.text)

        async with state.proxy() as data:
            data['write_phone'] = msg.text
            data['code'] = code
            sessions[msg.from_user.id] = client
    except FloodWait as waitE:
        loguru.logger.error(waitE)
        await bot.send_message(msg.from_user.id, f"Не удалось отправить смс!\n"
                                                 f"Повторите попытку через - {datetime.timedelta(seconds=waitE.value)}")
        await state.finish()
        return
    await bot.send_message(msg.from_user.id, "Введите код подтверждения из телеграма: ")
    await state.set_state(CreateUserBotState.AUTH_CODE)


async def input_oauth_code(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_data = await state.get_data()

    client: Client = sessions[msg.from_user.id]
    del(sessions[msg.from_user.id])
    try:
        await client.sign_in(
            user_data['write_phone'],
            user_data['code'].phone_code_hash,
            "".join(msg.text.split())
        )
    except PhoneCodeInvalid as code_exception:
        loguru.logger.error(code_exception)
        await bot.send_message(msg.from_user.id,
                               "Неверный код!\n"
                               "Повторите авторизацию заново")
        return
    except SessionPasswordNeeded:
        await bot.send_message(msg.from_user.id, "У вас включена двух этапная аунтефикация.\n"
                                                 "Выключите её чтобы пользоваться ботом!")
        await state.finish()
        return
    loguru.logger.debug("Запускаю сабпроцесс")
    string_session = await client.export_session_string()
    user = get_user_by_id_telegram_id(msg.from_user.id)
    if user:
        create_user_bot_session(user, string_session)

    await client.disconnect()

    start_user_bot(string_session, msg.from_user.id)

    loguru.logger.debug("после сабпроцесс")

    await bot.send_message(msg.from_user.id, "User bot запущен")
    await state.finish()


# endregion


# region Vip

async def buy_vip(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="Vip",
        description="Описание",
        provider_token=TgBot.PAYMENTS_TOKEN,
        currency='rub',
        prices=[LabeledPrice(label="Vip доступ", amount=30000)],
        start_parameter='True',
        payload='some_invoice',
        protect_content=True,
    )


async def on_success_buy(msg: Message) -> None:
    bot: Bot = msg.bot
    set_vip(msg.from_user.id)
    await bot.send_message(
        msg.from_user.id,
        "Вы успешно оформили вип доступ!",
        reply_markup=main_keyboard_start_pro
    )


async def check_oup_process(check_out_query: PreCheckoutQuery) -> None:
    bot: Bot = check_out_query.bot
    await bot.answer_pre_checkout_query(check_out_query.id, ok=True)


# endregion


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])

    dp.register_message_handler(buy_vip, content_types=['text'], text="Купить полную версию")
    dp.register_message_handler(input_api_id, content_types=['text'], state=CreateUserBotState.API_ID)
    dp.register_message_handler(input_api_hash, content_types=['text'], state=CreateUserBotState.API_HASH)
    dp.register_message_handler(input_phone, content_types=['text'], state=CreateUserBotState.PHONE)
    dp.register_message_handler(input_oauth_code, content_types=['text'], state=CreateUserBotState.AUTH_CODE)

    dp.register_pre_checkout_query_handler(check_oup_process, lambda q: True)
    dp.register_message_handler(on_success_buy, content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_message_handler(start_input_user_settings, content_types=['text'], text="Подключить бота", state=None)
