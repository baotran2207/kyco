from pydantic import BaseModel


class DepositOverview(BaseModel):
    capital_usd: float
    capital_vnd: float
    average_capital_price: float
    total_buy_usd: float
    total_buy_vnd: float
    total_sell_usd: float
    total_sell_vnd: float
    average_buy_price: float
    average_sell_price: float
