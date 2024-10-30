# bot.py

import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from plugins.start import start
from plugins.callback import handle_callback
from config import BOT_TOKEN

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_callback))

    logging.info("Starting bot...")
    updater.start_polling()
    updater.idle()
