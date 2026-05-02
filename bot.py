import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8439027423:AAEJ3-U46m7Ff2GyR1SCdDx6DQsA22uDbUg"  
URL = "https://vvvladmir2-coder.github.io/prodyus/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает команду /start, если перешли с параметром open – показывает кнопку с Web App."""
    if update.message and update.message.text and "open" in update.message.text:
        keyboard = [[InlineKeyboardButton(
            text="🚀 Открыть лендинг",
            web_app=WebAppInfo(url=URL)
        )]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Жми кнопку ниже, чтобы открыть предложение:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Привет! Я бот-визитка. Используй ссылку с ?startapp=open")

def main() -> None:
    """Запуск бота."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    logger.info("Бот запущен и готов к работе!")
    application.run_polling()

if __name__ == "__main__":
    main()
