from PySide6.QtCore import QObject, Signal

from ..views.loginView import LoginView
from ..src.structs import LoginData

class LoginController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)

    def setView(self, view:LoginView):
        self.__view = view
        view.uiChanged.connect(self.on_view_uiChanged)

    def on_view_uiChanged(self, ui:int):
        match ui:
            case LoginView.UI_FORM:
                view = self.__view.getLoginFormView()
                view.continueRequired.connect(self.on_LoginFormView_continueRequired)
                view.createAccountRequired.connect(self.on_LoginFormView_createAccountRequired)
                view.passwordForgot.connect(self.on_LoginFormView_passwordForgot)

            case LoginView.UI_CREATE_ACCOUNT:
                view = self.__view.getCreateAccountView()
                view.backRequired.connect(self.on_CreateAccountView_backRequired)
                view.continueRequired.connect(self.on_CreateAccountView_continueRequired)
    
    def on_LoginFormView_continueRequired(self, data:LoginData): ...

    def on_LoginFormView_createAccountRequired(self):
        self.__view.setUi(LoginView.UI_CREATE_ACCOUNT)

    def on_LoginFormView_passwordForgot(self): ...

    def on_CreateAccountView_backRequired(self):
        self.__view.setUi(LoginView.UI_FORM)

    def on_CreateAccountView_continueRequired(self): ...