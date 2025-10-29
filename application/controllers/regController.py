from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from ..views.regView import RegView
from ..src.structs import Profile

class RegController(QObject):
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__model = AppModel.instance()
        self.__view = None

    def setView(self, view:RegView):
        self.__view = view
        
        self.__view.destroyed.connect(self.on_view_destroyed)

    def on_view_destroyed(self):
        self.__view = None

    def on_model_currentProfileChanged(self, profile:Profile|None):
        #TODO: adicionar alerta para criação de perfil
        if profile is None: return

        