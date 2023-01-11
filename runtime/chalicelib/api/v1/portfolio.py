from chalice import Blueprint
from chalicelib.services.authorizers import chalice_authorizer
from chalicelib.services.porfolio import (
    get_p2p_overview,
    get_p2p_pricing,
    get_p2p_records,
    get_saving_accounts_overview,
    get_token_price,
)

porfolio_bp = Blueprint(__name__)


@porfolio_bp.route("/assets", authorizer=chalice_authorizer)
def get_summary():
    return get_saving_accounts_overview()


# @porfolio_bp.route("/dca-history", authorizer=chalice_authorizer)
# def get_savings_purchase_record():
#     res = get_dca_history()
#     return res


@porfolio_bp.route("/funding/overview", authorizer=chalice_authorizer)
def get_funding_overview():
    return get_p2p_overview()


@porfolio_bp.route("/funding/records", authorizer=chalice_authorizer)
def get_funding_records():
    return get_p2p_records()


@porfolio_bp.route("/price/{token_pair}")
def get_funding_records(token_pair):
    token_pairs = []
    if not token_pair:
        token_pairs = ["BTCUSDT", "LINKUSDT"]
    return get_token_price([token_pair.upper()])[0].get("price")


@porfolio_bp.route("/p2p-pricing")
def get_p2p_current_pricing():
    return get_p2p_pricing()
