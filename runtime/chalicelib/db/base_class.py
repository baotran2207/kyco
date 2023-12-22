from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __name__: str
    created_at = Column(DateTime(timezone=True), default=func.now())
    lastchanged_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
