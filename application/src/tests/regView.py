from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QDate

from ...views.regView import RegView
from ..structs import Account, Card, Registry
from ..consts import REG_OP_CREDIT

def regView():
    app = QApplication()
    wid = RegView()

    wid.setCategories({ 'Alimentação', 'Transporte', 'Alongamento' })
    wid.setAccounts({ 'A1': Account('A1', 'Mercado Pago'), 'A2': Account('A2', 'Nubank') })
    wid.setCards({ 'C1': Card('C1', 'Nubank', 10, 2500) })
    wid.setValues(Registry('R1', 'Lanche', False, 7.5, QDate(2025, 10, 29), 'Alimentação', REG_OP_CREDIT, '', cardId='C1'))

    wid.show()
    app.exec()