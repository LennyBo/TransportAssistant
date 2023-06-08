

import urequests
from secret import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def send_message(text, token, chat_id):
    url = f"https://api.telegram.org/bot{token}"
    r = urequests.get(f"{url}/sendMessage?chat_id={chat_id}&text={text}")
    return r


def easyMessage(text):
    r = send_message(text, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID)
    return r
