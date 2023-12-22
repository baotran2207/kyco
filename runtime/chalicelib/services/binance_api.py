import hashlib
import hmac
import json
import time
from dataclasses import dataclass
from datetime import date

import requests
from binance.spot import Spot
from chalicelib.config import settings

default_kargs = {"rows": 100}

from chalicelib.schemas.binance import (
    BinanceP2PRecord,
    EarnAsset,
    EarnAssets,
    P2PRecord,
)
from icecream import ic


class LendingType:
    DAILY = "DAILY"
    ACTIVITY = "ACTIVITY"
    CUSTOMIZED_FIXED = "CUSTOMIZED_FIXED"


class OrderStatus:
    COMPLETED = "COMPLETED"


@dataclass
class BinanceExchange:
    client: Spot

    def get_p2p_overview(self):
        pass

    def get_savings_account(self) -> EarnAssets:
        raw_data = self.client.get_flexible_product_position()

        earn_assets = []
        for row in raw_data.get("rows"):
            if row.get("asset") == "USDT":
                token_price = 1
            else:
                token_price = self.client.ticker_price(
                    symbol=[row.get("asset") + "USDT"]
                ).get("price", 0)

            earn_asset = EarnAsset(current_price=token_price, **row)
            earn_assets.append(earn_asset)

        return EarnAssets(earn_assets=earn_assets)

    def get_p2p_price(self, fiat="VND"):
        pass

    def get_tokens_price(self, token_pairs: list):
        return client.ticker_price(symbols=token_pairs)

    def get_p2p_records(self) -> list[BinanceP2PRecord]:
        buy_records_raw = self.client.c2c_trade_history("BUY", **{"rows": 100})["data"]
        sell_records_raw = self.client.c2c_trade_history("SELL", **{"rows": 100})[
            "data"
        ]

        binance_p2p_records = [
            BinanceP2PRecord(**sell_record)
            for sell_record in buy_records_raw + sell_records_raw
        ]
        return [
            p2precord
            for p2precord in binance_p2p_records
            if p2precord.order_status == OrderStatus.COMPLETED
        ]

    @staticmethod
    def get_p2p_pricing():
        data = {
            "asset": "USDT",
            "fiat": "VND",
            "merchantCheck": True,
            "page": 1,
            "payTypes": ["BANK"],
            "publisherType": None,
            "rows": 5,
            "tradeType": "BUY",
        }
        r = requests.post(
            "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search",
            # headers=headers,
            json=data,
        )
        raw = r.json()
        data = raw.get("data")
        first_pricing = data[0]["adv"].get("price")
        return first_pricing


binance_api_key = settings.BINANCE_API_KEY
binance_api_secret = settings.BINANCE_API_SECRET

client = Spot(binance_api_key, binance_api_secret)
bnb_ex = BinanceExchange(client)
bnb_client = bnb_ex
