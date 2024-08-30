from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN' with your bot token
TOKEN = 'YOUR_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is alive')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
