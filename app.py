from flask import Flask, request
import requests

app = Flask(__name__)

# আপনার টেলিগ্রাম ডিটেইলস
BOT_TOKEN = "8772565875:AAHyDH-063rlJoEoO5vvrEVnUtRQoTsHIdA"
CHAT_ID = "-1003833319917"

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # TradingView থেকে আসা মেসেজ রিসিভ করা
        data = request.data.decode('utf-8')
        send_telegram_msg(data)
        return "Success", 200
    else:
        return "Method Not Allowed", 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
