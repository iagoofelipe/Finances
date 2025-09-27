from PySide6.QtWidgets import QWidget, QLineEdit, QComboBox

from .tableParamsDialog import TableParamsDialog
from ...models.consts import TABLE_COLS_REG
from ...models.structs import RegTableParams, RegType

class RegTableParamsDialog(TableParamsDialog):
    def __init__(self, params:RegTableParams=None, parent:QWidget=None):
        super().__init__(TABLE_COLS_REG, params, parent, False, False)

        # setting filters' layout
        self.__leTitle = QLineEdit(self)
        self.__cbType = QComboBox(self)

        self.__cbType.addItems(['Ambos', 'Entrada', 'Saída'])
        self._filterLayout.addRow('Título', self.__leTitle)
        self._filterLayout.addRow('Tipo', self.__cbType)

        if params:
            self.setParams(params)

        self._setSize()

    def setParams(self, params:RegTableParams):
        super().setParams(params)
        self.__leTitle.setText(params.titleContains)
        
        match params.type:
            case RegType.IN: op = 'Entrada'
            case RegType.OUT: op = 'Saída'
            case None: op = 'Ambos'

        self.__cbType.setCurrentText(op)

    def getParams(self):
        match self.__cbType.currentText():
            case 'Ambos': regType = None
            case 'Entrada': regType = RegType.IN
            case 'Saída': regType = RegType.OUT

        return RegTableParams(
            self._ui.cbOrder.currentText(),
            self._ui.cbAlpha.isChecked(),
            self.__leTitle.text(),
            regType
        )