from PySide6.QtWidgets import QApplication, QWidget

from ..ui.auto.ui_CreateAccountForm import Ui_CreateAccountForm
from ..src.tools import generateStyleSheet

def crerateAccountForm():
    app = QApplication()
    wid = QWidget()
    ui = Ui_CreateAccountForm()
    
    style = generateStyleSheet(
        inputs=['QWidget#widUser', 'QWidget#widNome', 'QWidget#widEmail', 'QWidget#widPass', 'QWidget#widPassConfirm'],
        highlightBtns=['QPushButton#btnSalvar'],
        secondaryButtons=['QPushButton#btnVoltar'],
    )
    
    print('stylesheet', style)

    ui.setupUi(wid)
    wid.setStyleSheet(style)
    wid.show()
    app.exec()
