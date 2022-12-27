from celery import Celery
from chalicelib.config import settings

# print(settings.REDIS_URL)
# app = Celery(
#     'tasks',
#     broker=settings.REDIS_URL,
#     broker_use_ssl=True
#     # backend=settings.REDIS_URL,
# )

# print(2)
# @app.task
# def add(x, y):
#     print(x)
#     print( x+ y)
#     return x + y
