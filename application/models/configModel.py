from PySide6.QtCore import QObject, Signal

from .appModel import AppModel

class ConfigModel(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__model = AppModel.instance()

    def getTablePerfisData(self):
        pass