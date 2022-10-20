
from chalice import Chalice, AuthResponse
from chalicelib.config import settings ## loadsetting before start up
from chalicelib.blueprint import init_blueprint
from chalicelib.middlewares import init_middlewares

import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Chalice(app_name='chalice-backend')
"""
Local localhost:8000/v1/users/baotran
stage: localhost:8000/{stage}v1/users/baotran

localhost:8000/dev/v1/users/baotran
localhost:8000/api/v1/users/baotran
"""


@app.route('/health')
def health():
    return "ok"


@app.route('/check_db_connection')
def check_db_connection():
    from chalicelib.db.session import SessionLocal
    db = SessionLocal()
    query = db.execute("SELECT 1")
    logger.info(f" Connection ok ! Detail {query} ")
    return 'Connection is ok'

init_blueprint(app)
init_middlewares(app)



@app.authorizer()
def jwt_auth(auth_request):
    token = auth_request.token
    decoded = decode_jwt_token(token)
    return AuthResponse(routes=["*"], principal_id=decoded["username"])