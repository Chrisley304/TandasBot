from telegram.ext import Application, CommandHandler, MessageHandler, filters
# Import of bot commands
from commands.help import start_command, help_command
from commands.handlers import handle_message, handle_error
from utils.strings import TELEGRAM_TOKEN

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Commands handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    app.add_error_handler(handle_error)

    # Start polling
    print("Bot started!")
    app.run_polling(poll_interval=3)