from telegram import Update;
from telegram.ext import ContextTypes;

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.name;

    await update.message.reply_text(f'Olá, {username}');