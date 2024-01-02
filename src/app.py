from dotenv import load_dotenv
from notion_client import Client
import os
import json
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater
from telegram import Update

load_dotenv()  # take environment variables from .env.

# Variable with the strings of the bot.
STRINGS = {}
with open('./lang/es.json', 'r') as f:
    STRINGS = json.load(f)

BOT_USERNAME = os.environ["BOT_USERNAME"]

def get_notion()->Client:
    """
        Get the notion client using the token from the environment variables.
    """
    return Client(auth=os.environ["NOTION_TOKEN"])

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Start command handler.
    """
    await update.message.reply_text(STRINGS["help"]["start"])

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Help command handler.
    """
    await update.message.reply_text(STRINGS["help"]["commands"])

# Responses
def handle_response(text:str) -> str:
    """
        Handle the response from the user.
    """

    processed:str = text.lower()

    if text == "/start":
        return STRINGS["help"]["start"]
    elif text == "/help":
        return STRINGS["help"]["commands"]
    elif text == "hola":
        return STRINGS["responses"]["start"]

    return STRINGS["help"]["unknown"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Handle the message from the user.
    """
    # await update.message.reply_text(handle_response(update.message.text))
    message_type = update.message.chat.type
    text = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, "").strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    print(f'Response: "{response}"')
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Error handler.
    """
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(os.environ["TELEGRAM_TOKEN"]).build()

    # Commands handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    app.add_error_handler(error)

    # Start polling
    print("Bot started!")
    app.run_polling(poll_interval=3)