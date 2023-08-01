import json

from chalice import Blueprint
from chalicelib.config import settings
from chalicelib.enums import EmailType
from chalicelib.logger_app import logger
from chalicelib.services.authorizers import chalice_authorizer
from chalicelib.services.email_sender import enqueue_send_email
from chalicelib.services.porfolio import (
    deposit_overview,
    get_funding_overview,
    get_p2p_overview,
    get_p2p_pricing,
    get_p2p_records,
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
def get_funding_overview_route():
    response = get_funding_overview()
    enqueue_send_email(
        to_emails=[settings.WEBMASTER_EMAIL],
        message_type=EmailType.PORFOLIO_OVERVIEW.value,
        message_payload=response,
    )
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
