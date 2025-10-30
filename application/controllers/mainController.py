from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from ..src.structs import Profile
from ..views.mainPageView import MainPageView
from .configController import ConfigController
from .regController import RegController

class MainController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__model = AppModel.instance()
        self.__configController = ConfigController(self)
        self.__regController = RegController(self)

    def setView(self, view:MainPageView):
        self.__view = view
        model = self.__model

        view.uiChanged.connect(self.on_view_uiChanged)
        view.logoutRequired.connect(self.on_view_logoutRequired)
        model.profilesUpdated.connect(self.on_model_profilesUpdated)

        profiles = model.getProfiles()
        if profiles: self.on_model_profilesUpdated(None)

        view.setUserName(model.getUser().name)
        view.setUi(view.UI_REG)

    def on_model_profilesUpdated(self, profiles:dict[str, Profile]):
        self.__view.setProfiles(self.__model.getProfileNames())

    def on_view_logoutRequired(self):
        self.__view.setWaitMode(True)
        self.__model.logout()

    def on_view_uiChanged(self, ui:int):
        match ui:
            case MainPageView.UI_CONFIG:
                self.__configController.setView(self.__view.getConfigView())

            case MainPageView.UI_REG:
                self.__regController.setView(self.__view.getRegView())