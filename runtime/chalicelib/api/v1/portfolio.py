from chalice import Blueprint
from chalicelib.services.porfolio import get_my_earn_assets

porfolio_bp = Blueprint(__name__)

MY_HOLDING = ["LINK", "ETH", "BUSD", "USDT"]


@porfolio_bp.route("/assets")
def get_summary():
    res = get_my_earn_assets(MY_HOLDING)
    return res


@porfolio_bp.route("/assets/{token_name}")
def get_summary(token_name):
    res = get_my_earn_assets([token_name.upper()])
    return res
