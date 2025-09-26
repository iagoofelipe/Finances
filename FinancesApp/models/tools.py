from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette

from typing import Sequence, Any
from .consts import MAX_ITEMS_TABLE

def isDark() -> bool:
    return QApplication.instance().palette().color(QPalette.ColorRole.Window).lightness() < 128

def splitTableData(data:Sequence[Any], maxItems=MAX_ITEMS_TABLE):
    pass