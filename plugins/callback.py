# plugins/callback.py

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.data import DataProduk

def handle_callback(update, context):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    # Tombol utama
    if data == "vps":
        context.bot.edit_message_caption(
            chat_id=chat_id,
            message_id=message_id,
            caption="Daftar Harga VPS:\n" + "\n".join(DataProduk.pricelist_vps),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("‹", callback_data="main_menu"), InlineKeyboardButton("×", callback_data="close")]
            ])
        )

    elif data == "userbot":
        context.bot.edit_message_caption(
            chat_id=chat_id,
            message_id=message_id,
            caption="Daftar Harga Userbot:\n" + "\n".join(DataProduk.pricelist_userbot),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("‹", callback_data="main_menu"), InlineKeyboardButton("×", callback_data="close")]
            ])
        )

    elif data == "bot_fsub":
        context.bot.edit_message_caption(
            chat_id=chat_id,
            message_id=message_id,
            caption="Daftar Harga Bot Fsub:\n" + "\n".join(DataProduk.pricelist_bot_fsub),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("‹", callback_data="main_menu"), InlineKeyboardButton("×", callback_data="close")]
            ])
        )

    elif data == "main_menu":
        show_main_menu(chat_id, message_id, context)

    elif data == "close":
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)


def show_main_menu(chat_id, message_id, context):
    context.bot.edit_message_caption(
        chat_id=chat_id,
        message_id=message_id,
        caption="Pilih pricelist yang diinginkan:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("VPS", callback_data="vps")],
            [InlineKeyboardButton("Userbot", callback_data="userbot")],
            [InlineKeyboardButton("Bot Fsub", callback_data="bot_fsub")]
        ])
    )
