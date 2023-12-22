import uuid as uuid_lib

from chalicelib.db.base_class import Base
from chalicelib.enums import *
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, column, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

"""
Order Number,Order Type,Asset Type,Fiat Type,Total Price,Price,Quantity,Exchange rate,Couterparty,Status,Created Time
20401194693654421504,Buy,USDT,VND,9355539.0000000000000000,24180.0000000000000000,386.9100000000000000,"",silegiaodichnhanhhcm,Completed,2022-09-08 14:11:12
"""


class DepositRecords(Base):
    """
    ref:https://c2c.binance.com/en/fiatOrder?tab=1&page=1
    """

    order_number: Mapped[str] = mapped_column(String(50), index=True, primary_key=True)
    order_type: Mapped[str] = mapped_column(String(5), index=True)
    asset_type: Mapped[str] = mapped_column(String(10))
    fiat_type: Mapped[str] = mapped_column(String(10))

    total_price: Mapped[float] = mapped_column(Float)
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[float] = mapped_column(Float)
    exchange_rate: Mapped[str] = mapped_column(String(10), default="")
    counter_party: Mapped[str] = mapped_column(String(20), nullable=True)
    order_status: Mapped[str] = mapped_column(String(20))
    created_time = Column(DateTime(timezone=True))


# class AutoinvestRecords(Base):
#     """
#     ref : https://www.binance.com/en/my/earn/history/auto-invest
#     """

#     token_name = Column(Integer, primary_key=True, index=True)
