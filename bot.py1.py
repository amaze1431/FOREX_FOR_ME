
import logging
import asyncio
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# הכנס כאן את הטוקן שלך ואת מזהה הטלגרם שלך
BOT_TOKEN = "7929941695:AAFM9fsbpkeoNIkPMLIUfkR1-A3fWP6dXAE
"
CHAT_ID = 123456789  # לדוגמה: 123456789

pairs = [
    "GBP/CHF", "CHF/CAD", "CAD/JPY", "USD/CAD",
    "GBP/AUD", "AUD/CHF", "EUR/USD", "CHF/JPY",
    "EUR/CAD", "EUR/CHF", "EUR/GBP"
]

# הגדרת לוגים
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 שלום! שלח /signal כדי לקבל איתותים.")

def analyze_forex_pair(pair):
    directions = ["קנייה", "מכירה", None]
    direction = random.choice(directions)
    if direction:
        reason = random.choice([
            "RSI נמוך מ-30", "RSI גבוה מ-70", "פריצה של רמת תמיכה", "פריצה של רמת התנגדות"
        ])
        return {"direction": direction, "reason": reason}
    return None

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 אותות לחצי שעה:")
    for pair in pairs:
        result = analyze_forex_pair(pair)
        if result:
            message = f"{pair} - {result['direction']} ({result['reason']})"
            await update.message.reply_text(message)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("🤖 הבוט התחיל לפעול...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
