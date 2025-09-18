from flask import Flask, request
import requests

app = Flask(__name__)

# Token bot Telegram dan chat id group
BOT_TOKEN = "8208178189:AAG8HYOLEhTzmmr2-Pzwyi0wxm77s1ErCEQ"
CHAT_ID = "859152762"

# Endpoint webhook dari TradingView
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return {"status": "error", "message": "No data received"}, 400

    # Pesan yang akan dikirim ke Telegram
    message = f"📢 TradingView Alert:\n{data}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            return {"status": "success", "message": "Alert sent to Telegram!"}, 200
        else:
            return {"status": "error", "message": r.text}, 500
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

@app.route('/')
def home():
    return "🚀 Bot is running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
