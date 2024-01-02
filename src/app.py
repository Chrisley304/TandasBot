from telegram.ext import Application, CommandHandler, MessageHandler, filters
from utils.strings import TELEGRAM_TOKEN
# Import of bot commands
from commands.help import start_command, help_command
from commands.handlers import handle_message, handle_error
from commands.create import create_tanda_command

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Commands handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("ayuda", help_command))
    app.add_handler(CommandHandler("creartanda", create_tanda_command))

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    app.add_error_handler(handle_error)

    # Start polling
    print("Bot started!")
    app.run_polling(poll_interval=3)