from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater
from telegram import Update
from utils.strings import STRINGS

async def create_tanda_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Create a new tanda command handler.
    """
    await update.message.reply_text(STRINGS["commands"]["create"]["start"])