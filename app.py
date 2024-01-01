from dotenv import load_dotenv
from notion_client import Client
import os
from telegram.ext import Update

load_dotenv()  # take environment variables from .env.

def get_notion()->Client:
    """
        Get the notion client using the token from the environment variables.
    """
    return Client(auth=os.environ["NOTION_TOKEN"])

def main():
    """
        Main function of the app.
    """
    pass

main()