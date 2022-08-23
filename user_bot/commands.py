# from telethon import TelegramClient
# from telethon.events import *
# from telethon.events.newmessage import NewMessage as Msg
#
#
# @register(event=Msg(pattern=r"\.he"))
# async def on_he(event: Msg.Event) -> None:
#     client: TelegramClient = event.client
#     await client.send_code_request(phone="+79206671979")
#
#
# @register(event=Msg(pattern=r"\.penis"))
# async def make_dick(event: Msg.Event):
#     await event.client.edit_message(event.message, "")
