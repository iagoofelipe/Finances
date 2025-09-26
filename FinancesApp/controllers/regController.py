from PySide6.QtCore import QObject, Signal

from ..models.appModel import AppModel
from ..views.appView import AppView
from ..views.regView import RegView

class RegController(QObject):
    def __init__(self, model:AppModel, appview:AppView):
        super().__init__()
        self.__model = model
        self.__appView = appview

    #----------------------------------------------------------
    # Public Methods
    def setView(self, view:RegView):
        self.__view = view

    #----------------------------------------------------------
    # Events

    #----------------------------------------------------------
