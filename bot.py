# bot.py

import logging
import subprocess
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from plugins.start import start
from plugins.callback import handle_callback
from config import BOT_TOKEN

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def update_repo(update, context):
    """Handle the /update command to pull the latest changes from the repo."""
    try:
        logging.info("Updating the repository...")
        # Run the git pull command
        result = subprocess.run(
            ["git", "pull", "https://github.com/KatsuHere/plbot"], 
            capture_output=True, text=True
        )
        
        # Check if the update was successful
        if result.returncode == 0:
            update.message.reply_text("Repository updated successfully:\n" + result.stdout)
        else:
            update.message.reply_text("Error updating the repository:\n" + result.stderr)
    except Exception as e:
        logging.error("Failed to update repository: %s", e)
        update.message.reply_text("Failed to update repository.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("update", update_repo))  # Add the update command handler
    dp.add_handler(CallbackQueryHandler(handle_callback))

    logging.info("Starting bot...")
    updater.start_polling()
    updater.idle()
