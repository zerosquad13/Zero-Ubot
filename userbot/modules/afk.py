# Copyright (C) 2020 TeamUltroid
# Ported by X_ImFine
# Recode by @mrismanaziz

import asyncio
import os
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from userbot import CMD_HANDLER as cmd
from userbot.events import man_cmd

from userbot import (  # noqa pylint: disable=unused-import isort:skip
    AFKREASON,
    ALIVE_NAME,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    COUNT_MSG,
    ISAFK,
    PM_AUTO_BAN,
    USERS,
    bot,
)

USER_AFK = {}
afk_time = None
last_afk_message = {}
last_afk_msg = {}
afk_start = {}


@bot.on(events.NewMessage(outgoing=True))
@bot.on(events.MessageEdited(outgoing=True))
async def set_not_afk(event):
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if "afk" not in current_message and "yes" in USER_AFK:
        try:
            if pic.endswith((".tgs", ".webp")):
                shite = await bot.send_message(event.chat_id, file=pic)
                shites = await bot.send_message(
                    event.chat_id,
                    f"**{ALIVE_NAME} 𝙆𝙚𝙢𝙗𝙖𝙡𝙞 𝙤𝙣𝙡𝙞𝙣𝙚 𝙪𝙣𝙩𝙪𝙠 𝙘𝙖𝙧𝙞 𝙥𝙖𝙧𝙩𝙣𝙚𝙧 𝙥𝙧𝙞𝙫𝙖𝙩𝙚**\n**𝘿𝙖𝙧𝙞 𝘼𝙁𝙆 :** `{total_afk_time}` **𝙔𝙖𝙣𝙜 𝙇𝙖𝙡𝙪**",
                )
            else:
                shite = await bot.send_message(
                    event.chat_id,
                    f"**{ALIVE_NAME} 𝙊𝙬𝙣𝙚𝙧 𝙓𝙓𝙓 𝙮𝙜 𝙥𝙖𝙡𝙞𝙣𝙜 𝙠𝙚𝙧𝙚𝙣 𝙗𝙖𝙡𝙞𝙠 𝙡𝙖𝙜𝙞!**\n**𝘿𝙖𝙧𝙞 𝘼𝙁𝙆 :** `{total_afk_time}` **𝙔𝙖𝙣𝙜 𝙇𝙖𝙡𝙪**",
                    file=pic,
                )
        except BaseException:
            shite = await bot.send_message(
                event.chat_id,
                f"**{ALIVE_NAME} 𝙆𝙚𝙢𝙗𝙖𝙡𝙞 𝙊𝙣𝙡𝙞𝙣𝙚**\n**𝘿𝙖𝙧𝙞 𝘼𝙁𝙆 :** `{total_afk_time}` **𝙔𝙖𝙣𝙜 𝙇𝙖𝙡𝙪**",
            )

        await asyncio.sleep(6)
        await shite.delete()
        try:
            await shites.delete()
        except BaseException:
            pass
        USER_AFK = {}
        afk_time = None

        os.system("rm -rf *.webp")
        os.system("rm -rf *.mp4")
        os.system("rm -rf *.tgs")
        os.system("rm -rf *.png")
        os.system("rm -rf *.jpg")


