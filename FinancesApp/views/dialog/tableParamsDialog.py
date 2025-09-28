from PySide6.QtWidgets import QWidget, QDialog, QFormLayout
from typing import Sequence

from ...models.structs import TableParams
from ...src.ui.auto.ui_TableParamsForm import Ui_TableParamsForm

class TableParamsDialog(QDialog):
    def __init__(self, columns:Sequence[str], data:TableParams=None, parent:QWidget=None, hideFilters=True, setFixedSize=True):
        super().__init__(parent, modal=True)
        self._ui = Ui_TableParamsForm()
        
        self._ui.setupUi(self)
        if hideFilters: self._ui.gbFilters.hide()
        if setFixedSize: self.__setSize()
        self._ui.cbOrder.addItems(columns)

        self._filterLayout = QFormLayout(self._ui.gbFilters)

        # setting data
        if data:
            self._ui.cbOrder.setCurrentText(data.orderByColumn)
            self._ui.cbAlpha.setChecked(data.alphabetically)

    def getValues(self) -> TableParams:
        return TableParams(
            self._ui.cbOrder.currentText(),
            self._ui.cbAlpha.isChecked(),
        )
    
    def setValues(self, data:TableParams):
        self._ui.cbOrder.setCurrentText(data.orderByColumn)
        self._ui.cbAlpha.setChecked(data.alphabetically)
    
    def _setSize(self):
        self.adjustSize()
        self.setFixedSize(self.size())