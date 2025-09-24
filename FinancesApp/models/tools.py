from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette

def isDark() -> bool:
    return QApplication.instance().palette().color(QPalette.ColorRole.Window).lightness() < 128