# plugins/callback.py

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from plugins.data import DataProduk, Pay

def handle_callback(update, context):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    if data == "vps":
        context.bot.edit_message_caption(
            chat_id=chat_id,
            message_id=message_id,
            caption="\n".join(DataProduk.pricelist_vps),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("‹", callback_data="main_menu"), InlineKeyboardButton("×", callback_data="close")]
            ])
        )

    elif data == "userbot":
        context.bot.edit_message_caption(
            chat_id=chat_id,
            message_id=message_id,
            caption="Daftar Harga Userbot:\n" + "\n".join(DataProduk.pricelist_userbot),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("‹", callback_data="main_menu"), InlineKeyboardButton("×", callback_data="close")]
            ])
        )

    elif data == "bot_fsub":
        context.bot.edit_message_caption(
            chat_id=chat_id,
            message_id=message_id,
            caption="Daftar Harga Bot Fsub:\n" + "\n".join(DataProduk.pricelist_bot_fsub),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("‹", callback_data="main_menu"), InlineKeyboardButton("×", callback_data="close")]
            ])
        )

    elif data == "payment":
        context.bot.edit_message_caption(
            chat_id=chat_id,
            message_id=message_id,
            caption=Pay.payment_info,
            parse_mode=ParseMode.MARKDOWN,
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
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("VPS", callback_data="vps"), InlineKeyboardButton("Userbot", callback_data="userbot")],
            [InlineKeyboardButton("Bot Fsub", callback_data="bot_fsub")],
            [InlineKeyboardButton("Pembayaran", callback_data="payment")]  # Tombol Pembayaran di main menu
        ])
    )