@bot.on(
    events.NewMessage(incoming=True, func=lambda e: bool(e.mentioned or e.is_private))
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None
        if reason:
            message_to_reply = (
                f"**🜏 {ALIVE_NAME} 𝙎𝙚𝙙𝙖𝙣𝙜 𝘼𝙁𝙆** `{total_afk_time}` **𝙔𝙖𝙣𝙜 𝙇𝙖𝙡𝙪 🜏**\n"
                + f"**🜏 𝙆𝙖𝙧𝙚𝙣𝙖 :** `{reason}`"
            )
        else:
            message_to_reply = (
                f"**🜏 𝙈𝙖𝙖𝙛 {ALIVE_NAME} 𝙎𝙚𝙙𝙖𝙣𝙜 𝘼𝙁𝙆** `{total_afk_time}` **𝙔𝙖𝙣𝙜 𝙇𝙖𝙡𝙪 🜏**"
            )
        try:
            if pic.endswith((".tgs", ".webp")):
                msg = await event.reply(file=pic)
                msgs = await event.reply(message_to_reply)
            else:
                msg = await event.reply(message_to_reply, file=pic)
        except BaseException:
            msg = await event.reply(message_to_reply)
        await asyncio.sleep(2.5)
        if event.chat_id in last_afk_message:
            await last_afk_message[event.chat_id].delete()
        try:
            if event.chat_id in last_afk_msg:
                await last_afk_msg[event.chat_id].delete()
        except BaseException:
            pass
        last_afk_message[event.chat_id] = msg
        try:
            if msgs:
                last_afk_msg[event.chat_id] = msgs
        except BaseException:
            pass


@bot.on(man_cmd(outgoing=True, pattern="afk(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    global USER_AFK
    global afk_time
    global last_afk_message
    global last_afk_msg
    global afk_start
    global afk_end
    global reason
    global pic
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    last_afk_msg = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    pic = await event.client.download_media(reply) if reply else None
    if not USER_AFK:
        last_seen_status = await bot(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()
        USER_AFK = f"yes: {reason} {pic}"
        if reason:
            try:
                if pic.endswith((".tgs", ".webp")):
                    await bot.send_message(event.chat_id, file=pic)
                    await bot.send_message(
                        event.chat_id,
                        f"\n**🜏 {ALIVE_NAME} Telah AFK 🜏**\n**🜏 Karena :** `{reason}`",
                    )
                else:
                    await bot.send_message(
                        event.chat_id,
                        f"\n**🜏 {ALIVE_NAME} Telah AFK 🜏**\n**🜏 Karena :** `{reason}`",
                        file=pic,
                    )
            except BaseException:
                await bot.send_message(
                    event.chat_id,
                    f"\n**🜏 {ALIVE_NAME} Telah AFK 🜏**\n**🜏 Karena :** `{reason}`",
                )
        else:
            try:
                if pic.endswith((".tgs", ".webp")):
                    await bot.send_message(event.chat_id, file=pic)
                    await bot.send_message(
                        event.chat_id, f"**🜏 {ALIVE_NAME} Telah AFK 🜏**"
                    )
                else:
                    await bot.send_message(
                        event.chat_id,
                        f"**🜏 {ALIVE_NAME} Telah AFK 🜏**",
                        file=pic,
                    )
            except BaseException:
                await bot.send_message(event.chat_id, f"**🜏 {ALIVE_NAME} Telah AFK 🜏**")
        await event.delete()
        try:
            if reason and pic:
                if pic.endswith((".tgs", ".webp")):
                    await bot.send_message(BOTLOG_CHATID, file=pic)
                    await bot.send_message(
                        BOTLOG_CHATID,
                        f"\n**🜏 {ALIVE_NAME} Sedang AFK 🜏**\n**🜏 Karena :** `{reason}`",
                    )
                else:
                    await bot.send_message(
                        BOTLOG_CHATID,
                        f"\n**🜏 {ALIVE_NAME} Sedang AFK 🜏**\n**🜏 Karena :** `{reason}`",
                        file=pic,
                    )
            elif reason:
                await bot.send_message(
                    BOTLOG_CHATID,
                    f"\n**🜏 {ALIVE_NAME} Sedang AFK 🜏**\n**🜏 Karena :** `{reason}`",
                )
            elif pic:
                if pic.endswith((".tgs", ".webp")):
                    await bot.send_message(BOTLOG_CHATID, file=pic)
                    await bot.send_message(
                        BOTLOG_CHATID, f"\n**🜏 {ALIVE_NAME} Sedang AFK 🜏**"
                    )
                else:
                    await bot.send_message(
                        BOTLOG_CHATID,
                        f"\n**🜏 {ALIVE_NAME} Sedang AFK 🜏**",
                        file=pic,
                    )
            else:
                await bot.send_message(
                    BOTLOG_CHATID, f"\n**🜏 {ALIVE_NAME} Sedang AFK 🜏**"
                )
        except Exception as e:
            BOTLOG_CHATIDger.warn(str(e))


CMD_HELP.update(
    {
        "afk": f"**Plugin : **`afk`\
        \n\n  •  **Syntax :** `{cmd}afk` <alasan> bisa <sambil reply sticker/foto/gif/media>\
        \n  •  **Function : **Memberi tahu kalau Master sedang afk bisa dengan menampilkan media keren ketika seseorang menandai atau membalas salah satu pesan atau dm Anda.\
        \n\n  •  **Syntax :** `{cmd}off`\
        \n  •  **Function : **Memberi tahu kalau Master sedang OFFLINE, dan menguubah nama belakang menjadi 【 OFF 】 \
    "
    }
)
