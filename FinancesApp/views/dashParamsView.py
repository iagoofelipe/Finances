from PySide6.QtWidgets import QWidget, QDialog

from ..models.structs import DashParams, RegType
from ..src.ui.auto.ui_DashParamsForm import Ui_DashParamsForm

class DashParamsView(QDialog):
    def __init__(self, params:DashParams=None, parent:QWidget=None):
        super().__init__(parent, modal=True)
        self.__ui = Ui_DashParamsForm()

        self.__ui.setupUi(self)
        self.setFixedSize(558, 412)

        # setting params
        if params:
            self.__ui.dtStart.setDate(params.start)
            self.__ui.dtEnd.setDate(params.end)
            
            if params.regType == RegType.IN:
                self.__ui.rbIn.setChecked(True)
            else:
                self.__ui.rbOut.setChecked(True)

        else:
            self.__ui.rbIn.setChecked(True)

    def getParams(self) -> DashParams:
        return DashParams(
            self.__ui.dtStart.date(),
            self.__ui.dtEnd.date(),
            RegType.IN if self.__ui.rbIn.isChecked() else RegType.OUT
        )