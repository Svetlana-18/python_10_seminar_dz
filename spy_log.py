from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def log_command(update: Update, context: CallbackContext, text):
    file = open('C:\\Users\\vasil\\Documents\\репозитории\\python_10_seminar_dz\\db.csv', 'a', encoding='UTF-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {text}\n')
    file.close()
