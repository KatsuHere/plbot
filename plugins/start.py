# plugins/start.py

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from config import LOGO_URL

def start(update, context):
    chat_id = update.message.chat_id

    context.bot.send_photo(
        chat_id=chat_id,
        photo=LOGO_URL,
        caption="Selamat datang! Pilih produk yang Anda inginkan:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("VPS", callback_data="vps")],
            [InlineKeyboardButton("Userbot", callback_data="userbot")],
            [InlineKeyboardButton("Bot Fsub", callback_data="bot_fsub")]
        ])
    )
