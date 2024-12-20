import discord
import subprocess
from discord.ext import commands
from datetime import datetime
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True
intents.members = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("---------------------")


@bot.event
async def on_message(message):
    if message.channel.name == "music":
        if "youtube.com" in message.content or "youtu.be" in message.content:
            # Extract the YouTube link from the message
            url = extract_youtube_link(message.content)

            # Get the downloaded audio file
            #            audio_files = [filename for filename in os.listdir() if filename.endswith(".mp3")]
            #            if len(audio_files) > 0:
            #                audio_file = audio_files[0]

            # Download video using yt-dlp subprocess
            dl_command = f"yt-dlp -q --cookies cookies.txt -x --audio-format mp3 --audio-quality 0 {url}"
            subprocess.run(dl_command, shell=True)
            #            print(f'[{datetime.now().strftime("%Y-%m-%d:%H:%M")}]: Downloading file as {audio_file}')

            # Get the downloaded audio file
            audio_files = [
                filename for filename in os.listdir() if filename.endswith(".mp3")
            ]
            if len(audio_files) > 0:
                audio_file = audio_files[0]

            # Send the audio file back to the channel
            await message.reply(file=discord.File(audio_file))
            await asyncio.sleep(3)
            print(
                f'[{datetime.now().strftime("%Y-%m-%d:%H:%M")}]: {audio_file} deleted'
            )
            os.remove(audio_file)
            print(
                f'[{datetime.now().strftime("%Y-%m-%d:%H:%M")}]: Waiting for next file'
            )

    await bot.process_commands(message)


def extract_youtube_link(content):
    # Extract YouTube link from the message content
    # You can use regex or other methods to extract the link
    # Here's a simple example using string manipulation
    start_index = content.find("https://")
    end_index = content.find(" ", start_index)
    if end_index == -1:
        end_index = len(content)
    return content[start_index:end_index]


bot.run(f'{os.getenv("TOKEN")}')
