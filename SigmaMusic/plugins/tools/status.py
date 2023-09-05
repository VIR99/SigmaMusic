import psutil
import time
from SigmaMusic import app as Client
from pyrogram import filters 
from pyrogram.types import Message

start_time = time.time()

def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (((str(weeks) + "w:") if weeks else "") +
           ((str(days) + "d:") if days else "") +
           ((str(hours) + "h:") if hours else "") +
           ((str(minutes) + "m:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))
    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp


@Client.on_message(filters.command('RocksStatusBot') & filters.private)
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    TEXT = f"ᴜᴘᴛɪᴍᴇ : {uptime} | ᴄᴘᴜ : {cpu}%"
    await message.reply(TEXT)