from chalice import Blueprint
from chalice.app import Cron, Rate
from chalicelib.db.session import SessionLocal
from chalicelib.logger_app import logger
from chalicelib.services.porfolio import update_bnb_p2p_records
from chalicelib.db.session import SessionLocal

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
