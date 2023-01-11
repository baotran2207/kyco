# from chalicelib.extenions import gc
from functools import reduce
from pprint import pprint

import requests
from chalicelib.services.binance_api import bnb_ex

# porfolio_gsheet_url = "https://docs.google.com/spreadsheets/d/1Pbe9OPHhrVdDnjOurrTtSbUbLIHk1LsE_3R6s5pDLSw/edit?pli=1#gid=1375167053"
# porfolio_sheet = gc.open_by_url(porfolio_gsheet_url)


def get_p2p_records():
    p2p_records = bnb_ex.get_p2p_records()

    return p2p_records


def get_p2p_overview():
    """
    https://binance-docs.github.io/apidocs/spot/en/#get-c2c-trade-history-user_data
    binance only return 30 days
    """
    p2p_records = bnb_ex.get_p2p_records()
    return {
        "records": p2p_records,
        "total_records": len(p2p_records),
    }


def get_saving_accounts_overview():
    return bnb_ex.get_saving_accounts_overview()


def get_token_price(token_pairs):
    return bnb_ex.get_tokens_price(token_pairs)


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
