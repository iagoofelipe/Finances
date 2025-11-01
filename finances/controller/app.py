from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QObject

from finances.controller.login import LoginController
from finances.controller.home import HomeController
from finances.view.app import AppView
from finances.model import AppModel
from finances.view.component.dialog import NewProfileDialog

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view
        self.__loginController = LoginController(self)
        self.__homeController = HomeController(self)

        view.uiChanged.connect(self.on_view_uiChanged)
        view.themeChanged.connect(self.on_view_themeChanged)

        model.initializationFinished.connect(self.on_model_initializationFinished)
        model.authenticationFinished.connect(self.on_model_authenticationFinished)
        model.logoutFinished.connect(self.on_model_logoutFinished)
        model.noProfileFound.connect(self.on_model_noProfileFound)
        model.shareProfileFinished.connect(self.on_model_shareProfileFinished)
    
    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()

    def close(self):
        self.__model.close()

    def on_view_uiChanged(self, ui:int):
        match ui:
            case AppView.UI.Login:
                self.__loginController.setView(self.__view.getLoginPage())

            case AppView.UI.Home:
                self.__homeController.setView(self.__view.getHomePage())

    def on_model_initializationFinished(self, success:bool):
        if not success:
            QMessageBox(QMessageBox.Warning, 'Inicialização', 'Não foi possível inicializar os componentes').exec()
            QApplication.instance().quit()
            return

        credentials = self.__model.credentials
        if credentials:
            self.__model.authenticate(credentials)
            return
        
        view = self.__view.getLoginPage()
        view.setUi(view.UI.Authenticate)
        
    def on_model_authenticationFinished(self, success:bool):
        if not success: return
        
        if self.__model.credentials.remember:
            self.__model.saveCredentials()
        
        self.__view.setUi(AppView.UI.Home)

    def on_model_logoutFinished(self):
        self.__view.setUi(AppView.UI.Login)
        view = self.__view.getLoginPage()
        view.setUi(view.UI.Authenticate)

    def on_model_noProfileFound(self):
        dialog = NewProfileDialog(self.__view.getHomePage())
        if dialog.exec():
            self.__model.createProfile(dialog.getValues())
        
        # while True:
        #     if dialog.exec():
        #         self.__model.createProfile(dialog.getValues())
        #         break

    def on_model_shareProfileFinished(self, success:bool, msg:str|None):
        if success: return
            
        QMessageBox(QMessageBox.Warning, 'Compartilhamento de Perfil', msg if msg else 'não foi possível realizar o compartilhamento do perfil, tente novamente.').exec()
    
    def on_view_themeChanged(self, theme:AppView.Theme):
        print('Theme changed to', 'Dark' if theme == AppView.Theme.Dark else 'Light')
        #TODO: verificar se há trabalho a ser salvo
        self.__view.setUi(self.__view.getCurrentUiId())
