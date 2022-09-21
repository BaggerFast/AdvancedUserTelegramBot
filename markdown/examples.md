# Code Guide

### To understand the architecture of the application, watch this [VIDEO](https://www.youtube.com/watch?v=W-0YoEYBSwU&t=23s)

## [Main Bot](../telegram_bot/main.py)
1. [Setup config.py](../telegram_bot/utils/config.py):
   - PRICE - price for vip access
   - HELPER_URL - telegram username (@username) for help btn
   - BOT_URL - this bot username (@bot) for advert in free commands
   - VIP_HELP_URL - site url for view vip help commands
   - VIP_HELP_URL - site url for view free help commands

2. Add user commands [HERE](../telegram_bot/handlers/user/main.py)
3. Add admin commands [HERE](../telegram_bot/handlers/admin/main.py)

4. If you want to change the payment system, edit this [FILE](../telegram_bot/handlers/user/buy_vip.py)
--------

## [User Bot](../user_bot/main.py)
1. [Setup config.py](../user_bot/utils/config.py):
   - PREFIX - sign for commands (.hello)
   
2. Add Free commands [HERE](../user_bot/handlers/common/main.py)
3. Add Vip commands [HERE](../user_bot/handlers/vip/main.py)

--------

### [BACK](../README.md)