import hashlib
import hmac
import json
import time

import requests
from chalicelib.config import settings

uri = "https://api.binance.com"
binance_api_key = settings.BINANCE_API_KEY
binance_api_secret = settings.BINANCE_API_SECRET


def get_timestamp_offset():
    url = "{}/api/v3/time".format(uri)

    payload = {}
    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)["serverTime"] - int(time.time() * 1000)


def generate_signature(query_string):
    binance_api_secret_encoded = (
        binance_api_secret
        if isinstance(binance_api_secret, bytes)
        else binance_api_secret.encode("utf-8")
    )
    m = hmac.new(
        binance_api_secret_encoded, query_string.encode("utf-8"), hashlib.sha256
    )
    return m.hexdigest()


def get_flexible_savings_balance(asset):
    timestamp = int(time.time() * 1000 + get_timestamp_offset())
    query_string = "asset={}&timestamp={}".format(asset, timestamp)
    signature = generate_signature(query_string)

    url = "{}/sapi/v1/lending/daily/token/position?{}&signature={}".format(
        uri, query_string, signature
    )

    payload = {}
    headers = {"Content-Type": "application/json", "X-MBX-APIKEY": binance_api_key}

    response = json.loads(
        requests.request("GET", url, headers=headers, data=payload).text
    )
    print(response)
    return response


def get_locked_savings_balance(asset, project_id):
    timestamp = int(time.time() * 1000 + get_timestamp_offset())
    query_string = "asset={}&projectId={}&status=HOLDING&timestamp={}".format(
        asset, project_id, timestamp
    )
    signature = generate_signature(query_string)

    url = "{}/sapi/v1/lending/project/position/list?{}&signature={}".format(
        uri, query_string, signature
    )

    payload = {}
    headers = {"Content-Type": "application/json", "X-MBX-APIKEY": binance_api_key}

    return json.loads(requests.request("GET", url, headers=headers, data=payload).text)


def get_token_price(asset, stable_coin="USDT") -> float:
    """
    https://api.binance.com/api/v3/ticker/price?symbol=BTCBUSD
    """
    if asset == stable_coin:
        return 1
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={asset}{stable_coin}"
    res = json.loads(
        requests.request("GET", url, headers={"Content-Type": "application/json"}).text
    )
    return res.get("price")


def get_p2p_price(asset, currency) -> float:
    pass
