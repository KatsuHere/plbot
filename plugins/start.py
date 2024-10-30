# plugins/start.py

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext
from config import LOGO_URL  # Pastikan LOGO_URL didefinisikan di config.py
from plugins.callback import show_main_menu

def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id

    # Mengirimkan pesan dengan gambar logo dan tombol menu
    context.bot.send_photo(
        chat_id=chat_id,
        photo=LOGO_URL,
        caption="Selamat datang di Bot Pricelist! Pilih salah satu opsi di bawah untuk melihat daftar harga:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("VPS", callback_data="vps"), InlineKeyboardButton("Userbot", callback_data="userbot")],
            [InlineKeyboardButton("Bot Fsub", callback_data="bot_fsub")],
            [InlineKeyboardButton("Pembayaran", callback_data="payment")]  # Tombol Pembayaran ditambahkan di sini
        ])
    )
