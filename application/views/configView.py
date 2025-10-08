from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal

from ..src.ui.auto.ui_ConfigForm import Ui_ConfigForm
from ..src.tools import generateStyleSheet
from ..src.consts import MSG_DELETE_PROFILE
from .components.dialog import newProfilePopup, MessageDialog, NewProfileDialog

class ConfigView(QWidget):
    TITLE = 'configurações'

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_ConfigForm()

        self.__ui.setupUi(self)
        self.setStyleSheet(generateStyleSheet(
            inputs=['QWidget#widNome', 'QWidget#widEmail', 'QWidget#widSenhaAtual', 'QWidget#widSenhaNova', 'QWidget#widSenhaConfirm'],
            highlightBtns=['QPushButton#btnEditarUser', 'QPushButton#btnSalvarUser', 'QPushButton#btnSalvarSenha', 'QPushButton#btnAtualizarSenha'],
            secondaryButtons=['QPushButton#btnCancelarUser', 'QPushButton#btnCancelarSenha']
        ))

        # tables
        tables = (
            (self.__ui.tablePerfis, ['Proprietário', 'Perfil', 'Tipo de Acesso']),
            (self.__ui.tableShare, ['Proprietário', 'Perfil', 'Compartilhamento']),
            (self.__ui.tableEdicao, ['Usuário', 'Status']),
            (self.__ui.tableVisu, ['Usuário', 'Status']),
        )

        for table, cols in tables:
            table.setColumnCount(len(cols))
            table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            table.setHorizontalHeaderLabels(cols)

        self.__ui.btnAddPerfil.clicked.connect(self.btnAddPerfil_clicked)
        self.__ui.btnDelPerfil.clicked.connect(self.on_btnDelPerfil_clicked)

    def btnAddPerfil_clicked(self):
        # newProfilePopup(self)
        dialog = NewProfileDialog(self)
        if dialog.exec():
            print('Novo perfil:', dialog.getValues())

    def on_btnDelPerfil_clicked(self):
        dialog = MessageDialog('Exclusão de Perfil', MSG_DELETE_PROFILE, 500, self)
        print('deletar' if dialog.exec() else 'n deletar')