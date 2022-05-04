import os
import dotenv
dotenv.load_dotenv()
import requests

def send_telegram_message(message):
    try:
        requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(os.environ.get('keyTelegram'), os.environ.get('idChatTelegram'), message))
    except Exception as ex:
        print(ex)