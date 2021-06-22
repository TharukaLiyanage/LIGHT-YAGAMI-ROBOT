# COPYRIGHT (C) 2021 BY ANONYMOUS

"""
(((((((((((((((((((((((@XD_ANONYMOUS)))))))))))))))))))))))))))
(((((((((((((((((((((((@XD_ANONYMOUS)))))))))))))))))))))))))))
(((((((((((((((((((((((@XD_ANONYMOUS)))))))))))))))))))))))))))
(((((((((((((((((((((((@XD_ANONYMOUS)))))))))))))))))))))))))))
                 MADE BY ANONYMOUS
                   #PIKACHU_ON_FIRE
               #ANONYMOUS_OP_BOLTE HAHAHAHA
"""

from telethon import events, Button, custom
import re, os
from LightYagami.events import register
from LightYagami import telethn as LightYagami
from LightYagami import telethn as LightYagami
PHOTO = "https://telegra.ph/file/6f18a2115a76cb6285bb5.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "ʜᴇʏᴀᴀ ɪ'ᴍ ʟɪɢʜᴛ ʏᴀɢᴀᴍɪ 🔥\n\n"
  LEGENDX += "ᴀʟʟ sʏsᴛᴇᴍ ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  LEGENDX += "ʟɪɢʜᴛ ʏᴀɢᴀᴍɪ ᴏs : 3.8 ʟᴀᴛᴇsᴛ\n\n"
  LEGENDX += f"ᴍʏ ᴍᴀsᴛᴇʀ #ᴅᴇᴠɪʟ™🇮🇳\n\n"
  LEGENDX += "ғʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ\n\n"
  LEGENDX += "ᴛᴇʟᴇᴛʜᴏɴ : 1.19.5 ʟᴀᴛᴇsᴛ\n\n"
  LEGENDX += "ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ ʜᴇʀᴇ"
  BUTTON = [[Button.url("💻 ᴍᴀsᴛᴇʀ 💻", "https://t.me/ITZ_KING_VENOM"), Button.url("💻 ᴅᴇᴠʟᴏᴘᴇʀ 💻", "https://t.me/ITS_DEVIL_OP")]]
  BUTTON +=[[Button.url("💻Uᴘᴅᴀᴛᴇs💻", "https://t.me/YAGAMIBOT_UPDATES"), Button.url("💻Sᴜᴘᴘᴏʀᴛ💻", "https://t.me/YAGAMIBOT_SUPPORT")]]
  BUTTON += [[custom.Button.inline("lol", data="LEGENDX")]]
  await LightYagami.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@LightYagami.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# ɪɴʟɪɴᴇ ʙʏ  @XD_ANONYMOUS 🔥
   PROBOYX =[[Button.url("sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", "https://t.me/PIKACHUROBOT_UPDATES"), Button.url("SUPPORT", "https://t.me/PIKACHUROBOT_SUPPORT")]]
   PROBOYX +=[[custom.Button.inline("ᴀʟɪᴠᴇ", data="PROBOY")]]
  
@LightYagami.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  legendx = event.sender.first_name

__help__ = """
 - /alive ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ᴅɪᴇ
"""
__mod_name__ = "ALIVE"
