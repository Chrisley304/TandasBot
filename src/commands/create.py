from telegram.ext import filters, ContextTypes, Updater, ConversationHandler
from telegram import Update, ReplyKeyboardRemove
from utils.strings import STRINGS
from models.tanda import Tanda

TANDA_NAME, TANDA_PARTICIPANTS, TANDA_AMOUNT, TANDA_PERIOD = range(4)


async def create_tanda_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Create a new tanda command handler.
    """
    await update.message.reply_text(STRINGS["commands"]["create"]["start"])
    await update.message.reply_text(STRINGS["commands"]["create"]["get_name"])

    return TANDA_NAME


async def get_tanda_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
        Stores the tanda name given from the user.
    """
    user = update.message.from_user
    tanda_name = update.message.text
    context.user_data[TANDA_NAME] = tanda_name
    print(f"Tanda name given from {user.first_name}: {tanda_name}")
    await update.message.reply_text(
        STRINGS["commands"]["create"]["get_participants"],
    )

    return TANDA_PARTICIPANTS


def clean_participants(participants: list[str]) -> list[str]:
    """
        Removes empty strings from the participants list.
    """
    clean_participants = []
    for participant in participants:
        if participant != "":
            temp = participant.strip().capitalize()
            clean_participants.append(temp)

    return clean_participants


async def get_tanda_participants(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
        Stores the tanda participants given from the user.
    """
    user = update.message.from_user
    tanda_participants = update.message.text.split(",")
    context.user_data[TANDA_PARTICIPANTS] = clean_participants(
        tanda_participants)

    print(
        f"Tanda participants given from {user.first_name}: {tanda_participants}")
    await update.message.reply_text(
        STRINGS["commands"]["create"]["get_amount"],
    )

    return TANDA_AMOUNT


async def get_tanda_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
        Stores the tanda amount given from the user.
    """
    user = update.message.from_user
    tanda_amount = update.message.text.split()[0]

    if "$" in tanda_amount:
        tanda_amount = tanda_amount.replace("$", "")

    if not tanda_amount.isnumeric():
        await update.message.reply_text(
            STRINGS["commands"]["create"]["invalid_amount"],
        )
        return ConversationHandler.END

    context.user_data[TANDA_AMOUNT] = float(tanda_amount)

    print(f"Tanda amount given from {user.first_name}: {tanda_amount}")
    await update.message.reply_text(
        STRINGS["commands"]["create"]["get_period"],
    )

    return TANDA_PERIOD


async def get_tanda_period(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
        Stores the tanda period given from the user.
    """
    user = update.message.from_user
    tanda_period = update.message.text.split()[0]

    if not tanda_period.isnumeric():
        await update.message.reply_text(
            STRINGS["commands"]["create"]["invalid_period"],
        )
        return ConversationHandler.END

    context.user_data[TANDA_PERIOD] = int(tanda_period)

    print(f"Tanda period given from {user.first_name}: {tanda_period}")

    # Retrieve the previously stored information from context
    tanda_name = context.user_data.get(TANDA_NAME)
    tanda_participants = context.user_data.get(TANDA_PARTICIPANTS)
    tanda_amount = context.user_data.get(TANDA_AMOUNT)

    # Create the tanda object
    tanda = Tanda(tanda_name, tanda_participants,
                  tanda_amount, int(tanda_period))

    print("ALL DATA", tanda.name, tanda.participants,
          tanda.amount, tanda.period, tanda.total_amount)

    done_string: str = STRINGS["commands"]["create"]["done"]

    await update.message.reply_text(
        done_string.format(name=tanda_name),
    )

    return ConversationHandler.END


async def cancel_create_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    print(f"User {user.first_name} canceled the tanda creation command.")
    await update.message.reply_text(
        STRINGS["commands"]["create"]["cancel"], reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
