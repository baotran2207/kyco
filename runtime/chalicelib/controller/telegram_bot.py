from dataclasses import dataclass
from typing import Protocol

import requests
from chalicelib.config import settings
from chalicelib.controller.wallet import binance_controller
from chalicelib.enums import TelegramCommands
from loguru import logger

BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN

help_message = """
Hello, supported TelegramCommands:
/start
/help
/portfolio_dashboard
"""


class ReplyMessage(Protocol):
    def render(*arg, **kwargs):
        ...


class StartReplyMessage(ReplyMessage):
    def render():
        text = help_message
        return text


class HelpReplyMessage(ReplyMessage):
    def render():
        return help_message


class PorfolioDashboardReplyMessage(ReplyMessage):
    def render():
        raw_response = binance_controller.get_funding_overview()
        text = """
Chainlink
- Amount: {link_position_amount}
- Current price: {link_price}
- average buy at: {link_price_breakevent}
    ({capital_usd_deployed} - {capital_vnd_deployed})

Deposit
- Total deposit: {deposit_usd}
    ({deposit_vnd})
- Average buy price: {average_buy_price}
- Current price: {current_usd_price}
- Stables amount: {stables_amount}
    ({stables_amount_vnd})
- Current values: {value_in_usd}
    ({value_in_vnd})

PNL
- PNL Total: {pnl_in_usd} -  ({pnl_in_vnd})
- PNL position : {position_pnl_usd} - ({position_pnl_vnd})
""".format(
            **raw_response
        )
        return text


REPLY_MESSAGE_HANDLERS = {
    TelegramCommands.START.value: StartReplyMessage,
    TelegramCommands.HELP.value: HelpReplyMessage,
    TelegramCommands.PORTFOLIO_DASHBOARD.value: PorfolioDashboardReplyMessage,
}


@dataclass
class TelegramBotController:
    URL: str = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    def send_message(self, chat_id: int, text: str):
        payload = {
            "chat_id": chat_id,
            "text": text,
        }
        res = requests.post(self.URL, data=payload)
        return res.json()

    def is_command(self, origin_text: str):
        return origin_text.startswith("/")

    def get_reply_message(self, origin_text: str) -> str:
        if not self.is_command(origin_text):
            return help_message

        command = origin_text.split(" ")[0].replace("/", "")
        if command not in REPLY_MESSAGE_HANDLERS:
            return help_message
        handler = REPLY_MESSAGE_HANDLERS.get(command)
        return handler.render()

    def reply(self, chat_id: int, origin_text: str):
        reply_message = self.get_reply_message(origin_text)
        return self.send_message(chat_id, reply_message)
