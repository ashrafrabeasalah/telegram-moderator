BAD_WORDS = [
    "spam",
    "scam",
    "idiot",
    "fuck"
]

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for word in BAD_WORDS:
        if word in text:
            await update.message.delete()

            await update.effective_chat.send_message(
                f"⚠️ {update.effective_user.first_name}, inappropriate language is not allowed."
            )
            return
