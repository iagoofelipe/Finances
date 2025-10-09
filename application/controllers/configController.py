from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from ..views.configView import ConfigView
from ..src.consts import MSG_DELETE_PROFILE
from ..views.components.dialog import MessageDialog, NewProfileDialog

class ConfigController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__model = AppModel.instance()

    def setView(self, view:ConfigView):
        self.__view = view

        # Table Perfis
        table = view.getTablePerfis()
        table.addRequired.connect(self.on_TablePerfis_addRequired)
        table.deleteRequired.connect(self.on_TablePerfis_deleteRequired)

    def on_TablePerfis_addRequired(self):
        dialog = NewProfileDialog(self.__view)
        if dialog.exec():
            self.__model.createProfile(dialog.getValues())

    def on_TablePerfis_deleteRequired(self):
        dialog = MessageDialog('Exclusão de Perfil', MSG_DELETE_PROFILE, 500, self.__view)
        print('deletar' if dialog.exec() else 'n deletar')