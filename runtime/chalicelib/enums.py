from enum import Enum

class Status(Enum):
    Active = 1
    Disabled = 98
    Deleted = 99

class AppEnv(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"
