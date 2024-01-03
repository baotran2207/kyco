import json

import requests
from chalice import Blueprint
from chalicelib.config import settings
from chalicelib.controller.telegram_bot import TelegramBotController

# from chalicelib.controller.wallet import binance_controller
from chalicelib.schemas.telegram_bot import RequestBody, RequestMessage
from loguru import logger
from pydantic import BaseModel

# from chalicelib.services.porfolio import summary_sheet

webhooks_routes = Blueprint(__name__)


class TelegramResponsePayload(BaseModel):
    chat_id: int
    text: str


url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"


@webhooks_routes.route("/telegram", methods=["GET", "POST"])
def telegram_bot():
    """
    Telegram bot webhook
    hook: https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api/webhooks/telegram

    """
    params = webhooks_routes.current_app.current_request.json_body
    request_body = RequestBody(**params)
    request_message = request_body.message
    if webhooks_routes.current_app.current_request.method == "GET":
        return request_body

    telegram_bot_controller = TelegramBotController()

    telegram_bot_controller.reply(
        chat_id=request_message.chat.id, origin_text=request_message.text
    )

    return 200
