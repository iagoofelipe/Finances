from PySide6.QtWidgets import QWidget, QButtonGroup
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal

from ..src.ui.auto.ui_MainPage import Ui_MainPage
from .regView import RegView
from .configView import ConfigView
from ..src.tools import isDarkTheme, generateStyleSheet
from ..src.consts import STYLE_PROPERTIES_LIGHT, STYLE_PROPERTIES_DARK

class MainPageView(QWidget):
    logoutRequired = Signal()
    uiChanged = Signal(int)
    currentProfileChanged = Signal(object) # profileId: str | None

    UI_QUANT = 0
    UI_REG = 1
    UI_CARD = 2
    UI_CONFIG = 3

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_MainPage()
        self.__currentUi = None
        self.__profileIdByIndex = []
        self.__theme = 'light'

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

        self.setStyleSheet(generateStyleSheet(
            title=['QLabel#lbMainTitle'],
        ))

        self.updateTheme()
        self.__updateNavStyle()
        

    def updateTheme(self):
        isdark = isDarkTheme()
        
        # if is up to date
        if (isdark and self.__theme == 'dark') or (not isdark and self.__theme == 'light'):
            return
        
        prefix = 'dark_' if isdark else 'light_'
        self.__ui.btnNotificacoes.setIcon(QIcon(f":/root/icons/{prefix}bell.svg"))
        self.__ui.btnNav.setIcon(QIcon(f":/root/icons/{prefix}bars-solid-full.svg"))
        self.__ui.btnQuantitativos.setIcon(QIcon(f":/root/icons/{prefix}pie-chart.svg"))
        self.__ui.btnRegs.setIcon(QIcon(f":/root/icons/{prefix}list.svg"))
        self.__ui.btnCartoes.setIcon(QIcon(f":/root/icons/{prefix}credit-card.svg"))
        self.__ui.btnConfig.setIcon(QIcon(f":/root/icons/{prefix}settings.svg"))
        self.__ui.btnSair.setIcon(QIcon(f":/root/icons/{prefix}log-out.svg"))
        self.__updateNavStyle()

    def getConfigView(self):
        return self.__configView if self.isCurrentView(self.UI_CONFIG) else None
    
    def getRegView(self):
        return self.__regView if self.isCurrentView(self.UI_REG) else None

    def getCurrentProfileId(self) -> str | None:
        index = self.__ui.cbProfile.currentIndex()
        return self.__profileIdByIndex[index] if index != -1 else None

    def isCurrentView(self, ui:int):
        return self.__currentUi == ui

    def setUserName(self, name:str):
        self.__ui.lbTextUser.setText(f'Olá, {name}!')

    def setTitle(self, text:str):
        self.__ui.lbMainTitle.setText(text)

    def setWaitMode(self, arg:bool):
        self.setDisabled(arg)

    def setProfiles(self, profiles:dict[str, str]):
        cb = self.__ui.cbProfile
        text = cb.currentText()
        values = sorted(profiles.values())
        self.__profileIdByIndex = list(profiles)
        
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
                widNew = self.__regView = RegView(self)

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
        self.currentProfileChanged.emit(self.getCurrentProfileId())

    def __updateNavStyle(self):
        self.__ui.frameNav.setStyleSheet(
            """
            QWidget {
                color: %(COLOR_SUBTITLE)s;
            }

            QPushButton {
                border: none;
                padding: 10;
                border-radius: 10;
                border-top-left-radius: 0;
                border-bottom-left-radius: 0;
            }
                
            QPushButton::hover, QPushButton:checked {
                border-left:4px solid %(BG_HIGHLIGHT)s;
                background-color: %(BG_NAV_BUTTON)s;
            }
                
            /* botões para não aplicar cores */
            QPushButton#btnSair::hover, QPushButton#btnNav::hover {
                background-color: transparent;
                border: none;
            }
            """ % (STYLE_PROPERTIES_DARK if isDarkTheme() else STYLE_PROPERTIES_LIGHT)
        )