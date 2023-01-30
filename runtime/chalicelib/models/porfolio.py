import uuid as uuid_lib

from chalicelib.db.base_class import Base
from chalicelib.enums import *
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, column, func
from sqlalchemy.orm import relationship

"""
Order Number,Order Type,Asset Type,Fiat Type,Total Price,Price,Quantity,Exchange rate,Couterparty,Status,Created Time
20401194693654421504,Buy,USDT,VND,9355539.0000000000000000,24180.0000000000000000,386.9100000000000000,"",silegiaodichnhanhhcm,Completed,2022-09-08 14:11:12
"""


class DepositRecords(Base):
    """
    ref:https://c2c.binance.com/en/fiatOrder?tab=1&page=1
    """

    order_number = Column(String, primary_key=True, index=True)
    order_type = Column(String, index=True)
    asset_type = Column(String)
    fiat_type = Column(String)
    total_price = Column(Float)
    price = Column(Float)  ## real exchange rate
    quantity = Column(Float)
    exchange_rate = Column(String, default="")  ## not use
    counter_party = Column(String)
    order_status = Column(String)
    created_time = Column(DateTime(timezone=True))

    created_at = Column(DateTime(timezone=True), default=func.now())


# class AutoinvestRecords(Base):
#     """
#     ref : https://www.binance.com/en/my/earn/history/auto-invest
#     """

#     token_name = Column(Integer, primary_key=True, index=True)
