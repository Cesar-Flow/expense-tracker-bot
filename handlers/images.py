from telegram import Update;
from telegram.ext import ContextTypes;
from pathlib import Path;

IMAGES_DIR = Path('tempImages');
IMAGES_DIR.mkdir(exist_ok=True);

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user;
    photo = update.message.photo[-1];

    file = await photo.get_file();
    file_path = IMAGES_DIR / f'{user.id}.jpg';

    await file.download_to_drive(file_path);

    await update.message.reply_text('📸 Analisando...');
