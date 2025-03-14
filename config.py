import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

API_ID = int(getenv("API_ID", "6435225"))  # Optional
API_HASH = getenv("API_HASH", "")  # Optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN")  # Personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/VG-DEVELOPERS/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master")  # Don't change

STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")

# API for AutoGrab
API_URL = getenv("API_URL", "http://cheatbot.twc1.net/getName")
API_TOKEN = getenv("API_TOKEN", "TEST-API-TOKEN")
BOT_USERNAME = getenv("BOT_USERNAME", "@Fancy_Waifu_Husbando_Bot")  # Example bot username
