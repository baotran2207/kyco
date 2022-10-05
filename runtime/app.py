
from chalice import Chalice
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


@app.route('/fetch')
def fetch_data():
    from chalicelib.db.session import SessionLocal
    db = SessionLocal()
    a = db.execute("SELECT 1")
    return {'result': "aa"}

init_blueprint(app)
init_middlewares(app)
