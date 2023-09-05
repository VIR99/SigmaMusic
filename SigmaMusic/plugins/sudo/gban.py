import asyncio
import time

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from config import BANNED_USERS, OWNER_ID, GBAN_LOG_ID
from SigmaMusic import app
from SigmaMusic.utils import get_readable_time
from SigmaMusic.utils.database import (
    add_banned_user,
    get_banned_count,
    get_banned_users,
    get_served_chats,
    is_banned_user,
    remove_banned_user,
)
from SigmaMusic.utils.decorators.language import language


GBAN_CHANNEL = GBAN_LOG_ID


@app.on_message(filters.command("gban", "globalban") & filters.user(OWNER_ID))
@language
async def global_ban(client, message: Message, _):
    if not message.reply_to_message:
        text_cutting = message.text.split(" ")
        user = text_cutting[1]
        choose_reason = text_cutting[2:]
        reason = " ".join(choose_reason)
        user = await app.get_users(user)
        user_id = user.id
        mention = user.mention
        sudo_admin = message.from_user.username
        sudo_admin_id = message.from_user.id
        sudo_first_name = message.from_user.mention
        if len(text_cutting) <= 2:
            return await message.reply_text(_["gban_reason"])
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    if user_id == message.from_user.id:
        return await message.reply_text(_["gban_1"])
    elif user_id == app.id:
        return await message.reply_text(_["gban_2"])
    elif user_id in SUDOERS:
        return await message.reply_text(_["gban_3"])
    is_gbanned = await is_banned_user(user_id)
    if is_gbanned:
        return await message.reply_text(_["gban_4"].format(mention))
    if user_id not in BANNED_USERS:
        BANNED_USERS.add(user_id)
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = len(served_chats)
    time_expected = get_readable_time(time_expected)
    mystic = await message.reply_text(_["gban_5"].format(mention, time_expected))
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await app.ban_chat_member(chat_id, user_id)
            number_of_chats += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.value))
        except Exception:
            pass
    await add_banned_user(user_id)
    await message.reply_text(_["gban_6"].format(mention, number_of_chats))
    await app.send_message(
        GBAN_CHANNEL, _["gban_log"].format(sudo_first_name, sudo_admin, mention, reason)
    )
    await app.send_message(GBAN_CHANNEL, _["gban_warning"].format(mention))
    await mystic.delete()


@app.on_message(filters.command("ungban") & filters.user(OWNER_ID))
@language
async def gungabn(client, message: Message, _):
    if not message.reply_to_message:
        text_cutting = message.text.split(" ")
        user = text_cutting[1]
        user = await app.get_users(user)
        user_id = user.id
        mention = user.mention
        choose_reason = text_cutting[2:]
        reason = " ".join(choose_reason)
        sudo_admin = message.from_user.username
        sudo_admin_id = message.from_user.id
        sudo_first_name = message.from_user.mention
        if len(text_cutting) <= 2:
            return await message.reply_text(_["ungban_reason"])
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    is_gbanned = await is_banned_user(user_id)
    if not is_gbanned:
        return await message.reply_text(_["gban_7"].format(mention))
    if user_id in BANNED_USERS:
        BANNED_USERS.remove(user_id)
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = len(served_chats)
    time_expected = get_readable_time(time_expected)
    mystic = await message.reply_text(_["gban_8"].format(mention, time_expected))
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await app.unban_chat_member(chat_id, user_id)
            number_of_chats += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.value))
        except Exception:
            pass
    await remove_banned_user(user_id)
    await message.reply_text(_["gban_9"].format(mention, number_of_chats))
    await app.send_message(
        GBAN_CHANNEL,
        _["ugban_log"].format(sudo_first_name, sudo_admin, mention, reason),
    )
    await mystic.delete()


@app.on_message(filters.command("gbannedusers", "gbanlist") & filters.user(OWNER_ID))
@language
async def gbanned_list(client, message: Message, _):
    counts = await get_banned_count()
    if counts == 0:
        return await message.reply_text(_["gban_10"])
    mystic = await message.reply_text(_["gban_11"])
    msg = "ɢʙᴀɴɴᴇᴅ ᴜsᴇʀs:\n\n"
    count = 0
    users = await get_banned_users()
    for user_id in users:
        count += 1
        try:
            user = await app.get_users(user_id)
            user = user.first_name if not user.mention else user.mention
            msg += f"{count}➤ {user}\n"
        except Exception:
            msg += f"{count}➤ [ɢʙᴀɴɴᴇᴅ ᴜsᴇʀs]{user_id}\n"
            continue
    if count == 0:
        return await mystic.edit_text(_["gban_10"])
    else:
        return await mystic.edit_text(msg)
