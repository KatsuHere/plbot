# plugins/start.py

import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext
from config import LOGO_URL, OWNER_USERNAME
from plugins.data import DataProduk

def start(update, context: CallbackContext):
    chat_id = update.effective_chat.id

    # Mulai dengan pesan pertama
    typing_text = "Starting Bot..."
    message = context.bot.send_message(chat_id=chat_id, text="S")
    
    # Update pesan secara bertahap untuk animasi teks
    for i in range(1, len(typing_text) + 1):
        time.sleep(0.2)  # jeda antar karakter untuk efek mengetik
        context.bot.edit_message_text(chat_id=chat_id, message_id=message.message_id, text=typing_text[:i])

    # Setelah animasi selesai, kirimkan gambar, caption, dan tombol
    keyboard = [
        [
            InlineKeyboardButton("Vps", callback_data="vps"),
            InlineKeyboardButton("Userbot", callback_data="userbot")
        ],
        [
            InlineKeyboardButton("Bot Fsub", callback_data="fsub")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    caption_text = "*Welcome to NyxianNetwork!*" \
                   "\nSilakan pilih layanan yang ingin Anda lihat harganya."

    # Mengirimkan pesan gambar, caption, dan tombol
    context.bot.send_photo(
        chat_id=chat_id,
        photo=LOGO_URL,
        caption=caption_text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN_V2
    )
