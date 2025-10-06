from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QObject, Signal

from .loginController import LoginController
from ..views.appView import AppView
from ..models.appModel import AppModel

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view
        self.__loginController = LoginController(self)

        view.uiChanged.connect(self.on_view_uiChanged)
        model.initializationFinished.connect(self.on_model_initializationFinished)
    
    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()

    def on_view_uiChanged(self, ui:int):
        match ui:
            case AppView.UI_LOGIN:
                self.__loginController.setView(self.__view.getLoginView())

    def on_model_initializationFinished(self, success:bool):
        if success:
            view = self.__view.getLoginView()
            view.setUi(view.UI_FORM)
        
        else:
            QMessageBox(QMessageBox.Warning, 'Inicialização', 'Não foi possível inicializar os componentes').exec()
            QApplication.instance().quit()