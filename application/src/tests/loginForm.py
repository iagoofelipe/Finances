from PySide6.QtWidgets import QApplication, QWidget

from ..ui.auto.ui_LoginForm import Ui_LoginForm
from ..tools import generateStyleSheet

def loginForm():
    app = QApplication()
    wid = QWidget()
    ui = Ui_LoginForm()
    
    style = generateStyleSheet(
        inputs=['QWidget#widUser', 'QWidget#widPass'],
        highlightBtns=['QPushButton#btnAcessar'],
        linkBtns=['QPushButton#btnCriar', 'QPushButton#btnEsqueci']
    )
    
    print('stylesheet', style)
    ui.setupUi(wid)
    wid.setStyleSheet(style)
    wid.show()
    app.exec()
