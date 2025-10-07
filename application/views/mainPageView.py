from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from ..src.ui.auto.ui_MainPage import Ui_MainPage
from ..models.appModel import AppModel

class MainPageView(QWidget):
    logoutRequired = Signal()

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_MainPage()
        self.__model = AppModel.instance()
        user = self.__model.getUser()

        self.__ui.setupUi(self)
        self.__ui.lbText.setText(f'Olá, {user.name if user else 'Usuário'}!')

        self.__ui.btnSair.clicked.connect(self.logoutRequired)

    def setWaitMode(self, arg:bool):
        self.setDisabled(arg)