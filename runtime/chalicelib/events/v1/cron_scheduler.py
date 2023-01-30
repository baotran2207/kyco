from chalice import Blueprint
from chalice.app import Cron
from chalicelib.db.session import SessionLocal
from chalicelib.logger_app import logger
from chalicelib.services.porfolio import update_bnb_p2p_records

cronjob_bp = Blueprint(__name__)


@cronjob_bp.schedule(Cron(0, 18, "?", "*", "MON-FRI", "*"))
def update_deposit(event):
    print("update_deposit !")
    print(event.to_dict())
    res = update_bnb_p2p_records()
    logger.info(f"new order :{res} ")
    return "This should be invoked every weekday at 6pm"
