from telegram.ext import Updater, CommandHandler

# جایگزین کن با توکن واقعی
TOKEN = "7541973947:AAEw7idIjFKPobs4AN-sr1iKXfqzkPT-7_M"

def start(update, context):
    update.message.reply_text("سلام! من یه ربات تلگرام ساده‌ام.")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
