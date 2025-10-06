from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from .loginView import LoginView

class AppView(QObject):
    uiChanged = Signal(int)

    UI_LOGIN = 0

    def __init__(self, model:AppModel):
        super().__init__()
        self.__loginView = None
        self.__currentUi = None
        self.__win = QMainWindow()

        self.__win.setWindowTitle('Finances')
        self.__win.resize(1000, 700)

    def getLoginView(self) -> LoginView | None:
        return self.__loginView if self.__currentUi == self.UI_LOGIN else None

    def setUi(self, ui:int):
        match ui:
            case self.UI_LOGIN:
                widNew = self.__loginView = LoginView()

            case _:
                raise ValueError('invalid UI')
        
        self.__currentUi = ui
        self.__win.setCentralWidget(widNew)
        self.uiChanged.emit(ui)
        

    def initialize(self):
        self.setUi(self.UI_LOGIN)
        self.__win.show()