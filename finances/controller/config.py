from PySide6.QtCore import QObject

from finances.core.structs import Profile
from finances.model import AppModel, ConfigModel
from finances.view.form import ConfigForm
from finances.core.consts import MSG_DELETE_PROFILE
from finances.view.component.dialog import MessageDialog, NewProfileDialog

class ConfigController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__appmodel = AppModel.instance()
        self.__model = ConfigModel(self)
        self.__view = None

        self.__appmodel.shareProfileFinished.connect(self.on_AppModel_shareProfileFinished)

    def setView(self, view:ConfigForm):
        self.__view = view
        
        view.destroyed.connect(self.on_view_destroyed)
        view.thirdAccessProfileChanged.connect(self.on_view_thirdAccessProfileChanged)
        view.shareProfileRequired.connect(self.__appmodel.shareProfile)

        self.__model.profilesUpdated.connect(self.on_model_profilesUpdated)
        self.__model.thirdAccessesUpdated.connect(self.on_model_thirdAccessesUpdated)

        # Table Perfis
        table = view.getTablePerfis()
        table.addRequired.connect(self.on_TablePerfis_addRequired)
        table.deleteRequired.connect(self.on_TablePerfis_deleteRequired)

        # Table Share
        table = view.getTableShare()
        table.acceptRequired.connect(self.on_TableShare_acceptRequired)
        table.rejectRequired.connect(self.on_TableShare_rejectRequired)

        view.setUser(self.__appmodel.getUser())
        profiles = self.__appmodel.getProfiles()
        thirds = self.__appmodel.getProfileThirdAcesses()

        if profiles: self.__model.on_model_profilesUpdated(profiles)
        if thirds: self.__model.on_model_thirdAccessesUpdated(thirds)

    def on_view_destroyed(self):
        self.__view = None

    def on_view_thirdAccessProfileChanged(self, profile:Profile|None):
        self.__model.setCurrentProfileId(profile.id if profile else '')

    def on_model_profilesUpdated(self):
        if not self.__view: return

        tablePerfis = self.__view.getTablePerfis()
        tablePerfis.setData(self.__model.getProfilesForTable())

        tableShare = self.__view.getTableShare()
        tableShare.setData(self.__model.getPendingProfileShares())

        self.__view.setProfiles(self.__appmodel.getOwnProfiles().values())
    
    def on_model_thirdAccessesUpdated(self):
        if not self.__view: return

        tableEdicao = self.__view.getTableEdicao()
        tableEdicao.setData(self.__model.getEditionProfiles())

        tableView = self.__view.getTableVisualizacao()
        tableView.setData(self.__model.getVisualizationProfiles())

    def on_AppModel_shareProfileFinished(self, success:bool, msg:str|None):
        if not success or not self.__view: return

        self.__appmodel.requireProfileThirdAcesses()

    def on_TablePerfis_addRequired(self):
        dialog = NewProfileDialog(self.__view)
        if dialog.exec():
            self.__appmodel.createProfile(dialog.getValues())

    def on_TablePerfis_deleteRequired(self):
        table = self.__view.getTablePerfis()
        profileId = table.getSelectedKeys()[0]
        profileName = self.__appmodel.getProfileById(profileId).name

        dialog = MessageDialog('Exclusão de Perfil', MSG_DELETE_PROFILE % profileName, 500, self.__view)
        print('deletar' if dialog.exec() else 'n deletar')

    def on_TableShare_acceptRequired(self):
        self.__pendingShare(True)

    def on_TableShare_rejectRequired(self):
        self.__pendingShare(False)

    def __pendingShare(self, accept:bool):
        profileId = self.__view.getTableShare().getSelectedKeys()[0]
        roleId = self.__appmodel.getProfileById(profileId).roleId
        
        self.__appmodel.pendingShare(roleId, accept)
