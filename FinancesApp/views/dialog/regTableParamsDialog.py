from PySide6.QtWidgets import QWidget, QLineEdit, QComboBox

from .tableParamsDialog import TableParamsDialog
from ...models.consts import TABLE_COLS_REG
from ...models.structs import RegTableParams, RegType

class RegTableParamsDialog(TableParamsDialog):
    def __init__(self, data:RegTableParams=None, parent:QWidget=None):
        super().__init__(TABLE_COLS_REG, data, parent, False, False)

        # setting filters' layout
        self.__leTitle = QLineEdit(self)
        self.__cbType = QComboBox(self)

        self.__cbType.addItems(['Ambos', 'Entrada', 'Saída'])
        self._filterLayout.addRow('Título', self.__leTitle)
        self._filterLayout.addRow('Tipo', self.__cbType)

        if data:
            self.setValues(data)

        self._setSize()

    def setValues(self, data:RegTableParams):
        super().setValues(data)
        self.__leTitle.setText(data.titleContains)
        
        match data.type:
            case RegType.IN: op = 'Entrada'
            case RegType.OUT: op = 'Saída'
            case None: op = 'Ambos'

        self.__cbType.setCurrentText(op)

    def getValues(self):
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