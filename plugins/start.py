# plugins/start.py

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext, CommandHandler
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

def id_command(update: Update, context: CallbackContext):
    """Mengirimkan ID pengguna, nama lengkap, dan username pengguna."""
    user = update.effective_user
    user_id = user.id
    full_name = user.full_name
    username = user.username if user.username else "Tidak ada username"

    # Membuat pesan dengan informasi pengguna
    message = (
        f"**Informasi Pengguna**:\n"
        f"**User ID**: {user_id}\n"
        f"**Nama Lengkap**: {full_name}\n"
        f"**Username**: @{username}"
    )

    # Mengirimkan pesan kepada pengguna
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')

# Pastikan untuk menambahkan handler untuk perintah /id di tempat yang sesuai di bot.py
