import asyncio
from aiohttp import ClientSession
from pyrogram import Client
from config import (
    API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, 
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, 
    STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, 
    STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
)
from datetime import datetime
import time

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)

# ✅ Properly initialize aiohttp session
aiosession = None  # Declare globally

async def init_session():
    global aiosession
    if aiosession is None:
        aiosession = ClientSession()

asyncio.run(init_session())  # Ensures session is initialized properly

if not API_ID:
    print("WARNING: API ID NOT FOUND, USING DEFAULT ⚡")
    API_ID = "6435225"

if not API_HASH:
    print("WARNING: API HASH NOT FOUND, USING DEFAULT ⚡")   
    API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
    print("WARNING: BOT TOKEN NOT FOUND! Please add it ⚡")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Zaid/modules/bot"),
    in_memory=True,
)

sessions = [
    (STRING_SESSION1, "one"), (STRING_SESSION2, "two"),
    (STRING_SESSION3, "three"), (STRING_SESSION4, "four"),
    (STRING_SESSION5, "five"), (STRING_SESSION6, "six"),
    (STRING_SESSION7, "seven"), (STRING_SESSION8, "eight"),
    (STRING_SESSION9, "nine"), (STRING_SESSION10, "ten")
]

for session_string, name in sessions:
    if session_string:
        print(f"Client {name.capitalize()}: Found.. Starting.. 📳")
        client = Client(name=name, api_id=API_ID, api_hash=API_HASH, session_string=session_string, plugins=dict(root="Zaid/modules"))
        clients.append(client)
      
