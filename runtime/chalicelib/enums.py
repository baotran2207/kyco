from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Status(ExtendedEnum):
    Active = 1
    Disabled = 98
    Deleted = 99


class AppEnv(ExtendedEnum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"
    staging: str = "staging"


class EmailType(ExtendedEnum):
    NEW_OTP = "NEW_OTP"
    PORFOLIO_OVERVIEW = "PORFOLIO_OVERVIEW"


class LendingType(ExtendedEnum):
    DAILY = "DAILY"
    ACTIVITY = "ACTIVITY"
    CUSTOMIZED_FIXED = "CUSTOMIZED_FIXED"


class OrderStatus(ExtendedEnum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"


class P2POrderType(ExtendedEnum):
    BUY = "BUY"
    SELL = "SELL"


class TelegramCommands(ExtendedEnum):
    START = "start"
    HELP = "help"
    PORTFOLIO_DASHBOARD = "portfolio_dashboard"
