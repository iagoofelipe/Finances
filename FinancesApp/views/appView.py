from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from .homeView import HomeView
from .loginView import LoginView

from enum import Enum, auto

class AppView(QObject):
    displayModeChanged = Signal(object)

    class DisplayMode(Enum):
        Home = auto()
        Login = auto()

    def __init__(self, model:AppModel):
        super().__init__()
        self.__model = model
        self.__win = QMainWindow()
        self.__currentDisplay = None

    def initialize(self):
        self.__win.setMinimumSize(900, 550)
        self.__win.setWindowTitle('Finances')
        self.setDisplayMode(self.DisplayMode.Login)
        self.__loginView.setDisabled(True)
        self.__win.show()

    def setDisplayMode(self, mode:DisplayMode):
        if self.__currentDisplay == mode:
            return

        match mode:
            case self.DisplayMode.Home:
                self.__homeView = wid = HomeView(self.__model)

            case self.DisplayMode.Login:
                self.__loginView = wid = LoginView(self.__model)

            case _:
                raise ValueError(f'{mode} is not a valid display mode to AppView')

        self.__currentDisplay = mode
        self.__win.setCentralWidget(wid)
        
        self.displayModeChanged.emit(mode)

    def loginView(self) -> LoginView | None:
        if self.__currentDisplay == self.DisplayMode.Login:
            return self.__loginView
        
    def homeView(self) -> HomeView | None:
        if self.__currentDisplay == self.DisplayMode.Home:
            return self.__homeView