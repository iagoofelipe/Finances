from PySide6.QtWidgets import (
    QWidget, QDialog, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QMessageBox, QSizePolicy
)
from PySide6.QtGui import QFont

from ...src.tools import generateStyleSheet

class Dialog:
    BtnCancel = 2
    BtnSave = 4
    BtnContinue = 8
    LeftSpace = 16
    HideTitle = 32
    
    def __init__(self, title:str, btns:int=None, flags:int=0, width:int=None, parent:QWidget=None):
        self.__dialog = QDialog(parent)
        self.__dialog.setMinimumWidth(width if width else 450)
        self.__dialog.setWindowTitle(title)
        self.__dialog.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.__widContent = QWidget(self.__dialog)
        self.__font = QFont('Segoe UI', 12)
        
        self.__layout = QVBoxLayout(self.__dialog)

        if not (flags & self.HideTitle):
            lbTitle = QLabel(title, self.__dialog)
            lbTitle.setObjectName('lbTitle')
            lbTitle.setFont(QFont('Segoe UI', 15))
            lbTitle.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

            self.__layout.addWidget(lbTitle)

        self.__layout.addWidget(self.__widContent)

        if btns is not None:
            self.__generateBtns(btns, flags)

        self.__dialog.setStyleSheet(generateStyleSheet(
            title=['QLabel#lbTitle'],
            highlightBtns=['QPushButton#btnSave', 'QPushButton#btnContinue'],
            secondaryButtons=['QPushButton#btnCancel']
        ))

    def validate(self):
        if self.isValid():
            self.__dialog.accept()
        
        else:
            self.alertNotValid()

    def isValid(self) -> bool: return True

    def alertNotValid(self): ...

    def getParent(self) -> QWidget: return self.__dialog
    def getFont(self) -> QFont: return self.__font

    def setWidget(self, wid:QWidget):
        widOld = self.__widContent
        self.__widContent = wid

        self.__layout.replaceWidget(widOld, wid)
        widOld.deleteLater()

    def exec(self) -> bool:
        return self.__dialog.exec() == QDialog.DialogCode.Accepted

    def __generateBtns(self, btns:int, flags:int):
        if btns & self.BtnSave and btns & self.BtnContinue:
            raise ValueError('Save and Continue cannot be passed together')
        
        widBtns = QWidget(self.__dialog)
        widBtns.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        btnsLayout = QHBoxLayout(widBtns)
        btnsLayout.setContentsMargins(0, 0, 0, 0)
        btnsLayout.setSpacing(6)
        
        if flags & self.LeftSpace:
            btnsLayout.addStretch()

        if btns & self.BtnCancel:
            btnCancel = QPushButton('cancelar', widBtns)
            btnCancel.setObjectName('btnCancel')
            btnCancel.setFont(self.__font)
            btnCancel.clicked.connect(self.__dialog.reject)
            btnsLayout.addWidget(btnCancel)
        
        if btns & self.BtnSave:
            btnSave = QPushButton('salvar', widBtns)
            btnSave.setObjectName('btnSave')
            btnSave.setFont(self.__font)
            btnSave.clicked.connect(self.validate)
            btnsLayout.addWidget(btnSave)

        if btns & self.BtnContinue:
            btnContinue = QPushButton('continuar', widBtns)
            btnContinue.setObjectName('btnContinue')
            btnContinue.setFont(self.__font)
            btnContinue.clicked.connect(self.validate)
            btnsLayout.addWidget(btnContinue)
        
        self.__layout.addWidget(widBtns)

class MessageDialog(Dialog):
    def __init__(self, title:str, content:str, width:int=None, parent:QWidget=None):
        super().__init__(title, self.BtnContinue | self.BtnCancel | self.HideTitle | self.LeftSpace, width, parent=parent)
        lb = QLabel(content, self.getParent())
        lb.setFont(self.getFont())
        lb.setWordWrap(True)
        self.setWidget(lb)

class NewProfileDialog(Dialog):
    def __init__(self, parent:QWidget=None):
        super().__init__('Novo Perfil', self.BtnSave | self.BtnCancel, width=400, parent=parent)
        widName = QWidget(self.getParent())
        widName.setObjectName('widName')

        nameLayout = QVBoxLayout(widName)
        nameLayout.setContentsMargins(10, 10, 10, 10)
        nameLayout.setSpacing(0)

        lbName = QLabel('Nome', widName)
        nameLayout.addWidget(lbName)
        
        self.__leName = leName = QLineEdit(widName)
        leName.setFont(self.getFont())
        nameLayout.addWidget(leName)

        self.setWidget(widName)

        widName.setStyleSheet(generateStyleSheet(
            inputs=['QWidget#widName']
        ))

    def isValid(self):
        return bool(self.__leName.text())
    
    def alertNotValid(self):
        QMessageBox(QMessageBox.Warning, 'Validação de Parâmetros', 'O campo Nome não pode ser vazio!', parent=self.getParent()).exec()
    
    def getValues(self) -> str:
        return self.__leName.text()