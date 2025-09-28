from PySide6.QtCore import QObject, Signal

from .appModel import AppModel
from .structs import RegTableParams, Registry, NavigableData
from .consts import MAX_ITEMS_TABLE

class RegModel(QObject):
    regsChanged = Signal(tuple)

    def __init__(self, model:AppModel, parent:QObject=None):
        super().__init__(parent)
        self.__model = model
        self.__nav = NavigableData(model.getRegistries(), MAX_ITEMS_TABLE)
        self.__tableParams = None
        
        self.setTableParams(RegTableParams('Data Hora'))
        
    def navigation(self): return self.__nav

    def setTableParams(self, params:RegTableParams):
        if self.__tableParams == params:
            return
        
        self.__tableParams = params

        # TODO: change data by params

        self.regsChanged.emit(self.__nav.currentInterval())

    def getTableParams(self): return self.__tableParams

    def getCardNames(self) -> list[str]:
        return [ c.name for c in self.__model.getCards() ]
    
    def getCategoryNames(self) -> list[str]:
        return [ c.name for c in self.__model.getCategories() ]
    
    def isEdit(self):
        return self.__reg is None
    
    def getRegistries(self): return self.__nav.currentInterval()

    def next(self): self.regsChanged.emit(self.__nav.next())

    def previous(self): self.regsChanged.emit(self.__nav.previous())

    def hasNext(self): return self.__nav.hasNext()

    def hasPrevious(self): return self.__nav.hasPrevious()
    
    def on_model_regsChanged(self, data:tuple[Registry]):
        self.__nav.setData(data)
        self.regsChanged.emit(self.__nav.currentInterval())
