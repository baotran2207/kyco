from chalice import Blueprint
from chalice.app import Cron, Rate
from chalicelib.db.session import SessionLocal
from chalicelib.logger_app import logger
from chalicelib.services.porfolio import update_bnb_p2p_records
from chalicelib.db.session import SessionLocal
from chalicelib.services.porfolio import get_funding_overview
from chalicelib.services.email_sender import send_porfolio_overview
from chalicelib.config import settings
from chalicelib.services.github_service import update_file
import random

cronjob_bp = Blueprint(__name__)


@cronjob_bp.schedule(Cron(0, 18, "?", "*", "MON-FRI", "*"))
def update_deposit(event):
    print("update_deposit !")
    print(event.to_dict())
    res = update_bnb_p2p_records()
    logger.info(f"new order :{res} ")
    return "This should be invoked every weekday at 6pm"


@cronjob_bp.schedule(Cron(0, 18, "?", "*", "*", "*"))
def warm_up_db_everyday(event):
    logger.info("Warm up Superbase database !")
    db = SessionLocal()
    a = db.execute("SELECT 1")
    return "This should be invoked every weekday at 6pm"


@cronjob_bp.schedule(Rate(8, unit=Rate.HOURS))
def auto_commit_cron(event):
    if random.choice([True, False]):
        filename = "autocommit.txt"
        repo = "baotran2207/til"
        update_file(filename, "auto commit", repo)
    else:
        logger.info("No commit !")


@cronjob_bp.schedule(Cron(30, 9, "?", "*", "*", "*"))
def auto_send_porfolio_summary(event):
    funding_overview = get_funding_overview()
    link_price = round(float(get_token_price(["LINKUSDT"])[0].get("price")), 1)
    position_pnl_usd = float(
        unding_overview["PNL"]["position_pnl_usd"].replace("%", "")
    )
    response = dict(
        unding_overview,
        **{
            "link_price": link_price,
            "breakevent": round(link_price / (position_pnl_usd * 0.01), 1),
        },
    )
    send_porfolio_overview(settings.WEBMASTER_EMAIL, res)
    logger.info("Sent funding overview !")
