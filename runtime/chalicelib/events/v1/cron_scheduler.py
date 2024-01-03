import random

from chalice import Blueprint
from chalice.app import Cron, Rate
from chalicelib.config import settings
from chalicelib.controller.wallet import binance_controller
from chalicelib.db.session import SessionLocal
from chalicelib.enums import EmailType
from chalicelib.services.email_render import get_email_template
from chalicelib.services.email_sender import send_email
from chalicelib.services.github_service import update_file
from chalicelib.services.porfolio import update_bnb_p2p_records
from loguru import logger

cronjob_bp = Blueprint(__name__)


@cronjob_bp.schedule(Cron(0, 18, "?", "*", "MON-FRI", "*"))
def update_deposit(event):
    res = update_bnb_p2p_records()
    logger.info(f"new order :{res} ")
    return "This should be invoked every weekday at 6pm"


@cronjob_bp.schedule(Cron(0, 18, "?", "*", "*", "*"))
def warm_up_db_everyday(event):
    logger.info("Warm up Superbase database !")
    db = SessionLocal()
    a = db.execute("SELECT 1")
    logger.info(a)
    return "This should be invoked every weekday at 6pm"


@cronjob_bp.schedule(Rate(18, unit=Rate.HOURS))
def auto_commit_cron(event):
    if random.choice([True, False]):
        filename = "autocommit.txt"
        repo = "baotran2207/til"
        update_file(filename, "auto commit", repo)
    else:
        logger.info("No commit !")


@cronjob_bp.schedule(Cron(7, "2,7,22", "?", "*", "*", "*"))
def auto_send_porfolio_summary(event):
    response = binance_controller.get_funding_overview()
    template_name = get_email_template(EmailType.PORFOLIO_OVERVIEW.value)

    send_email(
        to_emails=[settings.WEBMASTER_EMAIL],
        template_name=template_name,
        message_type=EmailType.PORFOLIO_OVERVIEW.value,
        message_payload=response,
    )
    logger.info("Sent funding overview !")
