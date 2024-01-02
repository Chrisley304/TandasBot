from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater
from telegram import Update
from utils.strings import STRINGS

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