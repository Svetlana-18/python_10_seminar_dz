from telegram import Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from bot_commands import *


updater = Updater("5605526481:AAG9tx5MzA09nYUkPHA8Z_zkPtrpzmdg42M")

updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('program', program_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('sub', sub_command))
updater.dispatcher.add_handler(CommandHandler('mul', mul_command))
updater.dispatcher.add_handler(CommandHandler('div', div_command))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel_command))



updater.dispatcher.add_handler(MessageHandler(Filters.text, analize_command))

print ('bot start')
updater.start_polling()
updater.idle()
