from aiogram import Dispatcher, Bot
from aiogram.types import PreCheckoutQuery, ContentTypes, Message, LabeledPrice

from telegram_bot.database.methods.other import is_admin
from telegram_bot.database.methods.update import set_vip
from telegram_bot.utils import Env, Config
from telegram_bot.utils.process import kill_process, start_process_if_sessions_exists, check_process
from telegram_bot.utils.util import get_main_keyboard


async def __buy_vip(msg: Message) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    if is_admin(user_id):
        await bot.send_message(user_id, 'Вы являетесь администратором, используйте настройку в Админ меню')
        return
    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="Vip",
        description="Описание",
        provider_token=Env.PAYMENTS_TOKEN,
        currency='rub',
        prices=[LabeledPrice(label="Vip доступ", amount=Config.PRICE*100)],
        start_parameter='True',
        payload='some_invoice',
        protect_content=True,
    )


async def __on_success_buy(msg: Message) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    set_vip(user_id)
    kill_process(user_id)
    start_process_if_sessions_exists(user_id)
    await bot.send_message(user_id, "Вы успешно оформили вип доступ!🥳\n",
                           reply_markup=get_main_keyboard(user_id))


async def __check_oup_process(check_out_query: PreCheckoutQuery) -> None:
    bot: Bot = check_out_query.bot
    await bot.answer_pre_checkout_query(check_out_query.id, ok=True)


def _register_vip_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__buy_vip, content_types=['text'], text="Купить полную версию")
    dp.register_message_handler(__on_success_buy, content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_pre_checkout_query_handler(__check_oup_process, lambda _: True)
