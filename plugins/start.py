import os
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipan
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from vars import var


START_STRING =f"""
Hi , Welcome to ◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』's Pm Bot.
Use Help Button For More....

 By [◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/gishankrishka)
"""


START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』', url=f"https://t.me/{OWNER}")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="cmds")
                 ],
                 [
                 InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/imgishan_Bot?startgroup=true")
                 ]]
                  )
                  
FORCESUB_TEXT = "**❌ Access Denied ❌**\n\n🌷You Must Join My Update Channel...🌷\n♻️Join it & Try Again.♻️"

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』', url=f"https://t.me/{OWNER}")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )
                  
force_subchannel = "GishanKrishka1_Cloud"

OWNER = "ImGishan"

START_IMG = "https://telegra.ph/file/490a71ad194e4d6ea95f0.jpg"


@Client.on_message(filters.private & filters.command(["start"]))
async def help_me(bot, message):
    USER = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('USER', url=f"https://t.me/{message.from_user.username}")
                 ]]
                  )
    info = await bot.get_users(user_ids=message.from_user.id)
    USER_DETAILS = f"[{message.from_user.mention}](tg://user?id={message.from_user.id}) [`{message.from_user.id}`] Started Ur Bot.\n\n**PM FROM: `{info.first_name}`**\n**LastName: `{info.last_name}`**\n**Scam: `{info.is_scam}`**\n**Restricted: `{info.is_restricted}`**\n**Status:`{info.status}`**\n**Dc Id: `{info.dc_id}`**"
    await bot.send_message(-1001581011760, text=USER_DETAILS, reply_markup=USER)
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    text = START_STRING
    reply_markup = START_BUTTON   
    await message.reply_photo(START_IMG,
        caption=text,
        reply_markup=reply_markup
    )