from chalice import Blueprint
from chalicelib.services.authorizers import chalice_authorizer
from chalicelib.services.email_sender import send_porfolio_overview
from chalicelib.logger_app import logger
from chalicelib.services.porfolio import (
    deposit_overview,
    get_p2p_overview,
    get_p2p_pricing,
    get_p2p_records,
    get_funding_overview,
    get_token_price,
    update_bnb_p2p_records,
    update_p2p_history_records,
    get_funding_overview,
)
import json

porfolio_bp = Blueprint(__name__)


@porfolio_bp.route("/assets", authorizer=chalice_authorizer)
def get_summary():
    return get_saving_accounts_overview()


@porfolio_bp.route("/trigger-update", methods=["GET"])
def trigger_update():
    his_res = update_p2p_history_records()

    orders = update_bnb_p2p_records()

    return "ok"


@porfolio_bp.route("/overview", authorizer=chalice_authorizer)
def get_funding_overview_route():
    funding_overview = get_funding_overview()

    position_pnl_usd = float(
        funding_overview["PNL"]["position_pnl_usd"].replace("%", "")
    )

    link_price = round(float(get_token_price(["LINKUSDT"])[0].get("price")), 1)
    link_price_breakevent = round(link_price / (position_pnl_usd * 0.01), 1)
    link_position = funding_overview.get("current_assets").get("positionAmountVos")[0]
    link_position_value = round(float(link_position.get("amountInUSDT")))
    link_position_amount = float(link_position.get("amount"))

    response = dict(
        funding_overview,
        **{
            "link_price": link_price,
            "link_price_breakevent": link_price_breakevent,
            "link_position_value": link_position_value,
            "link_position_amount": link_position_amount,
        }
    )
    send_porfolio_overview("tranthanhbao2207@gmail.com", response)
    return response


@porfolio_bp.route("/price/{token_pair}")
def get_funding_records(token_pair):
    token_pairs = []
    if not token_pair:
        token_pairs = ["BTCUSDT", "LINKUSDT"]
    return get_token_price([token_pair.upper()])[0].get("price")


@porfolio_bp.route("/p2p-pricing")
def get_p2p_current_pricing():
    return get_p2p_pricing()
