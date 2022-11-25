

# from chalice import Blueprint
# from chalice.app import Cron
# from chalicelib.db.session import SessionLocal

# cron_bp = Blueprint(__name__)


# @cron_bp.schedule(Cron(0, 18, '?', '*', 'MON-FRI', '*'))
# def warm_up_db_everyday(event):
#     print('Warm up Superbase database !')
#     print(event.to_dict())
#     db = SessionLocal()
#     a = db.execute("SELECT 1")
#     return "This should be invoked every weekday at 6pm"