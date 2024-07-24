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

import datetime
import time
from info import *
from utils import *
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio

@Client.on_message(filters.command('broadcast') & filters.user(ADMIN))
async def broadcast(bot, message):
    if not message.reply_to_message:
       return await message.reply("Use this command as a reply to any message!")
    m=await message.reply("Please wait...")   

    count, users = await get_users()
    stats     = "⚡ Broadcast Processing.."
    br_msg    = message.reply_to_message
    total     = count       
    remaining = total
    success   = 0
    failed    = 0    
     
    for user in users:
        chat_id = user["_id"]
        trying = await copy_msgs(br_msg, chat_id)
        if trying==False:
           failed+=1
           remaining-=1
        else:
           success+=1
           remaining-=1
        try:                                     
           await m.edit(script.BROADCAST.format(stats, total, remaining, success, failed))                                 
        except:
           pass
    stats = "✅ Broadcast Completed"
    await m.reply(script.BROADCAST.format(stats, total, remaining, success, failed)) 
    await m.delete()                                
      

@Client.on_message(filters.command('broadcast_groups') & filters.user(ADMIN))
async def grp_broadcast(bot, message):
    if not message.reply_to_message:
       return await message.reply("Use this command as a reply to any message!")
    m=await message.reply("Please wait...")   

    count, groups = await get_groups()
    stats     = "⚡ Broadcast Processing.."
    br_msg    = message.reply_to_message
    total     = count       
    remaining = total
    success   = 0
    failed    = 0    
     
    for group in groups:
        chat_id = group["_id"]
        trying = await grp_copy_msgs(br_msg, chat_id)
        if trying==False:
           failed+=1
           remaining-=1
        else:
           success+=1
           remaining-=1
        try:                                     
           await m.edit(script.BROADCAST.format(stats, total, remaining, success, failed))                                 
        except:
           pass
    stats = "✅ Broadcast Completed"
    await m.reply(script.BROADCAST.format(stats, total, remaining, success, failed)) 
    await m.delete()

    
    
async def grp_copy_msgs(br_msg, chat_id):
    try:
       h = await br_msg.copy(chat_id)
       try:
           await h.pin()
       except:
           pass
    except FloodWait as e:
       await asyncio.sleep(e.value)
       await copy_msgs(br_msg, chat_id)
    except Exception as e:
       await delete_group(chat_id)
       return False

   
async def copy_msgs(br_msg, chat_id):
    try:
       await br_msg.copy(chat_id)
    except FloodWait as e:
       await asyncio.sleep(e.value)
       await copy_msgs(br_msg, chat_id)
    except Exception as e:
       await delete_user(chat_id)
       return False

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
