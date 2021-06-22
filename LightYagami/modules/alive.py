# Thanks to @PYTHON_CODER_SRINIVAS.. 
# animation Idea by @PYTHON_CODER_SRINIVAS
# Made by @PYTHON_CODER_SRINIVAS...and thanks to @PYTHON_CODER_SRINIVAS...the logos...
# Kang with credits else gay...
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOT"

# Thanks to ASHUTOSH BRO.. 
# animation Idea by @PYTHON_CODER_SRINIVAS (op coder)
# Made by @PYTHON_CODER_SRINIVAS...and thanks to @koi_nhi_apna for the logos...
# Kang with credits else gay...
# alive.py for ɖǟʀӄ ֆɦǟɖօա

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/4e3f8b0d846c2c87352d7.mp4"
file2 = "https://telegra.ph/file/4e3f8b0d846c2c87352d7.mp4"
file3 = "https://telegra.ph/file/4e3f8b0d846c2c87352d7.mp4"
file4 = "https://telegra.ph/file/4e3f8b0d846c2c87352d7.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "devil king 😈 ɨֆ օռʟɨռɛ..!! **🔥🔥\n\n"
pm_caption += "⚔️⚔️ **Master, Am Alive And Systems Are Working Perfectly As It Should Be...**⚔️⚔️\n\n"
pm_caption += "༆༄☠︎︎About My System \n\n"
pm_caption += "🔥🔥 **ᴛᴇʟᴇᴛʜᴏɴ**🔥🔥 >>》 15.0.0\n"
pm_caption += "🚨🚨 **group**🚨🚨   >>》 [ʝօɨռ](https://t.me/TheEdutainmentAdda)\n"
pm_caption += f"🔰🔰**ᴍᴀsᴛᴇʀ**🔰🔰  >>》 {DEFAULTUSER}\n"
pm_caption += "🌏🌏 **ᴄʀᴇᴀᴛᴏʀ**🌏🌏  >>》 [ᴏᴡɴᴇʀ](https://t.me/@Devil_killer1st)\n\n"
pm_caption += "🔶🔶 **ᴄʀᴇᴅɪᴛs**🔶🔶  >>》 [ʙʀᴏ](https://t.me/respectgirls1st)\n\n"
pm_caption += "[....▄███▄███▄\n....█████████\n.......▀█████▀\n...............▀█▀\n](https://t.m/TheEdutainmentAdda)\n\n"
@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
