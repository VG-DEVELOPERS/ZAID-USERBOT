import base64
import requests
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message
from config import API_ID, API_HASH, STRING_SESSION, BOT_USERNAME, API_URL, API_TOKEN
from Zaid.modules.help import add_command_help

AUTO_GRAB = False  # Default state


@Client.on_message(filters.command("autograb", ".") & filters.me, group=3)
async def toggle_autograb(client: Client, message: Message):
    """Enable or disable autograb."""
    global AUTO_GRAB

    cmd = message.text.split()
    if len(cmd) < 2:
        return await message.reply("⚠️ Use `.autograb on` to enable or `.autograb off` to disable.")

    if cmd[1].lower() == "on":
        AUTO_GRAB = True
        await message.reply("✅ Auto-grab waifus is **enabled**!")
    elif cmd[1].lower() == "off":
        AUTO_GRAB = False
        await message.reply("❌ Auto-grab waifus is **disabled**!")
    else:
        await message.reply("⚠️ Invalid option! Use `.autograb on` or `.autograb off`.")


@Client.on_message(filters.chat(BOT_USERNAME) & filters.photo, group=3)
async def auto_grab_waifu(client: Client, message: Message):
    """Automatically grab waifus if enabled."""
    global AUTO_GRAB
    if not AUTO_GRAB:
        return  # Skip if auto-grab is disabled

    print("Received a waifu image, checking API...")

    # Download the image
    file = await message.download(in_memory=True)
    encoded_string = base64.b64encode(bytes(file.getbuffer())).decode()

    # Prepare API request
    data = {
        "api_token": API_TOKEN,
        "photo_b64": encoded_string
    }

    try:
        response = requests.post(API_URL, json=data)
        response_data = response.json()
        print("API Response:", response_data)  # Debugging

        if response_data.get("status") is True:
            char_name = response_data.get("name", "Unknown")
            print(f"Character Matched: {char_name}")

            # Send the /grab command automatically
            await asyncio.sleep(1)
            await message.reply(f"/grab {char_name}")
            print(f"Sent: /grab {char_name}")

        else:
            print("No match found for this waifu.")

    except Exception as e:
        print("API Error:", e)


add_command_help(
    "autograb",
    [
        [".autograb on", "Enables automatic waifu grabbing."],
        [".autograb off", "Disables automatic waifu grabbing."],
    ],
)
