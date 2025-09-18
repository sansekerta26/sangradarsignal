import telebot
from flask import Flask, request
import os
from datetime import datetime

# === Konfigurasi Bot Telegram ===
BOT_TOKEN = 8208178189:AAG8HYOLEhTzmmr2-Pzwyi0wxm77s1ErCEQ
CHAT_ID = 859152762
bot = telebot.TeleBot(BOT_TOKEN)

# === Setup Flask ===
app = Flask(__name__)

# Endpoint root
@app.route('/')
def index():
    return "🚀 Bot is running and ready for TradingView Webhook!"

# Endpoint webhook dari TradingView / manual test
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)

    try:
        # Waktu UTC sekarang
        signal_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

        # Format pesan
        message = f"""
🚀 *Sang Radar Alert* 🚀

📊 *Pair:* {data.get('pair', 'N/A')}
🕒 *Timeframe:* {data.get('timeframe', 'N/A')}
📈 *Type:* {data.get('type', 'N/A')}
💰 *Entry Price:* {data.get('price', 'N/A')}

🎯 *Target 1:* {data.get('target1', 'N/A')}
🎯 *Target 2:* {data.get('target2', 'N/A')}
🛑 *Stop Loss:* {data.get('stoploss', 'N/A')}

⏱️ *Signal Time:* {signal_time}
"""
        # Kirim ke Telegram
        bot.send_message(CHAT_ID, message, parse_mode="Markdown")
        return {"status": "ok", "message": "Signal terkirim ke Telegram ✅"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

# Jalankan Flask (untuk lokal testing)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
