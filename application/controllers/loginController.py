from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

from ..views.loginView import LoginView
from ..src.structs import LoginData, User
from ..models.appModel import AppModel

class LoginController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__model = model = AppModel.instance()

        model.authenticationFinished.connect(self.on_model_authenticationFinished)
        model.createUserFinished.connect(self.on_model_createUserFinished)

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
    
    def on_LoginFormView_continueRequired(self, data:LoginData):
        self.__view.getLoginFormView().setWaitMode(True)
        self.__model.authenticate(data)

    def on_LoginFormView_createAccountRequired(self):
        self.__view.setUi(LoginView.UI_CREATE_ACCOUNT)

    def on_LoginFormView_passwordForgot(self): ...

    def on_CreateAccountView_backRequired(self):
        self.__view.setUi(LoginView.UI_FORM)

    def on_CreateAccountView_continueRequired(self, data:User):
        self.__view.getCreateAccountView().setWaitMode(True)
        self.__model.createUser(data)

    def on_model_authenticationFinished(self, success:bool):
        if success: return

        if not self.__view.isCurrentView(LoginView.UI_FORM):
            self.__view.setUi(LoginView.UI_FORM)
        
        self.__view.getLoginFormView().setWaitMode(False)
        print('não autenticado')
        QMessageBox(QMessageBox.Critical, 'Login', 'Usuário ou senha incorretos!', parent=self.__view).exec()

    def on_model_createUserFinished(self, success:bool):
        if not success:
            view = self.__view.getCreateAccountView()
            QMessageBox(QMessageBox.Critical, 'Cadastro de Usuário', 'Já existe um usuário com essas informações!', parent=view).exec()
            view.setWaitMode(False)
            return
        
        self.__view.setUi(LoginView.UI_FORM)