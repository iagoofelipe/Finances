from PySide6.QtCore import QObject, Signal

class ConfigController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)

    