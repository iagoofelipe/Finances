from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal

from ..src.ui.auto.ui_HomeForm import Ui_HomeForm
from .dashView import DashView
from .regView import RegView
from ..models.appModel import AppModel
from ..models.tools import isDark

from enum import Enum, auto

class HomeView(QWidget):
    logoutRequired = Signal()
    displayModeChanged = Signal(object)

    class DisplayMode(Enum):
        Dashboard = auto()
        Reg = auto()
        Card = auto()
        User = auto()
        Config = auto()

    def regView(self) -> RegView | None:
        return self.__regView if self.__currentDisplay == self.DisplayMode.Reg else None
    
    def dashView(self) -> DashView | None:
        return self.__dashView if self.__currentDisplay == self.DisplayMode.Dashboard else None

    def __init__(self, model:AppModel, parent:QWidget=None):
        super().__init__(parent)
        self.__model = model
        self.__ui = Ui_HomeForm()
        self.__btnNav = None
        self.__currentDisplay = None

        self.__ui.setupUi(self)

        self.__ui.btnDash.clicked.connect(lambda: self.setDisplayMode(self.DisplayMode.Dashboard))
        self.__ui.btnReg.clicked.connect(lambda: self.setDisplayMode(self.DisplayMode.Reg))
        self.__ui.btnCard.clicked.connect(lambda: self.setDisplayMode(self.DisplayMode.Card))
        self.__ui.btnUser.clicked.connect(lambda: self.setDisplayMode(self.DisplayMode.User))
        self.__ui.btnConfig.clicked.connect(lambda: self.setDisplayMode(self.DisplayMode.Config))
        self.__ui.btnLogout.clicked.connect(self.logoutRequired)

        if isDark():
            self.__ui.btnDash.setIcon(QIcon(u":/root/imgs/dark-pie.svg"))
            self.__ui.btnReg.setIcon(QIcon(u":/root/imgs/dark-table.svg"))
            self.__ui.btnCard.setIcon(QIcon(u":/root/imgs/dark-card.svg"))
            self.__ui.btnUser.setIcon(QIcon(u":/root/imgs/dark-user.svg"))
            self.__ui.btnConfig.setIcon(QIcon(u":/root/imgs/dark-gear.svg"))
            self.__ui.btnLogout.setIcon(QIcon(u":/root/imgs/dark-logout.svg"))

        self.setDisplayMode(self.DisplayMode.Reg)

    def setDisplayMode(self, mode:DisplayMode):
        if self.__currentDisplay == mode:
            return

        match mode:
            case self.DisplayMode.Dashboard:
                widNew = self.__dashView = DashView(self)
                btnNav = self.__ui.btnDash

            case self.DisplayMode.Reg:
                widNew = self.__regView = RegView(self.__model, self)
                btnNav = self.__ui.btnReg

            case self.DisplayMode.Card:
                widNew = QWidget(self)
                btnNav = self.__ui.btnCard

            case self.DisplayMode.User:
                widNew = QWidget(self)
                btnNav = self.__ui.btnUser

            case self.DisplayMode.Config:
                widNew = QWidget(self)
                btnNav = self.__ui.btnConfig

            case _:
                raise ValueError(f'{mode} is not a valid display mode to HomeView')

        if self.__btnNav:
            self.__btnNav.setDisabled(False)

        if btnNav:
            self.__btnNav = btnNav
            btnNav.setDisabled(True)

        widOld = self.__ui.widContent
        self.__ui.widContent = widNew
        self.__ui.mainLayout.replaceWidget(widOld, widNew)
        widOld.deleteLater()

        self.displayModeChanged.emit(mode)