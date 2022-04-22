from CFC.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)







@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("▢", callback_data="cbstop"),
                      InlineKeyboardButton("II", callback_data="cbpause"),
                      InlineKeyboardButton("‣‣", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🚫 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)
        
        
#start



@Client.on_callback_query(filters.regex("cb_start"))
async def cb_start(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""Hello[,](https://telegra.ph/file/f82c6c960be3f8471fb0a.jpg) **Welcome** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})**\n
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
                    InlineKeyboardButton("👤 Bot Owner", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton("👨‍💻 Developer", url=f"https://t.me/Its_romeoo"),
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
                        "⚙ Source Code", url="https://github.com/SJMxADITI/TrickyMusic"
                    )
                ],
            ]
        ),
    )

    
    
    
    #Help command
    
    
@Client.on_callback_query(filters.regex("cb_cmd"))
async def cb_cmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Heyy** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

Check out the menu below to read the module information & see the list of available Commands !!

Developed By : @Its_romeoo""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Basic❗️", callback_data="cb_basic"),
                    InlineKeyboardButton("Advance 🕹", callback_data="cb_advance"),
                ],
               
                [InlineKeyboardButton("⬅️ Back", callback_data="cb_start")],
            ]
        ),
    )
    
@Client.on_callback_query(filters.regex("cb_basic"))
async def cb_basic(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""🤖 Normal Bot Commands :-

» /play - (song name) 
» /vplay - play video 
» /vstream - link or name
» /skip - Skip the Song
» /end - Stop Playing Music
» /pause - Pause the track
» /resume - Resumes the Track
» /mute - Mute the Assistant 
» /search - (song name)
» /song - Download Song File
» /lyrics - Get Lyrics of the Song

🌀 Powered By : @StrayCoder""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ Back", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_advance"))
async def cb_advance(_, query: CallbackQuery):
    await query.edit_message_text(    
      f"""⚙ Some Extra Commands :-

» /ping - Shows the Ping Status
» /alive - Shows the Alive Status
» /start - Starts the Bot
» /id - Get the ID
» /repo - Get the source code 
» /rmd - Clean all the downloads
» /clean - Clean the Storage
» /gcast - broadcast your message

🌀 Powered By : @StrayCoder""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ Back", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_fun"))
async def cb_fun(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""𝙁𝙪𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨
• `/lawda` 
• `/lassan`  
• `/randi`    
• `/lund`   
• `/chut`    
⚡""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ Back", callback_data="cb_cmd")]]
        ),
    )
        

    
    
    
        


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Sorry !! You are not a admin in this Group.", show_alert=True)
    await query.message.delete()
