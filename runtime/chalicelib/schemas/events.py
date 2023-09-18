from typing import Callable

from pydantic import BaseModel, Field


class Subscriber(BaseModel):
    event_type: str = Field(..., description="Event type")
    fn: Callable
    listener_group_name: str = Field(
        ..., description="Handler group name", default_factory=""
    )
