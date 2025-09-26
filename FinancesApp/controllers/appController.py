from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox, QApplication

from ..models.appModel import AppModel
from ..views.appView import AppView
from .homeController import HomeController

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view
        self.__homeController = HomeController(model, view)

        # connecting events
        model.initializationFinished.connect(self.on_model_initializationFinished)
        model.authFinished.connect(self.on_model_authFinished)
        view.displayModeChanged.connect(self.on_view_displayModeChanged)

    #----------------------------------------------------------
    # Public Methods
    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()

    #----------------------------------------------------------
    # Events
    def on_model_initializationFinished(self, success:bool, error:str):
        loginView = self.__view.loginView()

        if success:
            # checking saved credentials
            if self.__model.rememberCredentials():
                self.__model.auth(*self.__model.getSavedCredentials(), True) # continue in on_model_authFinished
                return

            loginView.setEnabled(True)

        else:
            QMessageBox(
                QMessageBox.Icon.Critical,
                'Erro de inicialização',
                f'não foi possível inicializar a aplicação\nerror : {error}',
                parent=loginView
            ).exec()

            QApplication.instance().quit()

    def on_model_authFinished(self, success:bool):
        self.__view.setDisplayMode(AppView.DisplayMode.Home if success else AppView.DisplayMode.Login)
        view = self.__view.loginView()

        if not success:
            view.setMessage('usuário ou senha incorretos!')


    def on_view_displayModeChanged(self, mode:AppView.DisplayMode):
        match mode:
            case AppView.DisplayMode.Login:
                view = self.__view.loginView()
                view.loginRequired.connect(self.__model.auth)
            
            case AppView.DisplayMode.Home:
                self.__homeController.setView(self.__view.homeView())

    #----------------------------------------------------------
