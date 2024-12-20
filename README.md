# Discord YouTube to MP3 Bot

A Discord bot that automatically converts YouTube links to MP3 files in a designated channel.

## Features

- Monitors a specific channel named "music"
- Automatically detects YouTube links
- Downloads and converts videos to high-quality MP3
- Automatically sends the MP3 file back to the channel
- Cleans up files after sending

## Prerequisites

- Python 3.8 or higher
- Discord.py library
- yt-dlp
- A Discord bot token
- YouTube cookies file

## Installation

1. Install [yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/Installation):

```bash
pip install -U yt-dlp
```

2. Clone the repo:

```bash
git clone https://github.com/nitemare0X/discord-yt2mp3
cd discord-yt2mp3
```

Choose your preferred installation method:

### Method 1: Using uv (Faster Installation)

1. Install [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

2. Create and activate virtual environment:

```bash
uv venv
#then use its "Activate with:" command 
```

3. install dependencies:

```bash
uv pip install discord.py python-dotenv
```

### Method 2: Traditional Python/pip

1. Create and activate virtual environment:

```bash
python -m venv .venv

source .venv/bin/activate # Linux
.venv\bin\activate.ps1    # Windows
```

2. Install dependencies:

```bash
pip install discord.py python-dotenv
```

### After Installation (Both Methods)

Move the `.env-example` file to `.env` and configure the token:

```env
TOKEN=DISCORD_BOT_TOKEN_HERE
```

## Getting YouTube Cookies

To download age-restricted videos or access region-locked content, you'll need to provide your YouTube cookies:

1. Install the "Cookie-Editor" extension for your browser:
   - [Chrome Web Store](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
   - [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)

2. Steps to export cookies:
   - Log into YouTube
   - Click the Cookie-Editor extension icon
   - Click "Export" in the bottom right
   - Select "Export as Netscape HTTP Cookie File"
   - Save the file as `cookies.txt` in your bot's directory

## Usage

1. Create a channel named "music" in your Discord server
2. Run the bot:

```bash
python bot.py
```

3. Start sending youtube links in the channel and enjoy. 
