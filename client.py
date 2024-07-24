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

from info import *
from pyrogram import Client

class Bot(Client):   
    def __init__(self):
        super().__init__(   
            "miguel-post-bot-v2",  
            api_id=API_ID,
            api_hash=API_HASH,           
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})
    
    async def start(self):                        
        await super().start()  
        print("""
███╗░░░███╗██╗░██████╗░██╗░░░██╗███████╗██╗░░░░░  ░█████╗░██╗██╗░░██╗░█████╗░██████╗░░█████╗░
████╗░████║██║██╔════╝░██║░░░██║██╔════╝██║░░░░░  ██╔══██╗╚█║██║░░██║██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║██║██║░░██╗░██║░░░██║█████╗░░██║░░░░░  ██║░░██║░╚╝███████║███████║██████╔╝███████║
██║╚██╔╝██║██║██║░░╚██╗██║░░░██║██╔══╝░░██║░░░░░  ██║░░██║░░░██╔══██║██╔══██║██╔══██╗██╔══██║
██║░╚═╝░██║██║╚██████╔╝╚██████╔╝███████╗███████╗  ╚█████╔╝░░░██║░░██║██║░░██║██║░░██║██║░░██║
╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚═════╝░╚══════╝╚══════╝  ░╚════╝░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝""")
    
    async def stop(self, *args):
        await super().stop()
