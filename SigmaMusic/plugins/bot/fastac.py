import asyncio
import math
import os
import shutil
import socket
import traceback
import psutil
import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from pyrogram.types import Message
from SigmaMusic import app
from SigmaMusic.utils.database import active, activevideo
from config import OWNER_ID
from SigmaMusic.utils.cmdforac import avoice
#Imported Modules

#-------------------------------------------------------------------#


LOGINGG = config.LOGGER_ID


#--------------------------Code------------------#

@app.on_message(avoice(["/ac"]) & filters.user(OWNER_ID))
async def start(client: Client, message: Message):
    ac_audio = str(len(active))
    ac_video = str(len(activevideo))
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]
            ]
        )
    await message.reply_text(f"乛 ⛦🦋ѵ͠αℓeɳсι͢а⍣̥ ❥ ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ »\n•━━━━━━━━━━━━━━━━━━•\n🔮 ᴀᴄᴛɪᴠᴇ ᴀᴜᴅɪᴏ : {ac_audio}\n°──────────°\n💫 ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ  : {ac_video}\n°──────────°\n",quote=True, reply_markup=reply_markup)
    

#--------------------------Clean_Commands------------------------#

@app.on_message(avoice(["/rm"]) & filters.user(OWNER_ID))
async def cleaning(client: Client, message: Message):
    A = 'rm -f -r unknown_errors.txt && rm -f -r logs.txt && rm -f -r logs.txt.1 && rm -f -r logs.txt.2 && rm -f -r logs.txt.3 && rm -f -r logs.txt.4 && rm -f -r logs.txt.5 && rm -f -r logs.txt.6 && rm -f -r logs.txt.7 && rm -f -r logs.txt.8 && rm -f -r logs.txt.9 && rm -f -r logs.txt.10'
    try:
        os.system(A)
    except:
        await message.reply_text(f"Failed To Delete Temp !!\nPlease Read\n{traceback.format_exc()}", quote=True)
    await message.reply_text(f"Successfully Deleted Below Folders:\n -Log Files \n -Error Files", quote=True)

    
CPU_LOAD = psutil.cpu_percent(interval=0.5)
RAM_LOAD = psutil.virtual_memory().percent
DISK_SPACE = psutil.disk_usage("/").percent
