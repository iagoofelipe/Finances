from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QButtonGroup
from typing import Sequence

from ..src.ui.auto.ui_MainPage import Ui_MainPage
from .configView import ConfigView
from ..src.structs import Profile

class MainPageView(QWidget):
    logoutRequired = Signal()
    uiChanged = Signal(int)

    UI_QUANT = 0
    UI_REG = 1
    UI_CARD = 2
    UI_CONFIG = 3

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_MainPage()
        self.__currentUi = None

        self.__ui.setupUi(self)
        self.setUserName('Usuário')
        self.setTitle('')

        self.__navBtns = QButtonGroup(self)
        self.__navBtns.setExclusive(True)
        self.__navBtns.addButton(self.__ui.btnQuantitativos)
        self.__navBtns.addButton(self.__ui.btnRegs)
        self.__navBtns.addButton(self.__ui.btnCartoes)
        self.__navBtns.addButton(self.__ui.btnConfig)

        self.__navBtnsText = { btn: '' for btn in self.__navBtns.buttons() }
        self.__navBtnsText[self.__ui.btnSair] = ''
        self.__navBtnsText[self.__ui.btnNav] = ''

        # connecting events
        self.__ui.btnNav.clicked.connect(self.on_btnNav_clicked)
        self.__ui.btnQuantitativos.clicked.connect(lambda: self.setUi(self.UI_QUANT))
        self.__ui.btnRegs.clicked.connect(lambda: self.setUi(self.UI_REG))
        self.__ui.btnCartoes.clicked.connect(lambda: self.setUi(self.UI_CARD))
        self.__ui.btnConfig.clicked.connect(lambda: self.setUi(self.UI_CONFIG))
        self.__ui.btnSair.clicked.connect(self.logoutRequired)
        self.__ui.cbProfile.currentTextChanged.connect(self.on_cbProfile_currentTextChanged)

    def getConfigView(self):
        return self.__configView if self.isCurrentView(self.UI_CONFIG) else None

    def isCurrentView(self, ui:int):
        return self.__currentUi == ui

    def setUserName(self, name:str):
        self.__ui.lbTextUser.setText(f'Olá, {name}!')

    def setTitle(self, text:str):
        self.__ui.lbTitle.setText(text)

    def setWaitMode(self, arg:bool):
        self.setDisabled(arg)

    def setProfiles(self, profiles:Sequence[Profile]):
        cb = self.__ui.cbProfile
        text = cb.currentText()
        values = sorted(profiles)
        
        cb.clear()
        cb.addItems(values)

        if text in values:
            cb.setCurrentText(text)
        
        cb.clear()
        cb.addItems(values)

        if text in values:
            cb.setCurrentText(text)

    def setUi(self, ui:int):
        if self.__currentUi == ui:
            return

        match ui:
            case self.UI_QUANT:
                navBtn = self.__ui.btnQuantitativos
                widNew = QWidget(self)

            case self.UI_REG:
                navBtn = self.__ui.btnRegs
                widNew = QWidget(self)

            case self.UI_CARD:
                navBtn = self.__ui.btnCartoes
                widNew = QWidget(self)

            case self.UI_CONFIG:
                navBtn = self.__ui.btnConfig
                widNew = self.__configView = ConfigView(self)

            case _:
                raise ValueError('undefined UI')


        widOld = self.__ui.widContent
        self.__ui.widContent = widNew
        
        self.__currentUi = ui
        
        self.setTitle(widNew.TITLE if hasattr(widNew, 'TITLE') else '')
        navBtn.setChecked(True)
        self.__ui.mainLayout.replaceWidget(widOld, widNew)
        widOld.deleteLater()

        self.uiChanged.emit(ui)

    def on_btnNav_clicked(self):
        for btn in [self.__ui.btnSair, self.__ui.btnNav] + self.__navBtns.buttons():
            currentText = btn.text()
            newText = self.__navBtnsText[btn]

            btn.setText(newText)
            self.__navBtnsText[btn] = currentText

    def on_cbProfile_currentTextChanged(self, text:str):
        self.__ui.cbProfile.setToolTip(text)