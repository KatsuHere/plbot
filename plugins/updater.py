import os
import subprocess
import time
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update

# Fungsi untuk memperbarui repositori dan merestart bot
def update_repo(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id

    # Mengirimkan pesan bahwa proses pembaruan sedang berlangsung
    context.bot.send_message(chat_id=chat_id, text="Memperbarui repositori...")

    # Perintah untuk memperbarui repositori
    try:
        # Menjalankan git pull
        subprocess.run(["git", "pull"], check=True)
        
        # Mengirim pesan bahwa pembaruan berhasil
        context.bot.send_message(chat_id=chat_id, text="Pembaruan berhasil. Restarting bot...")
        
        # Restart bot (menggunakan perintah bash untuk menjalankan start.sh)
        subprocess.Popen(["bash", "start"], shell=False)
        
        # Memberitahu pengguna bahwa bot sedang di-restart
        context.bot.send_message(chat_id=chat_id, text="Bot sedang di-restart...")
    except subprocess.CalledProcessError as e:
        # Jika terjadi error, beri tahu pengguna
        context.bot.send_message(chat_id=chat_id, text=f"Error saat memperbarui repositori: {str(e)}")

# Daftar command handler
def main(dispatcher):
    dispatcher.add_handler(CommandHandler("update", update_repo))
