from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox
import logging as log

from ..models.appModel import AppModel
from ..models.regModel import RegModel
from ..views.appView import AppView
from ..views.regView import RegView
from ..models.structs import Registry

class RegController(QObject):
    def __init__(self, appmodel:AppModel, appview:AppView):
        super().__init__()
        self.__model = RegModel(appmodel, self)
        self.__appmodel = appmodel
        self.__appView = appview

    #----------------------------------------------------------
    # Public Methods
    def setView(self, view:RegView):
        log.debug('[RegController::setView] view set')
        self.__view = view
        model = self.__model
        
        view.setModel(model)

        view.previousRequired.connect(model.previous)
        view.nextRequired.connect(model.next)
        view.deleteRequired.connect(self.__appmodel.deleteRegistries)
        view.editRequired.connect(self.on_view_editRequired)
        view.clearRequired.connect(self.on_view_clearRequired)
        view.saveRequired.connect(self.on_view_saveRequired)
        view.newRequired.connect(self.on_view_newRequired)
        view.newCategoryRequired.connect(self.__appmodel.newCategory)
        view.newCardRequired.connect(self.__appmodel.newCard)
        view.tableSelectionChanged.connect(self.on_view_tableSelectionChanged)

        model.regsChanged.connect(self.on_model_regsChanged)
        self.__updateViewTable(True)
        
    #----------------------------------------------------------
    # Events
    def on_view_editRequired(self):
        self.__view.setDetailsEditable(True)

    def on_view_clearRequired(self):
        reg = self.__view.getNotEdittedData()
        
        if reg:
            self.__view.setDetailsData(reg)
        else:
            self.__view.clearDetails()

    def on_view_saveRequired(self, reg:Registry):
        old = self.__view.getNotEdittedData()

        # edit required
        if old is not None:
            if old == reg:
                QMessageBox(QMessageBox.Icon.Information, 'Atualização de Registro', 'Nenhuma alteração encontrada!', parent=self.__view).exec()
                return

            # saving changes
            self.__appmodel.updateRegistry(reg)
            return
        
        # new required
        self.__appmodel.newRegistry(reg)
        self.__view.clearDetails()
        self.__view.setDetailsVisible(False)
    
    def on_view_newRequired(self):
        self.__view.clearDetails()
        self.__view.setDetailsEditable(True)

    def on_view_tableSelectionChanged(self, indexes:set[int]):
        hasData = bool(indexes)
        reg = self.__model.getRegistries()[tuple(indexes)[0]] if hasData else None

        self.__view.setDeleteVisible(hasData)
        self.__view.setDetailsVisible(hasData)
        self.__view.setDetailsData(reg)
        
        if hasData:
            self.__view.setDetailsEditable(False)

    def on_model_regsChanged(self, data:tuple[Registry]):
        self.__view.setTableData(data)
        self.__updateViewTable()

    #----------------------------------------------------------
    # Private Methods
    def __updateViewTable(self, setData=False):
        nav = self.__model.navigation()
        self.__view.setTableLabel(nav.start, nav.end, len(nav))
        self.__view.setPreviousAvailable(nav.hasPrevious())
        self.__view.setNextAvailable(nav.hasNext())
        self.__view.setDetailsData(None)

        if setData:
            self.__view.setTableData(self.__model.getRegistries())
    #----------------------------------------------------------
