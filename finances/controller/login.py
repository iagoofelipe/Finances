from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

from finances.view.page import LoginPage
from finances.core.structs import LoginData, User
from finances.model import AppModel

class LoginController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__model = model = AppModel.instance()

        model.authenticationFinished.connect(self.on_model_authenticationFinished)
        model.createUserFinished.connect(self.on_model_createUserFinished)

    def setView(self, view:LoginPage):
        self.__view = view
        view.uiChanged.connect(self.on_view_uiChanged)

    def on_view_uiChanged(self, ui:int):
        match ui:
            case LoginPage.UI.Authenticate:
                view = self.__view.getLoginForm()
                view.continueRequired.connect(self.on_LoginFormView_continueRequired)
                view.createAccountRequired.connect(self.on_LoginFormView_createAccountRequired)
                view.passwordForgot.connect(self.on_LoginFormView_passwordForgot)

            case LoginPage.UI.CreateAccount:
                view = self.__view.getCreateAccountForm()
                view.backRequired.connect(self.on_CreateAccountView_backRequired)
                view.continueRequired.connect(self.on_CreateAccountView_continueRequired)
    
    def on_LoginFormView_continueRequired(self, data:LoginData):
        self.__view.getLoginForm().setWaitMode(True)
        self.__model.authenticate(data)

    def on_LoginFormView_createAccountRequired(self):
        self.__view.setUi(LoginPage.UI.CreateAccount)

    def on_LoginFormView_passwordForgot(self): ...

    def on_CreateAccountView_backRequired(self):
        self.__view.setUi(LoginPage.UI.Authenticate)

    def on_CreateAccountView_continueRequired(self, data:User):
        self.__view.getCreateAccountForm().setWaitMode(True)
        self.__model.createUser(data)

    def on_model_authenticationFinished(self, success:bool):
        if success: return

        if not self.__view.isCurrentView(LoginPage.UI.Authenticate):
            self.__view.setUi(LoginPage.UI.Authenticate)
        
        self.__view.getLoginForm().setWaitMode(False)
        print('não autenticado')
        QMessageBox(QMessageBox.Critical, 'Login', 'Usuário ou senha incorretos!', parent=self.__view).exec()

    def on_model_createUserFinished(self, success:bool):
        if not success:
            view = self.__view.getCreateAccountForm()
            QMessageBox(QMessageBox.Critical, 'Cadastro de Usuário', 'Já existe um usuário com essas informações!', parent=view).exec()
            view.setWaitMode(False)
            return
        
        self.__view.setUi(LoginPage.UI.Authenticate)