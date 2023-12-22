from dataclasses import dataclass

from chalicelib.controller.wallet import WalletController, binance_controller


@dataclass
class PorfolioController:
    wallets: list[WalletController]

    def update_p2p_records(self):
        for wallet in self.wallets:
            if wallet.get_wallet_name() == "BINANCE":
                return wallet.update_p2p_records()


porfolio_controller = PorfolioController(wallets=[binance_controller])
