from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QObject, Signal

from .loginController import LoginController
from .mainController import MainController
from ..views.appView import AppView
from ..models.appModel import AppModel
from ..views.components.dialog import NewProfileDialog

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view
        self.__loginController = LoginController(self)
        self.__mainController = MainController(self)

        view.uiChanged.connect(self.on_view_uiChanged)
        model.initializationFinished.connect(self.on_model_initializationFinished)
        model.authenticationFinished.connect(self.on_model_authenticationFinished)
        model.logoutFinished.connect(self.on_model_logoutFinished)
        model.noProfileFound.connect(self.on_model_noProfileFound)
    
    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()

    def close(self):
        self.__model.close()

    def on_view_uiChanged(self, ui:int):
        match ui:
            case AppView.UI_LOGIN:
                self.__loginController.setView(self.__view.getLoginView())

            case AppView.UI_MAIN:
                self.__mainController.setView(self.__view.getMainPageView())

    def on_model_initializationFinished(self, success:bool):
        if not success:
            QMessageBox(QMessageBox.Warning, 'Inicialização', 'Não foi possível inicializar os componentes').exec()
            QApplication.instance().quit()
            return

        credentials = self.__model.credentials
        if credentials:
            self.__model.authenticate(credentials)
            return
        
        view = self.__view.getLoginView()
        view.setUi(view.UI_FORM)
        
    def on_model_authenticationFinished(self, success:bool):
        if not success: return
        
        if self.__model.credentials.remember:
            self.__model.saveCredentials()
        
        self.__view.setUi(AppView.UI_MAIN)

    def on_model_logoutFinished(self):
        self.__view.setUi(AppView.UI_LOGIN)
        view = self.__view.getLoginView()
        view.setUi(view.UI_FORM)

    def on_model_noProfileFound(self):
        dialog = NewProfileDialog(self.__view.getMainPageView())
        if dialog.exec():
            self.__model.createProfile(dialog.getValues())
        
        # while True:
        #     if dialog.exec():
        #         self.__model.createProfile(dialog.getValues())
        #         break