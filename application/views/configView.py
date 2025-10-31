from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from typing import Sequence

from ..src.ui.auto.ui_ConfigForm import Ui_ConfigForm
from ..src.structs import User, Profile, ShareProfile
from ..src.tools import isDarkTheme, generateStyleSheet
from ..src.consts import SHARE_TYPE_EDIT, SHARE_TYPE_VIEW
from .components.table import TableWidget
from .components.shareProfileDialog import ShareProfileDialog

class ConfigView(QWidget):
    TITLE = 'configurações'

    updatePasswordRequired = Signal(str, str)
    thirdAccessProfileChanged = Signal(object) # Profile | None
    shareProfileRequired = Signal(ShareProfile)

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_ConfigForm()
        self.__user = None
        self.__profiles = None
        self.__profilesByName = {}
        self.__theme = 'light'

        self.__ui.setupUi(self)
        self.setStyleSheet(generateStyleSheet(
            inputs=['QWidget#widNome', 'QWidget#widEmail', 'QWidget#widSenhaAtual', 'QWidget#widSenhaNova', 'QWidget#widSenhaConfirm'],
            highlightBtns=['QPushButton#btnEditarUser', 'QPushButton#btnSalvarUser', 'QPushButton#btnSalvarSenha', 'QPushButton#btnAtualizarSenha'],
            secondaryButtons=['QPushButton#btnCancelarUser', 'QPushButton#btnCancelarSenha'],
            title=['QLabel#lbSenhaUsuario', 'QLabel#lbDadosUsuario', 'QLabel#lbTerceiros'],
        ))
        
        self.on_btnCancelarUser_clicked()
        self.on_btnCancelarSenha_clicked()
        self.__ui.btnSenhaAtualHide.hide()
        self.__ui.btnSenhaNovaHide.hide()
        self.__ui.btnSenhaConfirmHide.hide()

        # nameWidOld, layout, columns, title, flags
        t = TableWidget
        tables = (
            ('widPerfis', self.__ui.gridLayout, ['Proprietário', 'Perfil', 'Tipo de Acesso'], 'Perfis', t.Style.ShowNavAsNeeded | t.Behavior.DeleteJustOne | t.Behavior.SelectJustOne | t.Button.Delete | t.Button.Add),
            ('widShare', self.__ui.gridLayout, ['Proprietário', 'Perfil', 'Compartilhamento'], 'Compartilhamentos Pendentes', t.Style.ShowNavAsNeeded | t.Behavior.SelectJustOne | t.Button.Accept | t.Button.Reject),
            ('widEdicao', self.__ui.acessoPerfilLayout, ['Usuário', 'Status'], 'Edição', t.Style.ShowNavAsNeeded | t.Style.InsideNoFrame | t.Button.Delete | t.Button.Add),
            ('widVisu', self.__ui.acessoPerfilLayout, ['Usuário', 'Status'], 'Visualização', t.Style.ShowNavAsNeeded | t.Style.InsideNoFrame | t.Button.Delete | t.Button.Add),
        )

        for nameWidOld, layout, columns, title, flags in tables:
            widOld = getattr(self.__ui, nameWidOld)
            table = TableWidget(columns, title, flags, parent=self)
            table.setMinimumHeight(250)
            setattr(self.__ui, nameWidOld, table)
            layout.replaceWidget(widOld, table)
            widOld.deleteLater()

        self.__ui.btnEditarUser.clicked.connect(self.on_btnEditarUser_clicked)
        self.__ui.btnCancelarUser.clicked.connect(self.on_btnCancelarUser_clicked)
        self.__ui.btnCancelarSenha.clicked.connect(self.on_btnCancelarSenha_clicked)
        self.__ui.btnAtualizarSenha.clicked.connect(self.on_btnAtualizarSenha_clicked)
        self.__ui.btnSenhaAtualHide.clicked.connect(self.on_btnSenhaAtualHide_clicked)
        self.__ui.btnSenhaAtualShow.clicked.connect(self.on_btnSenhaAtualShow_clicked)
        self.__ui.btnSenhaNovaHide.clicked.connect(self.on_btnSenhaNovaHide_clicked)
        self.__ui.btnSenhaNovaShow.clicked.connect(self.on_btnSenhaNovaShow_clicked)
        self.__ui.btnSenhaConfirmHide.clicked.connect(self.on_btnSenhaConfirmHide_clicked)
        self.__ui.btnSenhaConfirmShow.clicked.connect(self.on_btnSenhaConfirmShow_clicked)
        self.__ui.cbPerfil.currentTextChanged.connect(self.on_cbPerfil_currentTextChanged)
        self.__ui.widEdicao.addRequired.connect(lambda: self.requireShareProfileData(SHARE_TYPE_EDIT))
        self.__ui.widVisu.addRequired.connect(lambda: self.requireShareProfileData(SHARE_TYPE_VIEW))

        self.updateTheme()

    def updateTheme(self):
        isdark = isDarkTheme()
        
        # if is up to date
        if (isdark and self.__theme == 'dark') or (not isdark and self.__theme == 'light'):
            return
        
        prefix = 'dark_' if isdark else 'light_'
        self.__ui.btnSenhaAtualHide.setIcon(QIcon(f':/root/icons/{prefix}eye-off.svg'))
        self.__ui.btnSenhaAtualShow.setIcon(QIcon(f':/root/icons/{prefix}eye.svg'))
        self.__ui.btnSenhaNovaHide.setIcon(QIcon(f':/root/icons/{prefix}eye-off.svg'))
        self.__ui.btnSenhaNovaShow.setIcon(QIcon(f':/root/icons/{prefix}eye.svg'))
        self.__ui.btnSenhaConfirmHide.setIcon(QIcon(f':/root/icons/{prefix}eye-off.svg'))
        self.__ui.btnSenhaConfirmShow.setIcon(QIcon(f':/root/icons/{prefix}eye.svg'))

    def getTablePerfis(self) -> TableWidget: return self.__ui.widPerfis
    def getTableShare(self) -> TableWidget: return self.__ui.widShare
    def getTableEdicao(self) -> TableWidget: return self.__ui.widEdicao
    def getTableVisualizacao(self) -> TableWidget: return self.__ui.widVisu

    def setUser(self, user:User):
        self.__user = user
        self.__ui.leNome.setText(user.name)
        self.__ui.leEmail.setText(user.email)

    def getCurrentProfile(self) -> Profile | None:
        return self.__profilesByName.get(self.__ui.cbPerfil.currentText())

    def setProfiles(self, profiles:Sequence[Profile]):
        cb = self.__ui.cbPerfil
        text = cb.currentText()
        self.__profiles = profiles
        self.__profilesByName = { p.name : p for p in profiles }
        values = sorted(self.__profilesByName)

        cb.clear()
        cb.addItems(values)

        if text in values:
            cb.setCurrentText(text)
        
        cb.clear()
        cb.addItems(values)

        if text in values:
            cb.setCurrentText(text)

    def requireShareProfileData(self, shareType:int=None):
        dialog = ShareProfileDialog(self.__ui.widget_16, self.__profiles, self.getCurrentProfile(), shareType)
        if dialog.exec():
            self.shareProfileRequired.emit(dialog.getData())

    def on_btnEditarUser_clicked(self):
        self.__ui.btnCancelarUser.show()
        self.__ui.btnSalvarUser.show()
        self.__ui.btnEditarUser.hide()
        self.__ui.leNome.setReadOnly(False)
        self.__ui.leEmail.setReadOnly(False)

    def on_btnCancelarUser_clicked(self):
        self.__ui.btnCancelarUser.hide()
        self.__ui.btnSalvarUser.hide()
        self.__ui.btnEditarUser.show()
        self.__ui.leNome.setReadOnly(True)
        self.__ui.leEmail.setReadOnly(True)

        self.__ui.leNome.setText(self.__user.name if self.__user else '')
        self.__ui.leEmail.setText(self.__user.email if self.__user else '')

    def on_btnAtualizarSenha_clicked(self):
        self.__ui.btnCancelarSenha.show()
        self.__ui.btnSalvarSenha.show()
        self.__ui.btnAtualizarSenha.hide()
        self.__ui.leSenhaAtual.setReadOnly(False)
        self.__ui.leSenhaNova.setReadOnly(False)
        self.__ui.leSenhaConfirm.setReadOnly(False)

    def on_btnCancelarSenha_clicked(self):
        self.__ui.btnCancelarSenha.hide()
        self.__ui.btnSalvarSenha.hide()
        self.__ui.btnAtualizarSenha.show()
        self.__ui.leSenhaAtual.setReadOnly(True)
        self.__ui.leSenhaNova.setReadOnly(True)
        self.__ui.leSenhaConfirm.setReadOnly(True)

        self.__ui.leSenhaAtual.setText('')
        self.__ui.leSenhaNova.setText('')
        self.__ui.leSenhaConfirm.setText('')

    def on_btnSenhaAtualShow_clicked(self):
        self.__ui.leSenhaAtual.setEchoMode(QLineEdit.EchoMode.Normal)
        self.__ui.btnSenhaAtualShow.hide()
        self.__ui.btnSenhaAtualHide.show()
        self.__ui.leSenhaAtual.setFocus()

    def on_btnSenhaAtualHide_clicked(self):
        self.__ui.leSenhaAtual.setEchoMode(QLineEdit.EchoMode.Password)
        self.__ui.btnSenhaAtualShow.show()
        self.__ui.btnSenhaAtualHide.hide()
        self.__ui.leSenhaAtual.setFocus()

    def on_btnSenhaNovaShow_clicked(self):
        self.__ui.leSenhaNova.setEchoMode(QLineEdit.EchoMode.Normal)
        self.__ui.btnSenhaNovaShow.hide()
        self.__ui.btnSenhaNovaHide.show()
        self.__ui.leSenhaNova.setFocus()

    def on_btnSenhaNovaHide_clicked(self):
        self.__ui.leSenhaNova.setEchoMode(QLineEdit.EchoMode.Password)
        self.__ui.btnSenhaNovaShow.show()
        self.__ui.btnSenhaNovaHide.hide()
        self.__ui.leSenhaNova.setFocus()

    def on_btnSenhaConfirmShow_clicked(self):
        self.__ui.leSenhaConfirm.setEchoMode(QLineEdit.EchoMode.Normal)
        self.__ui.btnSenhaConfirmShow.hide()
        self.__ui.btnSenhaConfirmHide.show()
        self.__ui.leSenhaConfirm.setFocus()

    def on_btnSenhaConfirmHide_clicked(self):
        self.__ui.leSenhaConfirm.setEchoMode(QLineEdit.EchoMode.Password)
        self.__ui.btnSenhaConfirmShow.show()
        self.__ui.btnSenhaConfirmHide.hide()
        self.__ui.leSenhaConfirm.setFocus()

    def on_cbPerfil_currentTextChanged(self, text:str):
        self.thirdAccessProfileChanged.emit(self.getCurrentProfile())
        self.__ui.cbPerfil.setToolTip(text)