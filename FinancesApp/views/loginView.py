from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from ..src.ui.auto.ui_LoginForm import Ui_LoginForm
from ..models.appModel import AppModel

class LoginView(QWidget):
    loginRequired = Signal(str, str, bool)

    def __init__(self, model:AppModel, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_LoginForm()
        self.__ui.setupUi(self)
        self.__ui.lbAlert.hide()

        self.__ui.leUser.returnPressed.connect(self.on_btnLogin_clicked)
        self.__ui.lePassword.returnPressed.connect(self.on_btnLogin_clicked)
        self.__ui.btnLogin.clicked.connect(self.on_btnLogin_clicked)

    def on_btnLogin_clicked(self):
        user = self.__ui.leUser.text()
        pswd = self.__ui.lePassword.text()

        if not user or not pswd:
            self.setMessage('preencha todos os campos para prosseguir!')
            return
        
        self.loginRequired.emit(user, pswd, self.__ui.cbKeep.isChecked())

    def setMessage(self, text:str):
        self.__ui.lbAlert.show()
        self.__ui.lbAlert.setText(text)