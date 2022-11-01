
from chalice import Chalice, AuthResponse
from chalicelib.config import settings ## loadsetting before start up
from chalicelib.blueprint import init_blueprint
from chalicelib.middlewares import init_middlewares
from chalicelib.db.session import SessionLocal
from chalicelib.logger_app import logger


from chalicelib.services.authorizers import chalice_authorizer
app = Chalice(app_name='chalice-backend')


@app.route('/user-pools', methods=['GET'], authorizer=chalice_authorizer)
def authenticated():
    return {"success": True}


@app.route('/')
def health():
    return "Hello there from tranthanhbao2207@gmail.com"


@app.route('/check_db_connection')
def check_db_connection():
    db = SessionLocal()
    query = db.execute("SELECT 1")
    logger.info(f" Connection ok ! Detail {query} ")
    return 'Connection is ok'

init_blueprint(app)
init_middlewares(app)



############
## Events ##
############
# ref:
#     - https://github.com/aws/chalice/issues/1566
# Due to bug in blueprint register , we can only register API endpoint, but events and pure function. Let keep those events and pure function here in app.py until the bug is fixed
from chalice import Blueprint
from chalice.app import Cron


cron_events = Blueprint(__name__)
sqs_events = Blueprint(__name__)

@cron_events.schedule(Cron(0, 18, '?', '*', '*', '*'))
def warm_up_db_everyday(event):
    logger.info('Warm up Superbase database !')
    db = SessionLocal()
    a = db.execute("SELECT 1")
    return "This should be invoked every weekday at 6pm"


@sqs_events.on_sqs_message(
    queue='BaoTranChaliceGeneric',
    batch_size=1)
def handle_sqs_message(event):
    print('Trigger generic')
    print(type(event), event)
    for record in event:
        print(record, 'in event')
        logger.info(f" in even ! Detail {record} ")




app.register_blueprint(cron_events)
app.register_blueprint(sqs_events)


