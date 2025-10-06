from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from ..ui.auto.ui_LoginPage import Ui_LoginPage
from ..ui.auto.ui_LoginForm import Ui_LoginForm
from ..ui.auto.ui_CreateAccountForm import Ui_CreateAccountForm
from ..src.tools import generateStyleSheet

ui = None

def generateLoginPage(parent:QWidget=None):
    ui = Ui_LoginPage()
    wid = QWidget(parent)
    ui.setupUi(wid)

    return ui, wid

def generateLoginForm(parent:QWidget=None):
    ui = Ui_LoginForm()
    wid = QWidget(parent)
    ui.setupUi(wid)
    style = generateStyleSheet(
        inputs=['QWidget#widUser', 'QWidget#widPass'],
        highlightBtns=['QPushButton#btnAcessar'],
        linkBtns=['QPushButton#btnCriar', 'QPushButton#btnEsqueci']
    )

    wid.setStyleSheet(style)
    print(style)

    return ui, wid

def generateCreateForm(parent:QWidget=None):
    ui = Ui_CreateAccountForm()
    wid = QWidget(parent)
    ui.setupUi(wid)

    wid.setStyleSheet(generateStyleSheet(
        inputs=['QWidget#widUser', 'QWidget#widNome', 'QWidget#widEmail', 'QWidget#widPass', 'QWidget#widPassConfirm'],
        highlightBtns=['QPushButton#btnSalvar'],
        secondaryButtons=['QPushButton#btnVoltar'],
    ))

    return ui, wid

def btnVoltar_clicked():
    widOld = ui.widContent
    ui_loginForm, widNew = generateLoginForm(ui.widMain)
    ui.widContent = widNew

    ui_loginForm.btnCriar.clicked.connect(btnCriar_clicked)

    ui.mainLayout.replaceWidget(widOld, widNew)
    widOld.deleteLater()

def btnCriar_clicked():
    widOld = ui.widContent
    ui_createForm, widNew = generateCreateForm(ui.widMain)
    ui.widContent = widNew

    ui_createForm.btnVoltar.clicked.connect(btnVoltar_clicked)

    ui.mainLayout.replaceWidget(widOld, widNew)
    widOld.deleteLater()

def loginPage():
    global ui

    app = QApplication()
    win = QMainWindow()
    ui, wid = generateLoginPage()

    btnVoltar_clicked()

    win.setCentralWidget(wid)
    win.show()
    app.exec()