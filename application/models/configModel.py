from PySide6.QtCore import QObject, Signal

from .appModel import AppModel
from ..src.structs import Profile, ProfileThirdAccess

class ConfigModel(QObject):
    profilesUpdated = Signal()
    thirdAccessesUpdated = Signal()

    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__model = model = AppModel.instance()
        self.__profTable = {}
        self.__profShares = {}
        self.__profEdit = {}
        self.__profView = {}

        model.profilesUpdated.connect(self.on_model_profilesUpdated)
        model.thirdAccessesUpdated.connect(self.on_model_thirdAccessesUpdated)

    def getProfilesForTable(self) -> dict[str, tuple[str, str, str]]: return self.__profTable
    def getPendingProfileShares(self) -> dict[str, tuple[str, str, str]]: return self.__profShares
    def getEditionProfiles(self) -> dict[str, tuple[str, str]]: return self.__profEdit
    def getVisualizationProfiles(self) -> dict[str, tuple[str, str]]: return self.__profView

    # def setCurrentProfile(self, profile:Profile):
        # self.__model = 

    def on_model_profilesUpdated(self, profiles:dict[str, Profile]):
        self.__profTable.clear()
        self.__profShares.clear()

        for pId, p in profiles.items():
            ownerName = 'Eu' if p.isOwner else p.ownerName
            
            if p.isOwner: access = 'Proprietário'
            elif p.editPermission: access = 'Edição'
            elif p.viewPermission: access = 'Visualização'
            else: access = 'Indefinido'

            if p.pendingShare:
                self.__profShares[pId] = (
                    ownerName,
                    p.name,
                    access
                )
            
            else:
                self.__profTable[pId] = (
                    ownerName,
                    p.name,
                    access,
                )
            
        self.profilesUpdated.emit()

    def on_model_thirdAccessesUpdated(self, thirds:list[ProfileThirdAccess]):
        self.__profEdit.clear()
        self.__profView.clear()

        for third in thirds:
            if third.editPermission:
                self.__profEdit[third.profileId] = (
                    third.userName,
                    third.status
                )

            if third.viewPermission:
                self.__profView[third.profileId] = (
                    third.userName,
                    third.status
                )

        self.thirdAccessesUpdated.emit()