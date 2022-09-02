from aiogram import Dispatcher, Bot
from aiogram.types import PreCheckoutQuery, ContentTypes, Message, LabeledPrice

from telegram_bot.env import TgBot
from telegram_bot.database.methods import set_vip
from telegram_bot.keyboards import KB_START_BOT
from telegram_bot.handlers.user.user_bot import _process
from telegram_bot.misc.util import get_main_keyboard


async def __buy_vip(msg: Message) -> None:
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


async def __on_success_buy(msg: Message) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    set_vip(user_id)
    if user_id in _process:
        process_bot = _process[user_id]
        process_bot.kill()
        del _process[user_id]

        await bot.send_message(user_id, "Вы успешно оформили вип доступ!\n"
                                        "Запустите User бота заново, что-бы получить все возможности",
                               reply_markup=get_main_keyboard(user_id, user_id in _process))
    else:
        await bot.send_message(msg.from_user.id, "Вы успешно оформили вип доступ!\n",
                               reply_markup=get_main_keyboard(user_id, user_id in _process))


async def __check_oup_process(check_out_query: PreCheckoutQuery) -> None:
    bot: Bot = check_out_query.bot
    await bot.answer_pre_checkout_query(check_out_query.id, ok=True)


def _register_vip_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__buy_vip, content_types=['text'], text="Купить полную версию")
    dp.register_message_handler(__on_success_buy, content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_pre_checkout_query_handler(__check_oup_process, lambda _: True)
