from telegram import Update
from telegram.ext import ContextTypes, ApplicationHandlerStop
from filters.auth import auth

async def blockUnauthorized(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if auth(update): return;

    print('BLOCKED');
    raise ApplicationHandlerStop;
