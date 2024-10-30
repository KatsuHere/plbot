# bot.py

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from plugins.start import start
from plugins.callback import handle_callback
from config import BOT_TOKEN

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_callback))

    updater.start_polling()
    updater.idle()
