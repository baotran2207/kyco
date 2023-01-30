from chalice import Blueprint
from chalicelib.services.authorizers import chalice_authorizer
from chalicelib.services.porfolio import (
    deposit_overview,
    get_p2p_overview,
    get_p2p_pricing,
    get_p2p_records,
    get_saving_accounts_overview,
    get_token_price,
    update_bnb_p2p_records,
    update_p2p_history_records,
)

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
def get_funding_overview():
    current_assets = get_saving_accounts_overview()
    current_assets_usd = float(current_assets["totalAmountInUSDT"])
    current_usd_price = float(get_p2p_pricing())
    current_assets_vnd = current_usd_price * current_assets_usd

    deposits = deposit_overview()
    capital_usd = deposits["capital_usd"]
    capital_vnd = deposits["capital_vnd"]

    pnl_usd = current_assets_usd / capital_usd
    pnl_vnd = current_assets_vnd / capital_vnd
    return {
        "current_amount_in_vnd": current_assets_vnd,
        "current_amount_in_usd": current_assets_usd,
        "PNL": {
            "pnl_in_vnd": f"{pnl_vnd:,.2%}",
            "pnl_in_usd": f"{pnl_usd:,.2%}",
        },
        "current_usd_price": current_usd_price,
        "current_assets": current_assets,
        "deposits": deposits,
    }


@porfolio_bp.route("/price/{token_pair}")
def get_funding_records(token_pair):
    token_pairs = []
    if not token_pair:
        token_pairs = ["BTCUSDT", "LINKUSDT"]
    return get_token_price([token_pair.upper()])[0].get("price")


@porfolio_bp.route("/p2p-pricing")
def get_p2p_current_pricing():
    return get_p2p_pricing()
