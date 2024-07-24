# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! 
from info import PICS
import random
from plugins.forcesub import ForceSub
from utils import *
from pyrogram import Client, filters
from plugins.generate import database 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

# Main buttons for the bot
main_buttons = [[
    InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url='https://t.me/{username}?startgroup=true')
], [
    InlineKeyboardButton("ʜᴇʟᴘ", callback_data="misc_help"),
    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_about")
]]

@Client.on_message(filters.command("start") & ~filters.channel)
async def start(bot, message):
    # Check for force subscription
    Fsub = await ForceSub(bot, message)
    if Fsub == 400:
        return

    database.insert_one({"chat_id": message.from_user.id})
    username = (await bot.get_me()).username
    await add_user(message.from_user.id, message.from_user.first_name)
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random.choice(PICS),
        caption=script.START.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(main_buttons)
    )

@Client.on_message(filters.command("help"))
async def help(bot, message):
    # Check for force subscription
    Fsub = await ForceSub(bot, message)
    if Fsub == 400:
        return

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random.choice(PICS),
        caption=script.HELP
    )

@Client.on_message(filters.command("about"))
async def about(bot, message):
    # Check for force subscription
    Fsub = await ForceSub(bot, message)
    if Fsub == 400:
        return

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random.choice(PICS),
        caption=script.ABOUT.format((await bot.get_me()).mention)
    )

@Client.on_message(filters.command("stats"))
async def stats(bot, message):
    # Check for force subscription
    Fsub = await ForceSub(bot, message)
    if Fsub == 400:
        return

    g_count, g_list = await get_groups()
    u_count, u_list = await get_users()
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random.choice(PICS),
        caption=script.STATS.format(u_count, g_count)
    )

@Client.on_message(filters.command("id"))
async def id(bot, message):
    # Check for force subscription
    Fsub = await ForceSub(bot, message)
    if Fsub == 400:
        return

    text = f"Current Chat ID: `{message.chat.id}`\n"
    if message.from_user:
        text += f"Your ID: `{message.from_user.id}`\n"
    if message.reply_to_message:
        if message.reply_to_message.from_user:
            text += f"Replied User ID: `{message.reply_to_message.from_user.id}`\n"
        if message.reply_to_message.forward_from:
            text += f"Replied Message Forward from User ID: `{message.reply_to_message.forward_from.id}`\n"
        if message.reply_to_message.forward_from_chat:
            text += f"Replied Message Forward from Chat ID: `{message.reply_to_message.forward_from_chat.id}`\n"

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random.choice(PICS),
        caption=text
    )

@Client.on_callback_query(filters.regex(r"^misc"))
async def misc(bot, update):
    data = update.data.split("_")[-1]
    if data == "home":
        username = (await bot.get_me()).username
        button = [[
    InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url='https://t.me/{username}?startgroup=true')
], [
    InlineKeyboardButton("ʜᴇʟᴘ", callback_data="misc_help"),
    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_about")
]]
        await update.message.edit(
            text=script.START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(button)
        )
    elif data == "help":
        await update.message.edit(
            text=script.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="misc_home")]
            ])
        )
    elif data == "about":
        await update.message.edit(
            text=script.ABOUT.format((await bot.get_me()).mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="misc_home")]
            ])
        )

# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! 
         
