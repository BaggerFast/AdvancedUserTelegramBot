import os

from aiogram import types, Dispatcher, Bot
from aiogram.types import LabeledPrice, PreCheckoutQuery, ContentTypes
from aiogram.dispatcher import FSMContext

from telegram_bot.bot.database.methods import add_user, check_vip, set_vip
from telegram_bot.bot.keyboards import main_keyboard_start_pro, main_keyboard_start_trial
from telegram_bot.bot import TgBot
from telegram_bot.bot.keyboards.inline import me_telegram_keyboard
from telegram_bot.bot.misc import StartUserBot


async def start(msg: types.Message) -> None:
    add_user(msg.from_user.id)
    bot: Bot = msg.bot
    if check_vip(msg.from_user.id):
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_pro)
    else:
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_trial)


# region User setup

async def start_input_user_settings(msg: types.Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await bot.send_message(user_id, 'Узнать данные можно 👇', reply_markup=me_telegram_keyboard)
    await bot.send_message(user_id, "Введите ваш api-id:")
    await state.set_state(StartUserBot.write_api_id)


async def input_api_id(msg: types.Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    if msg.text.isdigit():
        async with state.proxy() as data:
            data['write_api_id'] = int(msg.text)
    else:
        await bot.send_message(msg.from_user.id, "api-id должен состоять только из цифр! Вы где-то ошиблись!")
        return
    await bot.send_message(msg.from_user.id, "Введите api-hash:")
    await state.set_state(StartUserBot.write_api_hash)


async def input_api_hash(msg: types.Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    if len(msg.text) == 32:
        async with state.proxy() as data:
            data['write_api_hash'] = msg.text
    else:
        await bot.send_message(msg.from_user.id, "api-hash должен состоять из 32 цифры! Вы где-то ошиблись!")
        return
    await state.set_state(StartUserBot.write_phone)


async def input_phone(msg: types.Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    async with state.proxy() as data:
        data['phone'] = msg.text
    await state.set_state(StartUserBot.write_auth_code)


async def input_oauth_code(msg: types.Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    async with state.proxy() as data:
        data['oauth'] = msg.text

    await bot.send_message(msg.from_user.id, "User bot запущен")
    await state.finish()

# endregion


# TODO input of user settings

# region Vip

async def buy_vip(msg: types.Message) -> None:
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


async def check_oup_process(check_out_query: PreCheckoutQuery) -> None:
    bot: Bot = check_out_query.bot
    await bot.answer_pre_checkout_query(check_out_query.id, ok=True)


async def on_success_buy(msg: types.Message) -> None:
    bot: Bot = msg.bot
    set_vip(msg.from_user.id)
    await bot.send_message(msg.from_user.id, "Вы успешно оформили вип доступ!", reply_markup=main_keyboard_start_pro)

# endregion


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])

    dp.register_message_handler(buy_vip, content_types=['text'], text="Купить полную версию")
    dp.register_message_handler(input_api_id, content_types=['text'], state=StartUserBot.write_api_id)
    dp.register_message_handler(input_api_hash, content_types=['text'], state=StartUserBot.write_api_hash)
    dp.register_message_handler(input_phone, content_types=['text'], state=StartUserBot.write_phone)
    dp.register_message_handler(input_oauth_code, content_types=['text'], state=StartUserBot.write_auth_code)

    dp.register_pre_checkout_query_handler(check_oup_process, lambda q: True)
    dp.register_message_handler(on_success_buy, content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_message_handler(start_input_user_settings, content_types=['text'], text="Подключить бота", state=None)

