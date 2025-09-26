from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from ..views.appView import AppView
from ..views.homeView import HomeView
from .regController import RegController

class HomeController(QObject):
    def __init__(self, model:AppModel, appview:AppView):
        super().__init__()
        self.__model = model
        self.__appView = appview
        self.__regController = RegController(model, appview)

    #----------------------------------------------------------
    # Public Methods
    def setView(self, view:HomeView):
        self.__view = view
        view.logoutRequired.connect(self.on_HomeView_logoutRequired)
        view.displayModeChanged.connect(self.on_HomeView_displayModeChanged)

    #----------------------------------------------------------
    # Events
    def on_HomeView_logoutRequired(self):
        self.__model.clearCredentials()
        self.__appView.setDisplayMode(AppView.DisplayMode.Login)

    def on_HomeView_displayModeChanged(self, mode:HomeView.DisplayMode):
        match mode:
            case HomeView.DisplayMode.Reg:
                self.__regController.setView(self.__view.regView())

    #----------------------------------------------------------
