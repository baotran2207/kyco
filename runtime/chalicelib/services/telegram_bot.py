# telegram_lib.py
import urllib.parse
import requests
import json
from dataclasses import dataclass
from chalicelib.config import settings


@datasclass
class TelegramBot:
    bot_token: str = settings.TELEGRAM_BOT_TOKEN
    chat_id: str | None = settings.TELEGRAM_CHAT_ID

    def get_updates(self):
        url = f"https://api.telegram.org/bot{self.bot_token}/getUpdates"
        return json.loads(requests.get(url).content)

    def send_message(self, message: str):
        encoded_message = urllib.parse.quote_plus(message)
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&parse_mode=Markdown&text={encoded_message}"
        return requests.get(url).status_code == 200


tele_bot = TelegramBot(
    bot_token=settings.TELEGRAM_BOT_TOKEN, chat_id=settings.TELEGRAM_CHAT_ID
)

tele_bot.get_updates()
