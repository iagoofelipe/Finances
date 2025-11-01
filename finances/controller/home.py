from PySide6.QtCore import QObject

from finances.model import AppModel
from finances.core.structs import Profile
from finances.view.page.home import HomePage
from finances.controller.config import ConfigController
from finances.controller.registry import RegistryController

class HomeController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__model = AppModel.instance()
        self.__configController = ConfigController(self)
        self.__regController = RegistryController(self)

    def setView(self, view:HomePage):
        self.__view = view
        model = self.__model

        view.uiChanged.connect(self.on_view_uiChanged)
        view.logoutRequired.connect(self.on_view_logoutRequired)
        model.profilesUpdated.connect(self.on_model_profilesUpdated)

        profiles = model.getProfiles()
        if profiles: self.on_model_profilesUpdated(None)

        view.setUserName(model.getUser().name)
        view.setUi(view.UI.Registry)

    def on_model_profilesUpdated(self, profiles:dict[str, Profile]):
        self.__view.setProfiles(self.__model.getProfileNames())

    def on_view_logoutRequired(self):
        self.__view.setWaitMode(True)
        self.__model.logout()

    def on_view_uiChanged(self, ui:int):
        match ui:
            case HomePage.UI.Config:
                self.__configController.setView(self.__view.getConfigForm())

            case HomePage.UI.Registry:
                self.__regController.setView(self.__view.getRegistryForm())