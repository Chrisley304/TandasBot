import json
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

STRINGS = {}
"""
    Variable with the strings of the bot. Using es.json file.
"""

# Load the strings from the json file
with open('src/lang/es.json', 'r') as f:
    STRINGS = json.load(f)

BOT_USERNAME = os.environ["BOT_USERNAME"]
"""
    Constant with the bot username.
"""
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
"""
    Constant with the notion token.

    TODO: Change this to accept the token from the user, instead of the environment variables.
"""

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
"""
    Constant with the telegram bot token.
"""