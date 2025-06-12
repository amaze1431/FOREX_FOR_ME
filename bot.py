
import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 7929941695:AAFM9fsbpkeoNIkPMLIUfkR1-A3fWP6dXAE


pairs = [
    "GBP/CHF", "CHF/CAD", "CAD/JPY", "USD/CAD", "GBP/AUD", "AUD/CHF",
    "EUR/USD", "CHF/JPY", "EUR/CAD", "EUR/CHF", "EUR/GBP"
]

reasons = [
    "RSI נמוך מ-30", "RSI גבוה מ-70", "פריצה של רמת תמיכה",
    "פריצה של רמת התנגדות", "תבנית ראש וכתפיים", "ספל וידית"
]

logging.basicConfig(level=logging.INFO)

async def send_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signals = []
    for pair in pairs:
        if random.random() > 0.5:  # בערך חצי מהפעמים ייתן איתות
            direction = random.choice(["קנייה", "מכירה"])
            reason = random.choice(reasons)
            signals.append(f"{pair}: {direction} – {reason}")

    if signals:
        await update.message.reply_text("📊 אותות לחצי שעה:
" + "\n".join(signals))
    else:
        await update.message.reply_text("אין אותות כרגע.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("signal", send_signal))
    app.run_polling()
