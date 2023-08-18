import csv
import io
import itertools
from datetime import datetime
from functools import reduce
from pprint import pprint

import requests
from chalicelib.config import settings
from chalicelib.db.session import SessionLocal
from chalicelib.logger_app import logger
from chalicelib.models.porfolio import DepositRecords
from chalicelib.services.binance_api import bnb_ex
from chalicelib.services.s3_service import read_s3_object
from chalicelib.utils import to_snake_key
from sqlalchemy.sql import functions


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


def read_history_records(
    s3_bucket: str,
    s3_object_path: str,
):
    body = read_s3_object(s3_bucket, s3_object_path)
    lines = body.decode("utf-8")
    buf = io.StringIO(lines)
    reader = csv.DictReader(buf)
    rows = list(reader)
    return rows


def update_p2p_history_records():
    history_orders = read_history_records(
        settings.S3_MAIN_BUCKET,
        "binance/c2c/binance_2021_2022.csv",
    )

    orders = [
        {to_snake_key(k): v for k, v in order.items()}
        | {"created_time": datetime.strptime(order.get("Created Time"), "%Y-%m-%d %H:%M:%S")}
        for order in history_orders
    ]

    return update_p2p_records(orders)


def update_bnb_p2p_records():
    recent_orders = bnb_ex.get_p2p_records()
    to_update_orders = []

    for order in recent_orders:
        to_update_orders.append(
            dict(
                order_number=order.get("orderNumber"),
                order_type=order.get("tradeType"),
                asset_type=order.get("asset"),
                fiat_type=order.get("fiat"),
                total_price=order.get("totalPrice"),
                price=order.get("unitPrice"),
                quantity=order.get("amount"),
                status=order.get("orderStatus").capitalize(),
                created_time=datetime.fromtimestamp(order.get("createTime") / 1e3),
            )
        )

    return update_p2p_records(reversed(to_update_orders))


def update_p2p_records(orders: list):
    db = SessionLocal()
    query_result = db.query(DepositRecords.order_number).all()
    exists_order_numbers = list(itertools.chain(*query_result))

    new_orders = (
        order for order in orders if order.get("order_number") not in exists_order_numbers
    )

    cols = DepositRecords.__table__.columns.keys()
    added_order_numbers = []
    for order in new_orders:
        order_db = DepositRecords(
            order_number=str(order.get("order_number")),
            order_type=order.get("order_type").capitalize(),
            asset_type=order.get("asset_type"),
            fiat_type=order.get("fiat_type"),
            total_price=order.get("total_price"),
            price=order.get("price"),
            quantity=order.get("quantity"),
            exchange_rate=order.get("exchange_rate"),
            order_status=order.get("status").capitalize(),
            created_time=order.get("created_time"),
        )
        db.add(order_db)
        logger.info(
            f"Adding p2p new order to db {order_db.order_number} - created time {order_db.created_time}"
        )

        added_order_numbers.append(
            {
                "order_number": order_db.order_number,
                "created_time ": order_db.created_time,
            }
        )

    db.commit()
    return added_order_numbers


def deposit_overview():
    db = SessionLocal()
    query = (
        db.query(
            DepositRecords.order_type,
            functions.sum(DepositRecords.quantity.label("total_usd")),
            functions.sum(DepositRecords.total_price.label("total_vnd")),
        )
        .group_by(DepositRecords.order_type)
        .order_by(DepositRecords.order_type)
        .all()
    )
    buy_capital, sell_capital = query
    capital_usd = buy_capital[1] - sell_capital[1]
    capital_vnd = buy_capital[2] - sell_capital[2]

    return {
        "capital_usd": capital_usd,
        "capital_vnd": capital_vnd,
        "average_capital_price": int(capital_vnd / capital_usd),
        "total_buy_usd": buy_capital[1],
        "total_buy_vnd": buy_capital[2],
        "total_sell_usd": sell_capital[1],
        "total_sell_vnd": sell_capital[2],
        "average_buy_price": int(buy_capital[2] / buy_capital[1]),
        "average_sell_price": int(sell_capital[2] / sell_capital[1]),
    }


def get_funding_overview():
    current_assets = get_saving_accounts_overview()
    assets_amount = current_assets["positionAmountVos"]
    current_assets_usd = float(current_assets["totalAmountInUSDT"])

    current_statable_assets = current_assets["totalAmountInUSDT"]
    stables_amount = sum(
        [
            float(asset.get("amount", 0))
            for asset in assets_amount
            if asset["asset"] in ["USDT", "BUSD", "USDC", "DAI"]
        ]
    )

    current_usd_price = float(get_p2p_pricing())
    current_assets_vnd = current_usd_price * current_assets_usd

    deposits = deposit_overview()
    capital_usd = deposits["capital_usd"]
    capital_vnd = deposits["capital_vnd"]
    capital_usd_deployed = capital_usd - stables_amount
    capital_vnd_deployed = capital_usd_deployed * current_usd_price

    pnl_usd = current_assets_usd / capital_usd
    pnl_vnd = current_assets_vnd / capital_vnd

    position_pnl_usd = (current_assets_usd - stables_amount) / capital_usd_deployed
    position_pnl_vnd = (
        current_assets_vnd - stables_amount * current_usd_price
    ) / capital_vnd_deployed

    link_price = float(get_token_price(["LINKUSDT"])[0].get("price"))
    link_price_breakevent = round(link_price / (position_pnl_usd), 1)
    link_position = current_assets.get("positionAmountVos")[0]
    link_position_value = round(float(link_position.get("amountInUSDT")))
    link_position_amount = float(link_position.get("amount"))

    return {
        "current_amount_in_vnd": current_assets_vnd,
        "current_amount_in_usd": current_assets_usd,
        "capital_usd_deployed": capital_usd_deployed,
        "capital_vnd_deployed": capital_vnd_deployed,
        "stables_amount": stables_amount,
        "PNL": {
            "pnl_in_vnd": f"{pnl_vnd:,.2%}",
            "pnl_in_usd": f"{pnl_usd:,.2%}",
            "position_pnl_usd": f"{position_pnl_usd:,.2%}",
            "position_pnl_vnd": f"{position_pnl_vnd:,.2%}",
        },
        "current_usd_price": current_usd_price,
        "current_assets": current_assets,
        "deposits": deposits,
        "link_price": round(link_price, 1),
        "link_price_breakevent": link_price_breakevent,
        "link_position_value": link_position_value,
        "link_position_amount": link_position_amount,
    }
