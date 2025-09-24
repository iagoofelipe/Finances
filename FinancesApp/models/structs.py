from enum import Enum, auto
from dataclasses import dataclass
from PySide6.QtCore import QDate

class AppViewMode(Enum):
    DASHBOARD = auto()
    REGISTRIES = auto()

class RegType(Enum):
    IN = auto()
    OUT = auto()

@dataclass
class DashParams:
    thirdParties: bool
    start: QDate
    end: QDate
    regType: RegType