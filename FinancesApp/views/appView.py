from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtCore import QObject, Signal

from ..src.ui.auto.ui_HomeForm import Ui_HomeForm
from .dashView import DashView
from ..models.appModel import AppModel
from ..models.structs import AppViewMode

class AppView(QObject):
    def __init__(self, model:AppModel):
        super().__init__()
        self.__model = model
        self.__win = QMainWindow()
        self.__wid = QWidget()
        self.__ui = Ui_HomeForm()
        self.__btnNav = None

    def initialize(self):
        self.__win.setMinimumSize(900, 550)
        self.__win.setWindowTitle('Finances')
        self.__ui.setupUi(self.__wid)

        self.__ui.btnDash.clicked.connect(lambda: self.setMode(AppViewMode.DASHBOARD))
        self.__ui.btnReg.clicked.connect(lambda: self.setMode(AppViewMode.REGISTRIES))

        self.__win.setCentralWidget(self.__wid)
        self.setMode(AppViewMode.DASHBOARD)
        self.__win.show()

    def setMode(self, mode:AppViewMode):
        widOld = self.__ui.widContent
        # print('mode changed to', mode.name)
        
        match mode:
            case mode.DASHBOARD:
                widNew = DashView(self.__wid)
                btnNav = self.__ui.btnDash

            case mode.REGISTRIES:
                widNew = QWidget()
                btnNav = self.__ui.btnReg

            case _:
                return

        if self.__btnNav:
            self.__btnNav.setDisabled(False)

        if btnNav:
            self.__btnNav = btnNav
            btnNav.setDisabled(True)

        self.__ui.widContent = widNew
        self.__ui.mainLayout.replaceWidget(widOld, widNew)
        widOld.deleteLater()