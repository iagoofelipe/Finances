from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from ..src.ui.auto.ui_RegForm import Ui_RegForm
from ..models.tools import isDark

class RegView(QWidget):
    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_RegForm()
        self.__ui.setupUi(self)

        # updating icons
        if isDark():
            self.__ui.btnFilter.setIcon(QIcon(u":/root/imgs/dark-filter.svg"))
            self.__ui.btnDelete.setIcon(QIcon(u":/root/imgs/dark-trash.svg"))
            self.__ui.btnEdit.setIcon(QIcon(u":/root/imgs/dark-pen.svg"))
            self.__ui.btnAdd.setIcon(QIcon(u":/root/imgs/dark-plus.svg"))
            self.__ui.btnPrev.setIcon(QIcon(u":/root/imgs/dark-left-arrow.svg"))
            self.__ui.btnNext.setIcon(QIcon(u":/root/imgs/dark-right-arrow.svg"))