import itertools
from dataclasses import dataclass

from chalicelib.db.session import SessionLocal
from chalicelib.models.porfolio import DepositRecords
from chalicelib.schemas.binance import AssetsOverView, BinanceP2PRecord, P2PRecord
from chalicelib.schemas.deposit import DepositOverview
from chalicelib.services.binance_api import BinanceExchange, bnb_ex
from loguru import logger
from sqlalchemy.sql import functions


@dataclass
class WalletController:
    def get_wallet_name(self) -> str:
        NotImplemented

    def get_p2p_records(self) -> list[P2PRecord]:
        NotImplemented

    def update_p2p_records(self) -> None:
        NotImplemented

    def get_deposits_overview(self) -> DepositOverview:
        NotImplemented


@dataclass
class BinanceController(WalletController):
    binance_exchange: BinanceExchange

    def get_p2p_overview(self):
        """
        https://binance-docs.github.io/apidocs/spot/en/#get-c2c-trade-history-user_data
        binance only return 30 days
        """
        p2p_records = self.binance_exchange.get_p2p_records()
        return {
            "records": p2p_records,
            "total_records": len(p2p_records),
        }

    def get_savings_account(self):
        return self.binance_exchange.get_savings_account()

    def get_wallet_name(self) -> str:
        return "BINANCE"

    def get_p2p_pricing(self, pair="USDT_VND"):
        return 0

    def get_p2p_records(self):
        return self.binance_client.get_p2p_records()

    def get_saving_accounts_overview(self):
        return self.binance_exchange.get_savings_account()

    def get_deposit_overview(self) -> DepositOverview:
        db = SessionLocal()
        query = (
            db.query(
                DepositRecords.order_type,
                functions.sum(DepositRecords.quantity.label("total_usd")),
                functions.sum(DepositRecords.total_price.label("total_vnd")),
            )
            .group_by(DepositRecords.order_type)
            .order_by(DepositRecords.order_type)
            .all()
        )
        buy_capital, sell_capital = query

        capital_usd = buy_capital[1] - sell_capital[1]
        capital_vnd = buy_capital[2] - sell_capital[2]

        res = {
            "capital_usd": capital_usd,
            "capital_vnd": capital_vnd,
            "average_capital_price": int(capital_vnd / capital_usd),
            "total_buy_usd": buy_capital[1],
            "total_buy_vnd": buy_capital[2],
            "total_sell_usd": sell_capital[1],
            "total_sell_vnd": sell_capital[2],
            "average_buy_price": int(buy_capital[2] / buy_capital[1]),
            "average_sell_price": int(sell_capital[2] / sell_capital[1]),
        }

        return DepositOverview(**res)

    def get_funding_overview(self) -> dict:
        current_assets = self.get_saving_accounts_overview()
        current_usd_price = self.binance_exchange.get_p2p_pricing()
        deposits = self.get_deposit_overview()

        link_price = float(
            self.binance_exchange.get_tokens_price(["LINKUSDT"])[0].get("price")
        )

        asset_overview = AssetsOverView(
            assets=[*current_assets],
            deposit_overview=deposits,
            # calculation
            current_usd_price=current_usd_price,
            # link_price=link_price,
        )

        link_price_breakevent = round(link_price / (asset_overview.pnl_usd), 1)
        link_position = asset_overview.major_asset

        link_position_value = round(float(link_position.total_amount))
        link_position_amount = float(link_position.total_amount)

        deposit_usd = "${:,.2f}".format(round(deposits.capital_usd, 2))
        deposit_vnd = "VND{:,.0f}".format(round(deposits.capital_vnd, 0))
        # average_buy_price =

        average_buy_price = "VND{:,.0f}".format(
            round(asset_overview.deposit_overview.average_buy_price)
        )
        stables_amount_vnd = "VND{:,.0f}".format(asset_overview.stables_amount_vnd)

        value_in_usd = "${:,.2f}".format(round(asset_overview.current_assets_usd, 2))
        value_in_vnd = "VND{:,.0f}".format(round(asset_overview.current_assets_vnd, 0))
        return {
            "value_in_usd": value_in_usd,
            "value_in_vnd": value_in_vnd,
            "capital_usd_deployed": "${:,.2f}".format(
                round(asset_overview.capital_usd_deployed)
            ),
            "capital_vnd_deployed": "VND{:,.0f}".format(
                round(asset_overview.capital_vnd_deployed)
            ),
            "stables_amount": asset_overview.stables_amount,
            "stables_amount_vnd": stables_amount_vnd,
            "current_usd_price": current_usd_price,
            "link_price": round(link_price, 1),
            "link_price_breakevent": link_price_breakevent,
            "link_position_value": link_position_value,
            "link_position_amount": link_position_amount,
            # "current_statable_assets": asset_overview.current_statable_assets,
            "deposit_usd": deposit_usd,
            "deposit_vnd": deposit_vnd,
            "average_buy_price": average_buy_price,
            "current_assets": current_assets.model_dump(),
            "deposits": deposits.model_dump(),
            # pnl
            "pnl_in_vnd": f"{asset_overview.pnl_vnd:,.2%}",
            "pnl_in_usd": f"{asset_overview.pnl_usd:,.2%}",
            "position_pnl_usd": f"{asset_overview.position_pnl_usd:,.2%}",
            "position_pnl_vnd": f"{asset_overview.position_pnl_vnd:,.2%}",
        }

    def update_p2p_records(self) -> list:
        recent_orders: list[BinanceP2PRecord] = self.binance_exchange.get_p2p_records()
        db = SessionLocal()
        query_result = db.query(DepositRecords.order_number).all()
        exists_order_numbers = list(itertools.chain(*query_result))

        new_orders = (
            binance_p2p_record
            for binance_p2p_record in recent_orders
            if binance_p2p_record.order_number not in exists_order_numbers
        )

        logger.debug(f"new_orders: {new_orders}")
        added_order_numbers = []
        for order in new_orders:
            order_db = DepositRecords()
            db.add(order_db)
            logger.info(
                "Adding p2p new order to db "
                + f"{order_db.order_number} - created time "
                + f"{order_db.created_time}"
            )

            added_order_numbers.append(
                {
                    "order_number": order_db.order_number,
                    "created_time ": order_db.created_time,
                }
            )

        db.commit()
        return added_order_numbers


binance_controller = BinanceController(bnb_ex)
logger.info(f"init binance_controller: {binance_controller}")
