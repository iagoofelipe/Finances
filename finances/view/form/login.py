from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal

from finances.ui.auto.ui_LoginForm import Ui_LoginForm
from finances.core.structs import LoginData
from finances.core.tools import generateStyleSheet

class LoginForm(QWidget):
    continueRequired = Signal(LoginData)
    createAccountRequired = Signal()
    passwordForgot = Signal()

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_LoginForm()
        
        # setting components
        self.__ui.setupUi(self)
        self.setStyleSheet(generateStyleSheet(
            inputs=['QWidget#widUser', 'QWidget#widPass'],
            highlightBtns=['QPushButton#btnAcessar'],
            linkBtns=['QPushButton#btnCriar', 'QPushButton#btnEsqueci']
        ))

        # connecting events
        self.__ui.btnAcessar.clicked.connect(self.on_btnAcessar_clicked)
        self.__ui.btnCriar.clicked.connect(self.createAccountRequired)
        self.__ui.btnEsqueci.clicked.connect(self.passwordForgot)
    
    def on_btnAcessar_clicked(self):
        data = self.getValues()

        if not data.username or not data.password:
            QMessageBox(QMessageBox.Warning, 'Validação de Parâmetros', 'todos os campos devem ser preenchidos!', parent=self).exec()
            return
        
        self.continueRequired.emit(data)

    def getValues(self) -> LoginData:
        return LoginData(
            self.__ui.leUsername.text(),
            self.__ui.lePassword.text(),
            self.__ui.cbLembrar.isChecked()
        )

    def setWaitMode(self, arg:bool):
        self.__ui.leUsername.setDisabled(arg)
        self.__ui.lePassword.setDisabled(arg)
        self.__ui.cbLembrar.setDisabled(arg)
        self.__ui.btnAcessar.setDisabled(arg)
        self.__ui.btnCriar.setDisabled(arg)
        self.__ui.btnEsqueci.setDisabled(arg)