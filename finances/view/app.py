from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, QEvent, QTimer

from finances.core.tools import isDarkTheme
from finances.view.page import LoginPage, HomePage

class AppView(QMainWindow):

    class Theme:
        Dark = 0
        Light = 1

    uiChanged = Signal(int)
    themeChanged = Signal(Theme)

    class UI:
        Login = 0
        Home = 1

    def __init__(self):
        super().__init__()
        self.__currentUi = None

        self.setWindowTitle('Finances')
        self.resize(1000, 700)

    def getLoginPage(self): return self.__loginPage if self.isCurrentView(self.UI.Login) else None
    def getHomePage(self): return self.__homePage if self.isCurrentView(self.UI.Home) else None
    
    def isCurrentView(self, ui:UI):
        return self.__currentUi == ui
    
    def getCurrentUiId(self): return self.__currentUi

    def setUi(self, ui:UI):
        match ui:
            case self.UI.Login:
                widNew = self.__loginPage = LoginPage()

            case self.UI.Home:
                widNew = self.__homePage = HomePage()

            case _:
                raise ValueError('invalid UI')
        
        self.__currentUi = ui
        self.setCentralWidget(widNew)
        self.uiChanged.emit(ui)
        
    def initialize(self):
        self.setUi(self.UI.Login)
        self.show()

    def changeEvent(self, event):
        if event.type() == QEvent.Type.PaletteChange:
            QTimer.singleShot(0, self, lambda: self.themeChanged.emit(self.Theme.Dark if isDarkTheme() else self.Theme.Light))        

        return super().changeEvent(event)
    