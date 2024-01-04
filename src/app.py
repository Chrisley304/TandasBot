from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from utils.strings import TELEGRAM_TOKEN
# Import of bot commands
from commands.help import start_command, help_command
from commands.handlers import handle_message, handle_error
from commands.create import create_tanda_command, get_tanda_name, get_tanda_participants, get_tanda_amount, get_tanda_period, cancel_create_command, TANDA_NAME, TANDA_PARTICIPANTS, TANDA_AMOUNT, TANDA_PERIOD

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Commands handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("ayuda", help_command))

    # Create tanda conversation handler
    create_tanda_handler = ConversationHandler(
        entry_points=[CommandHandler("creartanda", create_tanda_command)],
        states={
            TANDA_NAME: [MessageHandler(filters.TEXT, get_tanda_name)],
            TANDA_PARTICIPANTS: [MessageHandler(filters.TEXT, get_tanda_participants)],
            TANDA_AMOUNT: [
                MessageHandler(filters.TEXT, get_tanda_amount),
            ],
            TANDA_PERIOD: [MessageHandler(filters.TEXT, get_tanda_period)],
        },
        fallbacks=[CommandHandler("cancelar", cancel_create_command)],
    )

    app.add_handler(create_tanda_handler)

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    app.add_error_handler(handle_error)

    # Start polling
    print("Bot started!")
    app.run_polling(poll_interval=3)
