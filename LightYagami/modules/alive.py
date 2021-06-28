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
PHOTO = "https://telegra.ph/file/2a201600dd3827404201f.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "𝐇𝐄𝐘𝐀𝐀 𝐈'𝐌 𝐋𝐈𝐆𝐇𝐓 𝐘𝐀𝐆𝐀𝐌𝐈 😈\n\n"
  LEGENDX += "𝐀𝐋𝐋 𝐒𝐘𝐒𝐓𝐄𝐌 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐏𝐑𝐎𝐏𝐄𝐑𝐋𝐘\n\n"
  LEGENDX += "𝐋𝐈𝐆𝐇𝐓 𝐘𝐀𝐆𝐀𝐌𝐈 𝐎𝐒 : 𝟑. 𝟖 𝐋𝐄𝐓𝐄𝐒𝐓\n\n"
  LEGENDX += f"𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🇮🇳 #𝐑𝐨𝐜𝐤𝐲 🇮🇳\n\n"
  LEGENDX += "𝐅𝐔𝐋𝐋𝐘 𝐔𝐏𝐃𝐀𝐓𝐄𝐃\n\n"
  LEGENDX += "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 : 𝟏. 𝟏𝟗. 𝟓 𝐋𝐀𝐓𝐄𝐒𝐓\n\n"
  LEGENDX += "𝐓𝐇𝐀𝐍𝐊𝐒 𝐅𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐄 𝐇𝐄𝐑𝐄"
  BUTTON = [[Button.url("𝐌𝐀𝐒𝐓𝐄𝐑", "https://t.me/ROCKY_HU_BC"), Button.url("𝐃𝐄𝐕𝐋𝐎𝐏𝐄𝐑", "https://t.me/DANISH_ALONE_FIGHTER")]]
  BUTTON +=[[Button.url("𝐔𝐏𝐃𝐀𝐓𝐄𝐒", "https://t.me/KIRAUPDATESS"), Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓", "https://t.me/KIRASUPPORT")]]
  BUTTON += [[custom.Button.inline(" 𝐈'𝐌 𝐊𝐈𝐑𝐀 😈", data="LEGENDX")]]
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

help = """
 - /alive ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ᴅɪᴇ
"""
__mod_name__= "ALIVE"
