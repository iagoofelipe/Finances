from PySide6.QtWidgets import (
    QWidget, QDialog, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QSizePolicy
)
from PySide6.QtGui import QFont

from finances.core.tools import generateStyleSheet

class Dialog:
    
    class Button:
        Cancel = 2
        Save = 4
        Continue = 8

    class Style:
        LeftSpace = 16
        HideTitle = 32
    
    def __init__(self, title:str, flags:int=0, width:int=None, parent:QWidget=None):
        self.__dialog = QDialog(parent)
        self.__dialog.setMinimumWidth(width if width else 450)
        self.__dialog.setWindowTitle(title)
        self.__dialog.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.__widContent = QWidget(self.__dialog)
        self.__font = QFont('Segoe UI', 12)
        
        self.__layout = QVBoxLayout(self.__dialog)

        if not (flags & self.Style.HideTitle):
            lbTitle = QLabel(title, self.__dialog)
            lbTitle.setObjectName('lbTitle')
            lbTitle.setFont(QFont('Segoe UI', 15))
            lbTitle.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

            self.__layout.addWidget(lbTitle)

        self.__layout.addWidget(self.__widContent)

        if (flags & self.Button.Cancel) or (flags & self.Button.Save) or (flags & self.Button.Continue):
            self.__generateBtns(flags)

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

    def __generateBtns(self, flags:int):
        if flags & self.Button.Save and flags & self.Button.Continue:
            raise ValueError('Save and Continue cannot be passed together')
        
        widBtns = QWidget(self.__dialog)
        widBtns.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        btnsLayout = QHBoxLayout(widBtns)
        btnsLayout.setContentsMargins(0, 0, 0, 0)
        btnsLayout.setSpacing(6)
        
        if flags & self.Style.LeftSpace:
            btnsLayout.addStretch()

        if flags & self.Button.Cancel:
            btnCancel = QPushButton('cancelar', widBtns)
            btnCancel.setObjectName('btnCancel')
            btnCancel.setFont(self.__font)
            btnCancel.clicked.connect(self.__dialog.reject)
            btnsLayout.addWidget(btnCancel)
        
        if flags & self.Button.Save:
            btnSave = QPushButton('salvar', widBtns)
            btnSave.setObjectName('btnSave')
            btnSave.setFont(self.__font)
            btnSave.clicked.connect(self.validate)
            btnsLayout.addWidget(btnSave)

        if flags & self.Button.Continue:
            btnContinue = QPushButton('continuar', widBtns)
            btnContinue.setObjectName('btnContinue')
            btnContinue.setFont(self.__font)
            btnContinue.clicked.connect(self.validate)
            btnsLayout.addWidget(btnContinue)
        
        self.__layout.addWidget(widBtns)
    