from telegram import Update;
from dotenv import load_dotenv; load_dotenv();
import os;

ALLOWED_USER_ID = int(os.getenv('OWNER_ID'));

def auth(update: Update) -> bool:
    user = update.effective_user;
    print(f'ID usuário: {user.id if user else None} ');
    print(f'Nome usuário: {user.name}');
    return bool(user and user.id == ALLOWED_USER_ID);
