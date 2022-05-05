from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from CFC.decorators import sudo_users_only
from CFC.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"https://telegra.ph/file/f82c6c960be3f8471fb0a.jpg",
        caption=f"""Hello, **Welcome** {message.from_user.mention()}\n
 I am powerful easy to use TeleGram Super Bot. I can play high quality and unbreakable music × video in your group voice chat. Just add me and promote with needed powers.

Use Inline buttons for more !!
For Help : @StrayCoderSupport""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ Add me in your Group",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(
                    "❓Commands", callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton("👤 Bot Owner", url=f"https://t.me/{itz_xoxo}"),
                    InlineKeyboardButton("👨‍💻 Developer", url=f"https://t.me/itz_xoxo"),
                ],
                [
                    InlineKeyboardButton(
                        "📨 Support", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📨 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⚙ Source Code", url="https://github.com/TheStrayCoder/MusicVideo-Stream"
                    )
                ],
            ]
        ),
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}", "alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start_group(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📨 Support", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📨 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 Uptime Status: `{uptime}`\n\n**𝗧𝗵𝗮𝗻𝗸𝘀 𝗳𝗼𝗿 𝗔𝗱𝗱𝗶𝗻𝗴 𝗺𝗲 𝗵𝗲𝗿𝗲, 𝗳𝗼𝗿 𝗽𝗹𝗮𝘆𝗶𝗻𝗴 𝗺𝘂𝘀𝗶𝗰 𝗼𝗻 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["repo", f"repo@{BOT_USERNAME}"]) & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""`Click on the Button given below to Get the source code of the Bot.`""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="⚙️ Source Code", url=f"https://github.com/TheStrayCoder/MusicVideo-Stream")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("I am Alive ~\n@StrayCoder\n\nI am ready to fuck the vc❗")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
