import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8439027423:AAE4VGqFfTMgXfOkueDKEWev3b0-xM9371g"
URL = "https://vvvladmir2-coder.github.io/prodyus/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text and "open" in update.message.text:
        keyboard = [[InlineKeyboardButton(
            text="🚀 Открыть лендинг",
            web_app=WebAppInfo(url=URL)
        )]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Жми кнопку ниже:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Привет! Используй ссылку с ?startapp=open")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
