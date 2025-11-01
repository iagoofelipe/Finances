from PySide6.QtWidgets import QApplication, QMainWindow

from finances.view.form import CardAccountForm
from finances.core.structs import Card, Account, AccountTableItem, AccountBalance, CardLimit, CardTableItem

def cardAccountForm():
    app = QApplication()
    view = CardAccountForm()
    win = QMainWindow()

    view.setCardTableItems({
        'C0': CardTableItem(Card('C0', 'Nubank', 10, 3), CardLimit('C0', 2400, 1500.4, 899.6)),
        'C1': CardTableItem(Card('C1', 'Will', 7, 3), CardLimit('C1', 400, 120.6, 279.4)),
    })

    view.setAccountTableItems({
        'A1': AccountTableItem(Account('A1', 'Mercado Livre'), AccountBalance('A1', 1200.35, 100.35)),
        'A2': AccountTableItem(Account('A2', 'C6'), AccountBalance('A2', 0, 10)),
    })

    win.setWindowTitle(view.TITLE)
    win.setCentralWidget(view)
    win.resize(900, 400)
    win.show()
    app.exec()