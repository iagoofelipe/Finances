from PySide6.QtWidgets import QWidget, QDialog

from ...models.structs import DashParams, RegType
from ...src.ui.auto.ui_DashParamsForm import Ui_DashParamsForm

class DashParamsDialog(QDialog):
    def __init__(self, data:DashParams=None, parent:QWidget=None):
        super().__init__(parent, modal=True)
        self.__ui = Ui_DashParamsForm()

        self.__ui.setupUi(self)
        self.setFixedSize(558, 412)

        # setting data
        if data:
            self.setValues(data)

        else:
            self.__ui.rbIn.setChecked(True)

    def setValues(self, data:DashParams):
        self.__ui.dtStart.setDate(data.start)
        self.__ui.dtEnd.setDate(data.end)
        
        if data.regType == RegType.IN:
            self.__ui.rbIn.setChecked(True)
        else:
            self.__ui.rbOut.setChecked(True)

    def getValues(self) -> DashParams:
        return DashParams(
            self.__ui.dtStart.date(),
            self.__ui.dtEnd.date(),
            RegType.IN if self.__ui.rbIn.isChecked() else RegType.OUT
        )