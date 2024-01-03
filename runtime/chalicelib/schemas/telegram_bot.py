from pydantic import BaseModel, Field

# webhooks request
## example body
# {
#     "update_id": 924255644,
#     "message": {
#         "message_id": 5,
#         "from": {
#             "id": 5256531196,
#             "is_bot": False,
#             "first_name": "Bao",
#             "last_name": "Tran",
#             "username": "baotran2207",
#             "language_code": "en",
#         },
#         "chat": {
#             "id": 5256531196,
#             "first_name": "Bao",
#             "last_name": "Tran",
#             "username": "baotran2207",
#             "type": "private",
#         },
#         "date": 1704254663,
#         "text": "/start",
#         "entities": [{"offset": 0, "length": 6, "type": "bot_command"}],
#     },
# }


class RequestFrom(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str


class RequestChat(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    type: str


class RequestMessage(BaseModel):
    message_id: int
    from_: RequestFrom = Field(..., alias="from", frozen=True)
    chat: RequestChat
    date: int
    text: str
    entities: list

    def is_command(self):
        return self.text.startswith("/")


class RequestBody(BaseModel):
    update_id: int
    message: RequestMessage
