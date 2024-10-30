# plugins/start.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.constants import ParseMode
from telegram.ext import CallbackContext
from config import BOT_LOGO_URL, OWNER_USERNAME
from plugins.data import DataProduk

def start(update, context: CallbackContext):
    chat_id = update.effective_chat.id

    # Tampilkan animasi "typing..." sebelum menampilkan konten
    context.bot.send_chat_action(chat_id=chat_id, action="typing")
    
    # Kirim pesan animasi "Starting bot..." secara bertahap
    typing_text = "Starting bot..."
    for i in range(len(typing_text) + 1):
        context.bot.send_message(chat_id=chat_id, text=typing_text[:i])
        context.bot.send_chat_action(chat_id=chat_id, action="typing")
        time.sleep(0.1)  # jeda antar karakter untuk efek mengetik

    # Hapus pesan terakhir (untuk mengganti dengan konten utama)
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id + len(typing_text) + 1)
    
    # Menampilkan logo, caption, dan tombol setelah animasi selesai
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
        photo=BOT_LOGO_URL,
        caption=caption_text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )
