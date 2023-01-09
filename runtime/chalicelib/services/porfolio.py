# from chalicelib.extenions import gc
from functools import reduce

from chalicelib.services.binance_api import (
    get_flexible_savings_balance,
    get_token_price,
)

# porfolio_gsheet_url = "https://docs.google.com/spreadsheets/d/1Pbe9OPHhrVdDnjOurrTtSbUbLIHk1LsE_3R6s5pDLSw/edit?pli=1#gid=1375167053"
# porfolio_sheet = gc.open_by_url(porfolio_gsheet_url)


# print(porfolio_sheet.worksheets())
# summary_sheet = porfolio_sheet.get_worksheet(0)

# print(summary_sheet)


def get_my_earn_assets(token_names: list):
    assets = []
    for token_name in [t.upper() for t in token_names]:
        earned_assets = get_flexible_savings_balance(token_name)
        token_price = 1 if "USD" in token_name else get_token_price(token_name)
        token_amount = earned_assets and earned_assets[0].get("totalAmount") or 0

        asset = {
            "token_name": token_name,
            "token_price": token_price,
            "token_amount": token_amount,
            "token_value": float(token_amount) * float(token_price),
        }
        assets.append(asset)

    total_values = reduce(lambda x, asset: x + asset["token_value"], assets, 0)

    return {"total_values": total_values, "assets": assets}
