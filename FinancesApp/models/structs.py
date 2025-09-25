from enum import Enum, auto
from dataclasses import dataclass
from PySide6.QtCore import QDate

class AppViewMode(Enum):
    DASHBOARD = auto()
    REGISTRIES = auto()
    CARD = auto()
    USER = auto()
    CONFIG = auto()

class RegType(Enum):
    IN = auto()
    OUT = auto()

@dataclass
class RegCategory:
    id: int
    name: str

@dataclass
class DashParams:
    start: QDate
    end: QDate
    regType: RegType
    # allCategories: bool
    # categories: set[RegCategory] | None