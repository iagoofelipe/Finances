from PySide6.QtWidgets import QApplication

from ..models.appModel import AppModel
from .appView import AppView
from ..controllers.appController import AppController

class FinancesApp(QApplication):
    def __init__(self):
        super().__init__()
        self.__model = AppModel()
        self.__view = AppView(self.__model)
        self.__controller = AppController(self.__model, self.__view)

    def exec(self):
        self.__controller.initialize()
        return super().exec()