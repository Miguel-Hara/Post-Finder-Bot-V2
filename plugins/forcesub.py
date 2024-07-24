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

import random
import info
import asyncio
from info import UPDATES_CHANNEL, PICS  # Import PICS here
import pyrogram
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

async def ForceSub(c: Client, m: Message):
    try:
        invite_link = await c.create_chat_invite_link(chat_id=(int(info.UPDATES_CHANNEL) if info.UPDATES_CHANNEL.startswith("-100") else info.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        invite_link = await c.create_chat_invite_link(chat_id=(int(info.UPDATES_CHANNEL) if info.UPDATES_CHANNEL.startswith("-100") else info.UPDATES_CHANNEL))
    except Exception as err:
        print(f"Unable to do force subscribe to {info.UPDATES_CHANNEL}\n\nError: {err}")
        return 200
    try:
        user = await c.get_chat_member(chat_id=(int(info.UPDATES_CHANNEL) if info.UPDATES_CHANNEL.startswith("-100") else info.UPDATES_CHANNEL), user_id=m.from_user.id)
        if user.status == "kicked":
            await c.send_message(
                chat_id=m.from_user.id,
                text="Sorry sir, you are banned to use me. Contact my admin @anmol0700.",
                disable_web_page_preview=True,
                parse_mode="Markdown",
            )
            return 400
    except UserNotParticipant:
        await c.send_photo(
            chat_id=m.from_user.id,
            photo=random.choice(PICS),  # Use imported PICS
            caption="**Please join my updates channel to use this bot!**\n\nOnly channel subscribers can use the bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join updates channel", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="misc_home")
                    ]
                ]
            )
        )
        return 400
    except Exception:
        await c.send_message(
            chat_id=m.from_user.id,
            text="Something went wrong. Contact my admin.",
            disable_web_page_preview=True,
            parse_mode="Markdown",
        )
        return 400
    return 200


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
