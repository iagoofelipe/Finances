from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from finances.ui.auto.ui_LoginPage import Ui_LoginPage
from finances.core.tools import generateStyleSheet
from finances.view.form import LoginForm, CreateAccountForm

class LoginPage(QWidget):
    uiChanged = Signal(int)

    class UI:
        Authenticate = 0
        CreateAccount = 1

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_LoginPage()
        self.__uiForm = None
        self.__uiCreate = None
        self.__currentUi = None

        self.__ui.setupUi(self)
        self.setStyleSheet(generateStyleSheet())
    
    def getLoginForm(self) -> LoginForm | None: return self.__uiForm if self.isCurrentView(self.UI.Authenticate) else None
    def getCreateAccountForm(self) -> CreateAccountForm | None: return self.__uiCreate if self.isCurrentView(self.UI.CreateAccount) else None

    def isCurrentView(self, ui:int):
        return self.__currentUi == ui

    def setUi(self, ui:int):
        parent = self.__ui.widMain
        widOld = self.__ui.widContent

        match ui:
            case self.UI.Authenticate:
                widNew = self.__uiForm = LoginForm(parent)
            
            case self.UI.CreateAccount:
                widNew = self.__uiCreate = CreateAccountForm(parent)

            case _:
                raise ValueError('invalid UI')

        
        self.__ui.widContent = widNew
        self.__currentUi = ui
        self.__ui.mainLayout.replaceWidget(widOld, widNew)
        widOld.deleteLater()
        self.uiChanged.emit(ui)

    # def setWaitMode(self, arg:bool):
    #     if self.__currentUi == self.UI.Authenticate:
    #         self.__uiForm.setWaitMode(arg)
        
    #     elif self.__currentUi == self.UI.CreateAccount:
    #         self.__uiCreate.setWaitMode(arg)