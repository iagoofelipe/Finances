from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal
from dataclasses import fields

from finances.ui.auto.ui_CreateAccountForm import Ui_CreateAccountForm
from finances.core.structs import User
from finances.core.tools import generateStyleSheet

class CreateAccountForm(QWidget):
    backRequired = Signal()
    continueRequired = Signal(User)

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_CreateAccountForm()

        # setting components
        self.__ui.setupUi(self)
        self.setStyleSheet(generateStyleSheet(
            inputs=['QWidget#widUser', 'QWidget#widNome', 'QWidget#widEmail', 'QWidget#widPass', 'QWidget#widPassConfirm'],
            highlightBtns=['QPushButton#btnSalvar'],
            secondaryButtons=['QPushButton#btnVoltar'],
        ))

        # connecting events
        self.__ui.btnVoltar.clicked.connect(self.backRequired)
        self.__ui.btnSalvar.clicked.connect(self.on_btnSalvar_clicked)
    
    def on_btnSalvar_clicked(self):
        data = self.getValues()

        for field in fields(data):
            if not getattr(data, field.name) and field.name != 'id':
                QMessageBox(QMessageBox.Warning, 'Validação de Parâmetros', 'todos os campos devem ser preenchidos!', parent=self).exec()
                return
        
        if data.password != self.__ui.lePassConfirm.text():
            QMessageBox(QMessageBox.Warning, 'Validação de Parâmetros', 'senhas divergentes!', parent=self).exec()
            return
        
        self.continueRequired.emit(data)

    def getValues(self) -> User:
        return User(
            None,
            self.__ui.leUsername.text(),
            self.__ui.leName.text(),
            self.__ui.leEmail.text(),
            self.__ui.lePassword.text(),
        )
    
    def setWaitMode(self, arg:bool):
        self.__ui.leUsername.setDisabled(arg)
        self.__ui.leName.setDisabled(arg)
        self.__ui.leEmail.setDisabled(arg)
        self.__ui.lePassword.setDisabled(arg)
        self.__ui.lePassConfirm.setDisabled(arg)
        self.__ui.btnVoltar.setDisabled(arg)
        self.__ui.btnSalvar.setDisabled(arg)