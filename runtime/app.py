
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
s3_events = Blueprint(__name__)

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
    print("dict ", event.to_dict())
    print("body ", event.body)
    logger.info("body ", event.body)
    for record in event:
        print(record, 'in event')
        logger.info(f" in even ! Detail {record} ")


# TODO: https://aws.github.io/chalice/topics/events.html#s3-events current version does not support existing bucket created via cdk .
@s3_events.on_s3_event(
    bucket=settings.S3_MAIN_BUCKET,
    prefix="users_upload",
    events=['s3:ObjectCreated:*']
)
def handle_s3_event(event):
    print("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)
    app.log.info("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)

app.register_blueprint(cron_events)
app.register_blueprint(sqs_events)
# app.register_blueprint(s3_events)

@app.route('/test_sqs', methods=['GET'])
def test_sqs():
    from chalicelib.services.sqs_service import sqs_generic ,send_message
    print('test message ')
    test = send_message(
        queue=sqs_generic,
        message_body="test sqs mesg",
        message_attributes= {
                    'path': {'StringValue': "test", 'DataType': 'String'},
                    'line': {'StringValue': "trigger", 'DataType': 'String'}
        }
    )

    return test