from utils.strings import STRINGS
from telegram import Update
from telegram.ext import ContextTypes, Updater
from utils.strings import BOT_USERNAME

def handle_response(text:str) -> str:
    """
        Handle the response from the user.
    """

    processed_text = text.lower()

    if processed_text == "hola":
        return STRINGS["responses"]["greeting"]

    return STRINGS["help"]["unknown"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Handle the message from the user.
    """
    # await update.message.reply_text(handle_response(update.message.text))
    message_type = update.message.chat.type
    text = update.message.text
    
    print(f'\n---\nUser ({update.message.chat.id}) in {message_type}: "{text}"')

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

async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Error handler.
    """
    print(f'Update {update} caused error {context.error}')