from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from ..ui.auto.ui_LoginPage import Ui_LoginPage
from ..src.tools import generateStyleSheet
from .loginFormView import LoginFormView
from .createAccountView import CreateAccountView

class LoginView(QWidget):
    uiChanged = Signal(int)

    UI_FORM = 0
    UI_CREATE_ACCOUNT = 1

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_LoginPage()
        self.__uiForm = None
        self.__uiCreate = None
        self.__currentUi = None

        self.__ui.setupUi(self)
        self.setStyleSheet(generateStyleSheet())
    
    def getLoginFormView(self) -> LoginFormView | None: return self.__uiForm if self.__currentUi == self.UI_FORM else None
    def getCreateAccountView(self) -> CreateAccountView | None: return self.__uiCreate if self.__currentUi == self.UI_CREATE_ACCOUNT else None

    def setUi(self, ui:int):
        parent = self.__ui.widMain
        widOld = self.__ui.widContent

        match ui:
            case self.UI_FORM:
                widNew = self.__uiForm = LoginFormView(parent)
            
            case self.UI_CREATE_ACCOUNT:
                widNew = self.__uiCreate = CreateAccountView(parent)

            case _:
                raise ValueError('invalid UI')

        
        self.__ui.widContent = widNew
        self.__currentUi = ui
        self.__ui.mainLayout.replaceWidget(widOld, widNew)
        widOld.deleteLater()
        self.uiChanged.emit(ui)
