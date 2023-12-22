from enum import Enum


class Status(Enum):
    Active = 1
    Disabled = 98
    Deleted = 99


class AppEnv(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"
    staging: str = "staging"


class EmailType(Enum):
    NEW_OTP = "NEW_OTP"
    PORFOLIO_OVERVIEW = "PORFOLIO_OVERVIEW"


class LendingType(Enum):
    DAILY = "DAILY"
    ACTIVITY = "ACTIVITY"
    CUSTOMIZED_FIXED = "CUSTOMIZED_FIXED"


class OrderStatus(Enum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"


class P2POrderType(Enum):
    BUY = "BUY"
    SELL = "SELL"
