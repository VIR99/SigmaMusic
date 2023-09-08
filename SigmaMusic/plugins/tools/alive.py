import asyncio

from SigmaMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://te.legra.ph/file/678a0aa16416d550a9b77.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="🔮 ˹ Oᴡɴᴇʀ", url=f"https://t.me/IAM_B3SHARAM"
            ),
            InlineKeyboardButton(
                text="🔮 Mᴇᴇᴛ ᴍᴇ", url=f"https://t.me/Shayri_Music_Lovers"
            ),
        ],
                [
            InlineKeyboardButton(
                text="🔮 Aʙᴏᴜᴛ ᴍᴇ", url=f"https://t.me/AbOuT_InNoCeNt"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "✯ Cʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
