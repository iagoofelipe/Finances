from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate

from finances.view.component.table import TableWidget
from finances.ui.auto.ui_RegForm import Ui_RegForm
from finances.core.tools import generateStyleSheet, generateComboBox, generateSpinBox
from finances.core.consts import *
from finances.core.structs import Registry, Account, Card

class RegistryForm(QWidget):
    TITLE = 'registros'


    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        
        # GUI
        self.__ui = Ui_RegForm()
        self.__cbAccount = None
        self.__cbDestinyAccount = None
        self.__cbCard = None
        self.__sbInstallments = None
        self.__widOp1 = None
        self.__widOp2 = None
        columns = ['Título', 'Valor', 'Data', 'Operação', 'Contabilizado', 'Categoria']
        flags = TableWidget.Button.Delete | TableWidget.Button.Details | TableWidget.Button.Add | TableWidget.Button.Params | TableWidget.Button.Edit | TableWidget.Style.ShowNavAsNeeded
        self.__tableHistoric = TableWidget(columns, 'Histórico', flags, parent=self)

        # Control
        self.__currentOperation = None
        self.__opsWithAccount = (REG_OP_BETWEEN_ACCOUNTS, REG_OP_INVOICE_PAYMENT, REG_OP_IN, REG_OP_OUT)
        self.__opsWithCard = (REG_OP_INVOICE_PAYMENT, REG_OP_CREDIT)
        self.__opsWithDestinyAccount = (REG_OP_BETWEEN_ACCOUNTS, )
        self.__reg = None

        self.__accountNames = []
        self.__accountIds = []
        self.__cardNames = []
        self.__cardIds = []
        
        self.__ui.setupUi(self)
        self.__ui.mainLayout.replaceWidget(self.__ui.frameHistorico, self.__tableHistoric)
        self.__ui.cbOperacao.addItems(REG_OPERATION_IDS_BY_NAME)
        self.__ui.frameHistorico.deleteLater()
        
        self.setStyleSheet(generateStyleSheet(
            inputs=['QWidget#widTitulo', 'QWidget#widDesc'],
            highlightBtns=['QPushButton#btnSalvar'],
            secondaryButtons=['QPushButton#btnLimpar'],
            combobox=['QWidget#widContab', 'QWidget#widCat', 'QWidget#widOperacao'],
            abstractSpin=['QWidget#widVal', 'QWidget#widData'],
            title=['QLabel#lbTitleReg', 'QLabel#lbTitleOp'],
        ))

        # events
        self.__ui.cbOperacao.currentTextChanged.connect(lambda text: self.setOperationById(REG_OPERATION_IDS_BY_NAME[text]))
        self.__ui.btnLimpar.clicked.connect(self.backValuesToLastSet)

        self.clear()

    def clear(self):
        self.setOperationById(REG_OP_CREDIT)
        self.setTitle('')
        self.setPending(True)
        self.setRegistryValue(0)
        self.setDate(QDate.currentDate())
        self.setCategory('')
        self.setDescription('')

    def backValuesToLastSet(self):
        if self.__reg:
            self.setValues(self.__reg)
        else:
            self.clear()

    def setCategories(self, items:set[str]):
        val = self.__ui.cbCat.currentText()
        self.__ui.cbCat.clear()
        self.__ui.cbCat.addItems(items)
        self.__ui.cbCat.setCurrentText(val)

    def setAccounts(self, data:dict[str, Account]):
        self.__accountIds = list(data)
        self.__accountNames = [x.name for x in data.values()]

        if self.__currentOperation in self.__opsWithAccount:
            self.__cbAccount.clear()
            self.__cbAccount.addItems(self.__accountNames)

    def setCards(self, data:dict[str, Card]):
        self.__cardIds = list(data)
        self.__cardNames = [x.name for x in data.values()]

        if self.__currentOperation in self.__opsWithCard:
            self.__cbCard.clear()
            self.__cbCard.addItems(self.__cardNames)

    def setOperationByName(self, arg:str): self.setOperationById(REG_OPERATION_IDS_BY_NAME[arg])

    def setOperationById(self, operation:int):
        widNew1 = None
        widNew2 = None
        
        if operation == REG_OP_BETWEEN_ACCOUNTS:
            widNew1, self.__cbAccount, _ = generateComboBox('Conta Origem', self.__ui.widRegInputs)
            widNew2, self.__cbDestinyAccount, _ = generateComboBox('Conta Destino', self.__ui.widRegInputs)

            self.__cbDestinyAccount.addItems(self.__accountNames)

        elif operation == REG_OP_INVOICE_PAYMENT:
            widNew1, self.__cbAccount, _ = generateComboBox('Conta', self.__ui.widRegInputs)
            widNew2, self.__cbCard, _ = generateComboBox('Cartão', self.__ui.widRegInputs)
            
        elif operation == REG_OP_CREDIT:
            widNew1, self.__cbCard, _ = generateComboBox('Cartão', self.__ui.widRegInputs)
            widNew2, self.__sbInstallments, _ = generateSpinBox('Número de Parcelas', self.__ui.widRegInputs, minimum=1)

        elif operation in (REG_OP_IN, REG_OP_OUT):
            widNew1, self.__cbAccount, _ = generateComboBox('Conta', self.__ui.widRegInputs)

        else: raise ValueError('invalid operation')

        if self.__widOp1: self.__widOp1.deleteLater()
        if self.__widOp2: self.__widOp2.deleteLater()
        if widNew1: self.__ui.gridLayout.addWidget(widNew1, 3, 1)
        if widNew2: self.__ui.gridLayout.addWidget(widNew2, 3, 2)

        self.__widOp1 = widNew1
        self.__widOp2 = widNew2
        self.__currentOperation = operation

        # setting data
        self.__ui.cbOperacao.setCurrentText(REG_OPERATION_NAMES_BY_ID[operation])
        self.setTitle('')
        self.setPending(True)
        self.setRegistryValue(0)
        self.setDate(QDate.currentDate())
        self.setCategory('')
        self.setDescription('')

        if operation in self.__opsWithAccount:
            self.__cbAccount.addItems(self.__accountNames)

        if operation in self.__opsWithCard:
            self.__cbCard.addItems(self.__cardNames)

    def getTitle(self): return self.__ui.leTitulo.text()
    def getPending(self): return self.__ui.cbContab.currentText() == 'Pendente'
    def getDescription(self): return self.__ui.leDesc.text()
    def getRegistryValue(self): return self.__ui.dsVal.value()
    def getDate(self): return self.__ui.dtData.date()
    def getCategory(self): return self.__ui.cbCat.currentText()
    def getOperationId(self): return self.__currentOperation
    def getOperationName(self): return REG_OPERATION_NAMES_BY_ID[self.__currentOperation]
    def getAccountId(self): return self.__accountIds[self.__cbAccount.currentIndex()] if self.__currentOperation in self.__opsWithAccount else None
    def getDestinyAccountId(self): return self.__accountIds[self.__cbDestinyAccount.currentIndex()] if self.__currentOperation in self.__opsWithDestinyAccount else None
    def getCardId(self): return self.__cardIds[self.__cbCard.currentIndex()] if self.__currentOperation in self.__opsWithCard else None
    def getInstallments(self): return self.__sbInstallments.value() if self.__currentOperation == REG_OP_CREDIT else None

    def setTitle(self, arg:str): self.__ui.leTitulo.setText(arg)
    def setPending(self, arg:bool): self.__ui.cbContab.setCurrentText('Pendente' if arg else 'Contabilizado')
    def setDescription(self, arg:str): self.__ui.leDesc.setText(arg)
    def setRegistryValue(self, arg:int): self.__ui.dsVal.setValue(arg)
    def setDate(self, arg:QDate): self.__ui.dtData.setDate(arg)
    def setCategory(self, arg:str): self.__ui.cbCat.setCurrentText(arg)
    
    def setAccountId(self, arg:str):
        if self.__currentOperation not in self.__opsWithAccount:
            raise ValueError('the current mode has no account')
        
        self.__cbAccount.setCurrentIndex(self.__accountIds.index(arg))
    
    def setDestinyAccountId(self, arg:str):
        if self.__currentOperation not in self.__opsWithDestinyAccount:
            raise ValueError('the current mode has no destiny account')
        
        self.__cbDestinyAccount.setCurrentIndex(self.__accountIds.index(arg))
    
    def setCardId(self, arg:str):
        if self.__currentOperation not in self.__opsWithCard:
            raise ValueError('the current mode has no card')
        
        self.__cbCard.setCurrentIndex(self.__cardIds.index(arg))
    
    def setInstallments(self, arg:int):
        if self.__currentOperation != REG_OP_CREDIT:
            raise ValueError('the current mode has no installments')
        
        self.__sbInstallments.setValue(arg)

    def getValues(self):
        return Registry(
            None,
            self.getTitle(),
            self.getPending(),
            self.getRegistryValue(),
            self.getDate(),
            self.getCategory(),
            self.getOperationId(),
            self.getDescription(),
            self.getAccountId(),
            self.getDestinyAccountId(),
            self.getCardId(),
            self.getInstallments()
        )
    
    def setValues(self, reg:Registry):
        self.__reg = reg

        self.setOperationById(reg.operation)
        self.setTitle(reg.title)
        self.setPending(reg.pending)
        self.setRegistryValue(reg.value)
        self.setDate(reg.date)
        self.setCategory(reg.category)
        self.setDescription(reg.description)
        if reg.accountId is not None: self.setAccountId(reg.accountId)
        if reg.destinyAccountId is not None: self.setDestinyAccountId(reg.destinyAccountId)
        if reg.cardId is not None: self.setCardId(reg.cardId)
        if reg.installments is not None: self.setInstallments(reg.installments)