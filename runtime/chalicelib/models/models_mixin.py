import uuid as uuid_lib

from chalicelib.db.base_class import Base
from chalicelib.enums import *
from sqlalchemy import Boolean, Column, DateTime, Integer, String, column, func
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(String, primary_key=True, index=True, default=uuid_lib.uuid4)
    cognito_id = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    full_name = Column(String, index=True)
    hashed_password = Column(String)
    status = Column(Integer, default=Status.Active.value)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    lastchanged_at = Column(DateTime(timezone=True), onupdate=func.now())


class UsedToken(Base):
    id = Column(String, primary_key=True, index=True, default=uuid_lib.uuid4)
    used_token = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    # owned_by = re
