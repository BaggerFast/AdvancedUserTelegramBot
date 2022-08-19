from aiogram import types, Dispatcher, Bot
from aiogram.types import LabeledPrice, PreCheckoutQuery, ContentTypes

from telegram_bot.bot.database.methods import add_user, check_vip, set_vip
from telegram_bot.bot.keyboards import main_keyboard_start_pro, main_keyboard_start_trial
from telegram_bot.bot import TgBot


async def start(msg: types.Message) -> None:
    add_user(msg.from_user.id)
    bot: Bot = msg.bot
    vip_status: bool = check_vip(msg.from_user.id)
    if vip_status:
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_pro)
    else:
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_trial)


async def buy_vip(msg: types.Message) -> None:
    bot: Bot = msg.bot
    await bot.send_invoice(msg.chat.id,
                           title="Vip",
                           description="Описание",
                           provider_token=TgBot.PAYMENTS_TOKEN,
                           currency='rub',
                           prices=[LabeledPrice(label="Vip доступ", amount=30000)],
                           start_parameter=True,
                           payload='some_invoice',
                           protect_content=True)


async def check_oup_process(check_out_query: PreCheckoutQuery) -> None:
    bot: Bot = check_out_query.bot
    await bot.answer_pre_checkout_query(check_out_query.id, ok=True)


async def on_succes_buy(msg: types.Message) -> None:
    bot: Bot = msg.bot
    set_vip(msg.from_user.id)
    await bot.send_message(msg.from_user.id, "Вы успешно оформили вип доступ!", reply_markup=main_keyboard_start_pro)


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(buy_vip, content_types=['text'], text="Купить полную версию")
    dp.register_message_handler(on_succes_buy, content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_pre_checkout_query_handler(check_oup_process, lambda q: True)
