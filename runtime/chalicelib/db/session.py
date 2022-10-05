from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chalicelib.config import settings ## loadsetting before start up

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
