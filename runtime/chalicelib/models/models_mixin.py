import uuid as uuid_lib
from typing import List

from chalicelib.db.base_class import Base
from chalicelib.enums import Status
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    column,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    id = Column(String, primary_key=True, index=True, default=uuid_lib.uuid4)
    cognito_id = Column(String, index=True)
    email = Column(String, index=True)
    phone_number = Column(String, index=True)
    full_name = Column(String, index=True)
    hashed_password = Column(String)
    status = Column(Integer, default=Status.Active.value)
    is_superuser = Column(Boolean(), default=False)

    used_tokens: Mapped[List["UsedToken"]] = relationship(
        "UsedToken",
        back_populates="user",
        cascade="all, delete, delete-orphan",
    )


class UsedToken(Base):
    id = Column(String, primary_key=True, index=True, default=uuid_lib.uuid4)
    used_token = Column(String)

    # user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_id = Column(String, ForeignKey("user.id"))
    user: Mapped["User"] = relationship(User, back_populates="used_tokens")
