import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["BOT_TOKEN"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Moderator Bot is online!")


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong!")


async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)

    await update.message.reply_text(
        f"You wrote:\n{update.message.text}"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, check_message)
)

print("Bot started...")
app.run_polling()
