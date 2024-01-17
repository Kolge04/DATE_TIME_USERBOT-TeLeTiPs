#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [DATE_TIME Telegram userbot by TeLe TiPs] (https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from lists_teletips.quotes_teletips import *
from lists_teletips.emojis_teletips import *
from PIL import Image, ImageDraw, ImageFont
import datetime
import pytz
import asyncio
import random
import os


SESSION_STRING = "AgC6Un0AkCyV7TAXZ3OFLIMakARY-u90xzzNyiffwCnhecK2yL33--igWZK62VF6pwkYeLNkRqjCD_NT9WBy9VRO732xnNqepBhc_Xr8JxPQ-251FgrN9UiiAZjvsxYuZ631aGIP2gcM0QZCABPpHU6sqgLtwTIKHBB3r_1G3jAmiYh4vA0zQW_Hvs-RYOMGSPCPxwdRQD5TL96GVYE-LZDazxpZdtPCAp-OHO0k-97AL_mNWMUII2VPc9Njj81QlZHZT6E3rgIaaoKP3zFKoeWeO4kU77dwEvt0lSIbUXtcZYRH2mQQPG_JLe9Vc_Q-5M5QYeC16R6z3HduQxKsoK8mNVk_tAAAAAFRk3SoAA"
API_HASH = "e42eeae11a2f96bcfc5ec3b46a30adad"
API_ID = 12210813



Date_Time_Userbot_teletips=Client(
    name = "date_time_userbot_teletips",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)

Time_Zone = os.environ["Asia/Baku1"]

async def main_teletips():
    try:
        while True:
            if Date_Time_Userbot_teletips.is_connected:
                Quotes_teletips = random.choice(quotes_teletips)
                Emojis_teletips = random.choice(emojis_teletips)
                TimeZone_teletips = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))
                Time_teletips = TimeZone_teletips.strftime("%I:%M %p")
                Date_teletips = TimeZone_teletips.strftime("%b %d") 
                Image_teletips = Image.open("image.jpg")
                Image_font_teletips = ImageFont.truetype("ds-digit.ttf", 360)
                Image_text_teletips = f"{Time_teletips}"
                Image_edit_teletips = ImageDraw.Draw(Image_teletips)
                Image_edit_teletips.text((690, 550), Image_text_teletips, (0, 255, 255), font = Image_font_teletips)
                Image_teletips.save("Image_final_teletips.jpg")
                await Date_Time_Userbot_teletips.update_profile(bio = f"{Emojis_teletips} {Quotes_teletips}" , last_name = f"| ⏰ {Time_teletips} | 📅 {Date_teletips}")
                await Date_Time_Userbot_teletips.set_profile_photo(photo="Image_final_teletips.jpg")
                me = await Date_Time_Userbot_teletips.get_me()
                photos = Date_Time_Userbot_teletips.get_chat_photos("me")
                try:
                    await Date_Time_Userbot_teletips.delete_profile_photos(photos[1].file_id)
                except Exception:
                    pass        
                print("Profile Updated!")
            await asyncio.sleep(60)     
    except FloodWait as e:
        await asyncio.sleep(e.x)         

print("DATE TIME USERBOT IS ALIVE!")
asyncio.ensure_future(main_teletips())
Date_Time_Userbot_teletips.run()

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
