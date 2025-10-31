from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from .components.dialog import MessageDialog
from ..src.ui.auto.ui_CardAccountForm import Ui_CardAccountForm
from ..src.tools import isDarkTheme, generateStyleSheet
from ..src.structs import Card, Account, CardTableItem, AccountTableItem
from .components.table import TableWidget

class CardAccountView(QWidget):
    TITLE = 'cartões e contas'

    saveCardRequired = Signal(Card)
    saveAccountRequired = Signal(Account)
    updateCardRequired = Signal(Card)
    updateAccountRequired = Signal(Account)
    deleteCardRequired = Signal(str) # id
    deleteAccountRequired = Signal(str) # id
    
    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.__ui = Ui_CardAccountForm()
        self.__theme = 'light'
        self.__unsavedCard = False
        self.__unsavedAccount = False
        self.__card = None
        self.__account = None
        self.__cards = {}
        self.__accounts = {}

        self.__ui.setupUi(self)
        self.setStyleSheet(generateStyleSheet(
            inputs=['QWidget#widNomeCartao', 'QWidget#widNomeConta'],
            abstractSpin=['QWidget#widVencimento', 'QWidget#widLimite', 'QWidget#widInicial'],
            highlightBtns=['QPushButton#btnSalvarCartao', 'QPushButton#btnSalvarConta'],
            secondaryButtons=['QPushButton#btnLimparCartao', 'QPushButton#btnLimparConta'],
            title=['QLabel#lbNovoCartao', 'QLabel#lbNovaConta'],
        ))

        t = TableWidget
        flags = t.Button.Delete | t.Button.Add | t.Button.Edit | t.Behavior.DeleteJustOne | t.Behavior.SelectJustOne | t.Style.ShowNavAsNeeded
        self.__tableCards = TableWidget(['Nome', 'Limite Total', 'Limite Disponível', 'Limite Utilizado', 'Vencimento', 'Fechamento'], 'Cartões', flags, parent=self)
        self.__tableAccounts = TableWidget(['Nome', 'Saldo', 'Previsto'], 'Contas', flags, parent=self)

        self.__ui.gridLayout.replaceWidget(self.__ui.frameCartoes, self.__tableCards)
        self.__ui.gridLayout.replaceWidget(self.__ui.frameContas, self.__tableAccounts)
        self.__ui.frameCartoes.deleteLater()
        self.__ui.frameContas.deleteLater()

        cardUnsavedTrue = lambda: self.setCardAsUnsaved(True)
        accountUnsavedTrue = lambda: self.setAccountAsUnsaved(True)

        self.__ui.btnSalvarCartao.clicked.connect(self.on_btnSalvarCartao_clicked)
        self.__ui.btnSalvarConta.clicked.connect(self.on_btnSalvarConta_clicked)
        self.__ui.btnLimparCartao.clicked.connect(self.on_btnLimparCartao_clicked)
        self.__ui.btnLimparConta.clicked.connect(self.on_btnLimparConta_clicked)
        self.__tableCards.addRequired.connect(self.on_tableCards_addRequired)
        self.__tableCards.deleteRequired.connect(self.on_tableCards_deleteRequired)
        self.__tableCards.editRequired.connect(self.on_tableCards_editRequired)
        self.__tableAccounts.addRequired.connect(self.on_tableAccounts_addRequired)
        self.__tableAccounts.deleteRequired.connect(self.on_tableAccounts_deleteRequired)
        self.__tableAccounts.editRequired.connect(self.on_tableAccounts_editRequired)
        self.__ui.leNomeCartao.textChanged.connect(cardUnsavedTrue)
        self.__ui.sbVencimento.valueChanged.connect(cardUnsavedTrue)
        self.__ui.sbLimite.valueChanged.connect(cardUnsavedTrue)
        self.__ui.leNomeConta.textChanged.connect(accountUnsavedTrue)
        self.__ui.sbInicial.valueChanged.connect(accountUnsavedTrue)

        self.clear()

    def clear(self):
        self.on_btnLimparCartao_clicked()
        self.on_btnLimparConta_clicked()

    #--------------------------------------------------------------------
    #region Cards
    def getTableCards(self): return self.__tableCards
    
    def setCardTableItems(self, d:dict[str, CardTableItem]):
        # set an iter with de columns ['Nome', 'Limite Total', 'Limite Disponível', 'Vencimento', 'Fechamento']
        self.__cards = d
        self.__tableCards.setData({ k: (v.card.name, v.limit.total, v.limit.available, v.limit.used, v.card.dueDay, v.card.closingDay) for k, v in d.items() })
    
    def setCardTableItem(self, c:CardTableItem | None):
        self.__card = c
        self.__ui.leNomeCartao.setText(c.card.name if c else '')
        self.__ui.sbVencimento.setValue(c.card.dueDay if c and c.card.dueDay and 1 <= c.card.dueDay <= 31 else 1)
        self.__ui.sbLimite.setValue(c.limit.total if c and c.limit.total else 0)
        self.setCardAsUnsaved(False)

    def setCardAsUnsaved(self, v:bool):
        if v == self.__unsavedCard: return
        self.__unsavedCard = v
        self.__ui.lbNovoCartao.setText('Novo Cartão' + ('*' if v else ''))
    
    def on_btnLimparCartao_clicked(self):
        self.setCardTableItem(self.__card)

    def on_btnSalvarCartao_clicked(self): ...

    def on_tableCards_addRequired(self):
        if not self.cardFormAvailableToUse(): return
        self.setCardTableItem(None)

    def on_tableCards_deleteRequired(self): ...

    def on_tableCards_editRequired(self):
        if not self.cardFormAvailableToUse(): return
        cardId = self.__tableCards.getSelectedKeys()[0]
        self.setCardTableItem(self.__cards[cardId])

    def cardFormAvailableToUse(self):
        """ check if it has unsaved data and, if it does, ask for the user's permition """

        if self.__unsavedCard:
            if not MessageDialog('Possível perda de dados', 'O campo Cartão possui dados não salvos, deseja continuar?').exec():
                return False
        return True

    #endregion
    #--------------------------------------------------------------------
    #region Accounts
    def getTableAccounts(self): return self.__tableAccounts
    
    def setAccountTableItems(self, d:dict[str, AccountTableItem]):
        # set an iter with de columns ['Nome', 'Saldo', 'Previsto']]
        self.__accounts = d
        self.__tableAccounts.setData({ k: (v.account.name, v.balance.currentValue, v.balance.expected) for k, v in d.items() })
    
    def setAccountTableItem(self, a:AccountTableItem | None):
        self.__account = a
        self.__ui.leNomeConta.setText(a.account.name if a else '')
        self.__ui.sbInicial.setValue(a.balance.currentValue if a and a.balance.currentValue else 0)
        # self.__ui.sbPrevisto.setValue(a.balance.expected if a and a.balance.expected else 0)
        self.setAccountAsUnsaved(False)

    def setAccountAsUnsaved(self, v:bool):
        if v == self.__unsavedAccount: return
        self.__unsavedAccount = v
        self.__ui.lbNovaConta.setText('Nova Conta' + ('*' if v else ''))

    def on_btnLimparConta_clicked(self):
        self.setAccountTableItem(self.__account)

    def on_btnSalvarConta_clicked(self): ...

    def on_tableAccounts_addRequired(self):
        if not self.accountFormAvailableToUse(): return
        self.setAccountTableItem(None)

    def on_tableAccounts_deleteRequired(self): ...

    def on_tableAccounts_editRequired(self):
        if not self.accountFormAvailableToUse(): return
        accountId = self.__tableAccounts.getSelectedKeys()[0]
        self.setAccountTableItem(self.__accounts[accountId])

    def accountFormAvailableToUse(self):
        """ check if it has unsaved data and, if it does, ask for the user's permition """

        if self.__unsavedAccount:
            if not MessageDialog('Possível perda de dados', 'O campo Conta possui dados não salvos, deseja continuar?').exec():
                return False
        return True

    #endregion
    #--------------------------------------------------------------------