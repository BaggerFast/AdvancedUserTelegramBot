from aiogram import types, Dispatcher, Bot

from telegram_bot.bot.database.methods import add_user, check_vip
from telegram_bot.bot.keyboards import main_keyboard_start_pro, main_keyboard_start_trial


async def start(msg: types.Message):
    add_user(msg.from_user.id)
    bot: Bot = msg.bot
    vip_status: bool = check_vip(msg.from_user.id)
    if vip_status:
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_pro)
    else:
        await bot.send_message(msg.from_user.id, "Hi, this is super user-bot!", reply_markup=main_keyboard_start_trial)


# TODO Implement the purchase of VIP status
async def buy_vip(msg: types.Message):
    pass


def register_users_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
