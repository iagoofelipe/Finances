from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from typing import Sequence

from ..src.ui.auto.ui_ConfigForm import Ui_ConfigForm
from ..src.tools import generateStyleSheet
from .components.table import TableWidget

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

        # nameWidOld, layout, columns, title, flags
        tables = (
            ('widPerfis', self.__ui.gridLayout, ['Proprietário', 'Perfil', 'Tipo de Acesso'], 'Perfis', TableWidget.ShowNavAsNeeded | TableWidget.BtnDelete | TableWidget.BtnAdd),
            ('widShare', self.__ui.gridLayout, ['Proprietário', 'Perfil', 'Compartilhamento'], 'Compartilhamentos Pendentes', TableWidget.ShowNavAsNeeded | TableWidget.BtnAccept | TableWidget.BtnReject),
            ('widEdicao', self.__ui.acessoPerfilLayout, ['Usuário', 'Status'], 'Edição', TableWidget.ShowNavAsNeeded | TableWidget.BtnDelete | TableWidget.BtnAdd),
            ('widVisu', self.__ui.acessoPerfilLayout, ['Usuário', 'Status'], 'Visualização', TableWidget.ShowNavAsNeeded | TableWidget.BtnDelete | TableWidget.BtnAdd),
        )

        for nameWidOld, layout, columns, title, flags in tables:
            widOld = getattr(self.__ui, nameWidOld)
            table = TableWidget(columns, title, flags, parent=self)
            setattr(self.__ui, nameWidOld, table)
            layout.replaceWidget(widOld, table)
            widOld.deleteLater()

    def getTablePerfis(self) -> TableWidget: return self.__ui.widPerfis
    def getTableShare(self) -> TableWidget: return self.__ui.widShare
    def getTableEdicao(self) -> TableWidget: return self.__ui.widEdicao
    def getTableVisualizacao(self) -> TableWidget: return self.__ui.widVisu

    def setProfiles(self, profiles:Sequence[str]):
        cb = self.__ui.cbPerfil
        text = cb.currentText()
        values = sorted(map(lambda p: p.name, profiles))
        
        cb.clear()
        cb.addItems(values)

        if text in values:
            cb.setCurrentText(text)
        
        cb.clear()
        cb.addItems(values)

        if text in values:
            cb.setCurrentText(text)

        # tablePerfis = self.getTablePerfis()
        # tablePerfis.setData([()])