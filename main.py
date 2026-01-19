from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    TypeHandler,
    filters,
)

from dotenv import load_dotenv;
import os;

# Handlers
from handlers.start import start
from handlers import images
from handlers.unauthorized import blockUnauthorized

load_dotenv();

TOKEN = os.getenv('TELEGRAM_TOKEN');


def main():
    app = ApplicationBuilder().token(TOKEN).build();

    # FIREWALL
    app.add_handler(
        TypeHandler(Update, blockUnauthorized),
        group=0
    );

    app.add_handler(
        CommandHandler('start', start),
        group=1
    );

    app.add_handler(
        MessageHandler(filters.PHOTO, images),
        group=1
    );

    print('bot online');
    app.run_polling();


if __name__ == '__main__': main();
