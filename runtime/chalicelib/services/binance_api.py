import hashlib
import hmac
import json
import time
from dataclasses import dataclass
from datetime import date
from pprint import pprint

import requests
from binance.spot import Spot
from chalicelib.config import settings

default_kargs = {"rows": 100}


class LendingType:
    DAILY = "DAILY"
    ACTIVITY = "ACTIVITY"
    CUSTOMIZED_FIXED = "CUSTOMIZED_FIXED"


class OrderStatus:
    COMPLETED = "COMPLETED"


@dataclass
class BinanceExchange:
    client: Spot

    def get_p2p_overview():
        pass

    def get_saving_accounts_overview(self):
        return self.client.savings_account()

    def get_p2p_price(self, fiat="VND"):
        pass

    def get_tokens_price(self, token_pairs: list):
        return client.ticker_price(symbols=token_pairs)

    def get_p2p_records(self):
        buy_records = client.c2c_trade_history("BUY", **{"rows": 100})["data"]
        sell_records = client.c2c_trade_history("SELL", **{"rows": 100})["data"]

        return [
            rec
            for rec in buy_records + sell_records
            if rec.get("orderStatus") == OrderStatus.COMPLETED
        ]


binance_api_key = settings.BINANCE_API_KEY
binance_api_secret = settings.BINANCE_API_SECRET

client = Spot(binance_api_key, binance_api_secret)
bnb_ex = BinanceExchange(client)
