import requests
import time
import telegram
import os


COINGLASS_API_KEY = "5c1ec8ed34f842ea89eb770c44a43a2f"


TELEGRAM_BOT_TOKEN = "7181559765:AAGAr04ECDvpveY5CaW-n2iHmV4xO1JxPRs"
TELEGRAM_CHAT_ID = "1727521702"

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def fetch_data():
    headers = {
        'accept': 'application/json',
        'coinglassSecret': COINGLASS_API_KEY
    }
    url = "https://open-api.coinglass.com/public/v2/futures/longShortRate?symbol=BTC"
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        btc_data = data["data"]["BTCUSDT"]
        long_rate = btc_data["longRate"]
        short_rate = btc_data["shortRate"]

        message = f"📊 BTC Long/Short Signal (15min)\n\n"
        if float(long_rate) > float(short_rate):
            direction = "📈 LONG"
        else:
            direction = "📉 SHORT"

        message += f"Signal: {direction}\nLong Rate: {long_rate}\nShort Rate: {short_rate}\n\n"
        message += f"TP 🎯: Dynamic based\nSL 🛑: Structure Based\n\n#BTC #Signal #Crypto"

        return message

    except Exception as e:
        return f"❌ Error fetching data: {e}"

def run_bot():
    while True:
        signal = fetch_data()
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=signal)
        time.sleep(900)  # 15 minutes

if __name__ == "__main__":
    run_bot()
