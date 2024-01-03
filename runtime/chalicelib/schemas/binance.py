import datetime
from itertools import chain

from chalicelib import utils
from chalicelib.enums import OrderStatus
from icecream import ic
from pydantic import BaseModel, Field, validator

from .deposit import DepositOverview

STABLES_ASSETS = ["USDT", "BUSD", "USDC", "DAI", "FDUSD"]


class BinanceP2PRecord(BaseModel):
    order_number: str = Field(..., alias="orderNumber", frozen=True)
    trade_type: str = Field(..., alias="tradeType", frozen=True)
    asset: str = Field(..., alias="asset", frozen=True)
    fiat: str = Field(..., frozen=True)
    fiat_symbol: str = Field(..., alias="fiatSymbol", frozen=True)
    amount: float = Field(..., frozen=True)
    total_price: float = Field(..., alias="totalPrice", frozen=True)
    unit_price: float = Field(..., alias="unitPrice", frozen=True)
    order_status: str = Field(..., alias="orderStatus", frozen=True)
    create_time: int = Field(..., alias="createTime", frozen=True)


class P2PRecord(BaseModel):
    order_number: str
    order_type: str
    asset_type: str
    fiat_type: str
    total_price: str
    price: str
    quantity: str
    status: str
    created_time: int

    def get_created_time(self) -> datetime.datetime:
        return datetime.fromtimestamp(self.created_time / 1e3)

    def is_completed(self):
        return self.status == OrderStatus.COMPLETED.value


class Asset(BaseModel):
    asset_name: str = Field(..., alias="asset", frozen=True)
    total_amount: float = Field(
        ..., alias="totalAmount", frozen=True, default_factory=float()
    )
    current_price: float = None

    @property
    def is_stables_asset(self) -> bool:
        return self.asset_name in STABLES_ASSETS

    @property
    def value_in_usd(self) -> bool:
        if self.is_stables_asset:
            return 1
        if self.total_amount == 0:
            return 0

        return self.total_amount * self.current_price


class EarnAsset(Asset):
    asset_name: str = Field(..., alias="asset", frozen=True)
    can_redeem: bool = Field(..., alias="canRedeem", frozen=True)
    collateral_amount: float = Field(..., alias="collateralAmount", frozen=True)
    cumulative_bonus_rewards: float = Field(
        ..., alias="cumulativeBonusRewards", frozen=True
    )
    cumulative_real_time_rewards: float = Field(
        ..., alias="cumulativeRealTimeRewards", frozen=True
    )
    cumulative_total_rewards: float = Field(
        ..., alias="cumulativeTotalRewards", frozen=True
    )
    latest_annual_percentage_rate: float = Field(
        ..., alias="latestAnnualPercentageRate", frozen=True
    )
    product_id: str = Field(..., alias="productId", frozen=True)
    total_amount: float = Field(..., alias="totalAmount", frozen=True)
    yesterday_real_time_rewards: float = Field(
        ..., alias="yesterdayRealTimeRewards", frozen=True
    )

    @property
    def is_earn_asset(self) -> True:
        return True


class EarnAssets(BaseModel):
    earn_assets: list[EarnAsset]
    total_amount: float = None
    stables_amount: float = None

    def __iter__(self):
        return iter(self.earn_assets)

    def model_post_init(self, ctx):
        self.total_amount = self.get_total_amount()
        self.stables_amount = self.get_stables_amount()

    def get_total_amount(self):
        return sum([asset.total_amount for asset in self.earn_assets])

    def get_stables_amount(self):
        return sum(
            [asset.total_amount for asset in self.earn_assets if asset.is_stables_asset]
        )

    def get_value_in_usd(self):
        return sum([asset.value_in_usd for asset in self.earn_assets])


class AssetsOverView(BaseModel):
    assets: list[Asset] = Field(..., frozen=True, exclude=True)
    deposit_overview: DepositOverview = Field(..., frozen=True, exclude=True)

    current_usd_price: float = Field(..., frozen=True)

    stables_amount: float = None
    stables_amount_vnd: float = None
    current_assets_usd: float = None
    current_assets_vnd: float = None

    capital_usd: float = None
    capital_vnd: float = None

    capital_usd_deployed: float = None
    capital_vnd_deployed: float = None

    pnl_usd: float = None
    pnl_vnd: float = None

    position_pnl_usd: float = None
    position_pnl_vnd: float = None

    deposit_usd: float = None
    deposit_vnd: float = None

    major_asset: Asset = None

    def model_post_init(self, ctx):
        self.stables_amount = round(
            sum(
                [asset.total_amount for asset in self.assets if asset.is_stables_asset]
            ),
            2,
        )
        self.stables_amount_vnd = round(self.stables_amount * self.current_usd_price)
        self.current_assets_usd = sum([asset.value_in_usd for asset in self.assets])
        self.current_assets_vnd = self.current_assets_usd * self.current_usd_price

        self.capital_usd = self.deposit_overview.capital_usd
        self.capital_vnd = self.deposit_overview.capital_vnd

        self.capital_usd_deployed = self.capital_usd - self.stables_amount
        self.capital_vnd_deployed = self.capital_usd_deployed * self.current_usd_price

        self.pnl_usd = round(
            (self.current_assets_usd + self.stables_amount) / self.capital_usd, 2
        )
        self.pnl_vnd = (
            self.current_assets_vnd + (self.stables_amount * self.current_usd_price)
        ) / self.capital_vnd

        self.position_pnl_usd = (
            self.current_assets_usd - self.stables_amount
        ) / self.capital_usd_deployed

        self.position_pnl_vnd = (
            self.current_assets_vnd - self.stables_amount * self.current_usd_price
        ) / self.capital_vnd_deployed

        self.major_asset = self.get_major_asset()

        self.deposit_usd = self.deposit_overview.capital_usd
        self.deposit_vnd = self.deposit_overview.capital_vnd

    def get_major_asset(self):
        non_staables_assets = [
            asset for asset in self.assets if asset.is_stables_asset is False
        ]

        return max(
            non_staables_assets,
            key=lambda asset: asset.total_amount,
        )
