from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your bot token
TOKEN = 'YOUR_BOT_TOKEN'

# List of required channel usernames
CHANNELS = [
    '@your_channel_username1',  # Replace with actual channel usernames
    '@your_channel_username2'
]

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = update.message.chat_id

    # Check if user is a member of all required channels
    if check_channels_membership(user.id):
        update.message.reply_text('Welcome! You are a member of the required channels.')
    else:
        update.message.reply_text('You must join the required channels to use this bot.')

def check_channels_membership(user_id: int) -> bool:
    """
    Check if the user is a member of all required channels.
    """
    for channel in CHANNELS:
        try:
            member = context.bot.get_chat_administrators(channel)
            if user_id not in [admin.user.id for admin in member]:
                return False
        except Exception as e:
            logger.error(f"Error checking channel membership: {e}")
            return False
    return True

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()