# bot.py

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from plugins.start import start
from plugins.callback import handle_callback
from plugins.updater import main as updater_main  # Import updater
from config import BOT_TOKEN

def main():
    # Membuat instance Updater
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Menambahkan handler untuk perintah /start
    dp.add_handler(CommandHandler("start", start))

    # Menambahkan handler untuk callback query
    dp.add_handler(CallbackQueryHandler(handle_callback))

    # Menambahkan handler untuk perintah /update
    updater_main(dp)  # Memanggil fungsi updater_main untuk menambahkan handler update

    # Memulai polling
    updater.start_polling()
    # Menunggu sampai bot dihentikan
    updater.idle()

if __name__ == '__main__':
    main()
