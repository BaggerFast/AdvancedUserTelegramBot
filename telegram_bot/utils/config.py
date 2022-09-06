from abc import ABC
from typing import Final
from yookassa import Configuration, Payment


class TgConfig(ABC):
    PRICE: Final = 60
    PREFIX: Final = '.'
    HELPER_URL: Final = '@Gamlet_Omlet'
    BOT_URL: Final = 'https://t.me/PronimBot'


Configuration.account_id = '939414'
Configuration.secret_key = 'test_gki50ihU_RxZ_siHtrpYQyyjb2oarNR_J1E2ia3nJSQ'
