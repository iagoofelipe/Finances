from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from ..views.appView import AppView

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view

    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()