from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QDialog
import logging as log

from ..models.appModel import AppModel
from ..models.regModel import RegModel
from ..views.appView import AppView
from ..views.regView import RegView
from ..views.dialog.regTableParamsDialog import RegTableParamsDialog
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
        view.paramsRequired.connect(self.on_view_paramsRequired)
        view.deleteRequired.connect(self.__appmodel.deleteRegistries)
        view.editRequired.connect(self.on_view_editRequired)
        view.clearRequired.connect(self.on_view_clearRequired)
        view.saveRequired.connect(self.on_view_saveRequired)
        view.newRequired.connect(self.on_view_newRequired)
        view.newCategoryRequired.connect(self.on_view_newCategoryRequired)
        view.newCardRequired.connect(self.on_view_newCardRequired)
        view.tableSelectionChanged.connect(self.on_view_tableSelectionChanged)

        model.regsChanged.connect(self.on_model_regsChanged)
        self.__updateViewTable(True)
        
    #----------------------------------------------------------
    # Events
    def on_view_paramsRequired(self):
        view = RegTableParamsDialog(self.__model.getTableParams(), self.__view)

        if QDialog.DialogCode.Accepted == view.exec():
            self.__model.setTableParams(view.getParams())

    def on_view_editRequired(self):
        self.__view.setDetailsEditable(True)

    def on_view_clearRequired(self):
        reg = self.__model.getRegistry()
        
        if reg:
            self.__view.setDetailsData(reg)
        else:
            self.__view.clearDetails()

    def on_view_saveRequired(self, reg:Registry):
        old = self.__model.getRegistry()
        if old: # edit required
            reg.id = old.id
            self.__appmodel.updateRegistry(reg)
            return
        
        # save required
        self.__appmodel.newRegistry(reg)
    
    def on_view_newRequired(self):
        self.__view.clearDetails()
        self.__model.setRegistry(None)
        self.__view.setDetailsEditable(False)

    def on_view_newCategoryRequired(self): ...
    def on_view_newCardRequired(self): ...

    def on_view_tableSelectionChanged(self, indexes:set[int]):
        hasData = bool(indexes)

        self.__view.setDeleteVisible(hasData)
        self.__view.setDetailsVisible(hasData)
        
        if not hasData:
            self.__model.setRegistry(None)
            return
        
        reg = self.__model.getRegistries()[tuple(indexes)[0]]
        self.__model.setRegistry(reg)
        self.__view.setDetailsData(reg)
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
        self.__model.setRegistry(None)

        if setData:
            self.__view.setTableData(self.__model.getRegistries())
    #----------------------------------------------------------
