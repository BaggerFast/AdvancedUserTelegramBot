from telegram_bot.utils import TgConfig


def get_payment_info() -> dict:
    return {
        "amount": {
            "value": f"{TgConfig.PRICE}.00",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": TgConfig.BOT_URL,
        },
        "capture": True,
        "description": "EmojiBot - подключение Vip доступа"
    }
