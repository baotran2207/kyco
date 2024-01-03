import json

from chalice import Blueprint
from chalicelib.config import settings
from chalicelib.controller.porfolio import porfolio_controller
from chalicelib.controller.wallet import binance_controller
from chalicelib.enums import EmailType
from chalicelib.logger_app import logger
from chalicelib.services.authorizers import chalice_authorizer
from chalicelib.services.email_render import get_email_template
from chalicelib.services.email_sender import send_email

porfolio_bp = Blueprint(__name__)


@porfolio_bp.route("/assets", authorizer=chalice_authorizer)
def get_summary():
    return binance_controller.get_savings_account()


@porfolio_bp.route("/trigger-update", methods=["GET"])
def trigger_update():
    porfolio_controller.update_p2p_records()
    return "ok"


@porfolio_bp.route("/overview", authorizer=chalice_authorizer)
def get_funding_overview_route():
    response = binance_controller.get_funding_overview()
    template_name = get_email_template(EmailType.PORFOLIO_OVERVIEW.value)

    send_email(
        to_emails=[settings.WEBMASTER_EMAIL],
        template_name=template_name,
        message_type=EmailType.PORFOLIO_OVERVIEW.value,
        message_payload=response,
    )
    return response


@porfolio_bp.route("/p2p-pricing")
def get_p2p_current_pricing():
    return binance_controller.get_p2p_pricing()
