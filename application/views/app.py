from PySide6.QtWidgets import QApplication
import logging as log

from ..models.appModel import AppModel
from .appView import AppView
from ..controllers.appController import AppController

class FinancesApp(QApplication):
    def __init__(self):
        super().__init__()
        log.basicConfig(level=log.DEBUG)
        
        self.__model = AppModel._AppModel__instance = AppModel()
        self.__view = AppView(self.__model)
        self.__controller = AppController(self.__model, self.__view)

        self.aboutToQuit.connect(self.__controller.close)

    def exec(self):
        self.__controller.initialize()
        return super().exec()