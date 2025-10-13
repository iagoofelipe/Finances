from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from ..models.configModel import ConfigModel
from ..views.configView import ConfigView
from ..src.consts import MSG_DELETE_PROFILE
from ..views.components.dialog import MessageDialog, NewProfileDialog

class ConfigController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__appmodel = AppModel.instance()
        self.__model = ConfigModel(self)
        self.__view = None

    def setView(self, view:ConfigView):
        self.__view = view
        
        view.destroyed.connect(self.on_view_destroyed)
        self.__model.profilesUpdated.connect(self.on_model_profilesUpdated)
        self.__model.thirdAccessesUpdated.connect(self.on_model_thirdAccessesUpdated)

        # Table Perfis
        table = view.getTablePerfis()
        table.addRequired.connect(self.on_TablePerfis_addRequired)
        table.deleteRequired.connect(self.on_TablePerfis_deleteRequired)

        view.setUser(self.__appmodel.getUser())
        profiles = self.__appmodel.getProfiles()
        thirds = self.__appmodel.getProfileThirdAcesses()

        if profiles: self.__model.on_model_profilesUpdated(profiles)
        if thirds: self.__model.on_model_thirdAccessesUpdated(thirds)


    def on_view_destroyed(self):
        self.__view = None

    def on_model_profilesUpdated(self):
        if not self.__view: return

        tablePerfis = self.__view.getTablePerfis()
        tablePerfis.setData(self.__model.getProfilesForTable())

        tableShare = self.__view.getTableShare()
        tableShare.setData(self.__model.getPendingProfileShares())

        self.__view.setProfiles([ p.name for p in self.__appmodel.getOwnProfiles().values() ])
    
    def on_model_thirdAccessesUpdated(self):
        if not self.__view: return

        tableEdicao = self.__view.getTableEdicao()
        tableEdicao.setData(self.__model.getEditionProfiles())

        tableView = self.__view.getTableVisualizacao()
        tableView.setData(self.__model.getVisualizationProfiles())

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