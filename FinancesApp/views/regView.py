from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Signal, QDateTime
from typing import Sequence

from ..src.ui.auto.ui_RegForm import Ui_RegForm
from .dialog.newCategoryDialog import NewCategoryDialog
from .dialog.newCardDialog import NewCardDialog
from .dialog.regTableParamsDialog import RegTableParamsDialog
from ..models.tools import checkUpdateIconsNeeded, updateIcons, castToRegType
from ..models.structs import Registry, RegType, Category
from ..models.appModel import AppModel
from ..models.consts import TABLE_COLS_REG
from ..models.regModel import RegModel

class RegView(QWidget):
    previousRequired = Signal()
    nextRequired = Signal()
    deleteRequired = Signal(list) # ids : list[int]
    editRequired = Signal()
    clearRequired = Signal()
    saveRequired = Signal(Registry)
    newRequired = Signal()
    newCategoryRequired = Signal(object) # Category
    newCardRequired = Signal(object) # Card
    tableSelectionChanged = Signal(set) # indexes : set[int]

    def __init__(self, appmodel:AppModel, parent:QWidget=None):
        super().__init__(parent)
        self.__model = None
        self.__appmodel = appmodel
        self.__theme = 'light'
        self.__ui = Ui_RegForm()
        self.__reg = None
        self.__cats = {}

        self.__ui.setupUi(self)
        self.__ui.widTable.setColumnCount(len(TABLE_COLS_REG))
        self.__ui.cbCard.addItems(sorted([ c.name for c in appmodel.getCards() ]))
        self.__ui.cbCat.addItems(sorted([ c.name for c in filter(lambda x: x.type == RegType.IN, self.__cats) ]))
        self.__ui.cbType.setCurrentText('Entrada')

        # Table Buttons
        self.__ui.btnParams.clicked.connect(self.on_btnParams_clicked)
        self.__ui.btnDelete.clicked.connect(self.on_btnDelete_clicked)
        self.__ui.btnAdd.clicked.connect(self.newRequired)

        # Table Buttons - Nav
        self.__ui.btnPrev.clicked.connect(self.previousRequired)
        self.__ui.btnNext.clicked.connect(self.nextRequired)

        # Details Buttons
        self.__ui.btnEdit.clicked.connect(self.editRequired)
        self.__ui.btnDeleteDetails.clicked.connect(self.on_btnDeleteDetails_clicked)
        self.__ui.btnHide.clicked.connect(self.__ui.widTable.clearSelection)
        self.__ui.btnAddCard.clicked.connect(self.on_btnAddCard_clicked)
        self.__ui.btnAddCat.clicked.connect(self.on_btnAddCat_clicked)
        self.__ui.btnEraseCard.clicked.connect(lambda: self.__ui.cbCard.setCurrentIndex(-1))
        self.__ui.btnEraseCat.clicked.connect(lambda: self.__ui.cbCat.setCurrentIndex(-1))
        self.__ui.btnClear.clicked.connect(self.clearRequired)
        self.__ui.btnSave.clicked.connect(self.on_btnSave_clicked)

        self.__ui.widTable.itemSelectionChanged.connect(self.on_widTable_itemSelectionChanged)
        self.__ui.cbType.currentTextChanged.connect(self.on_cbType_currentTextChanged)

        # connecting external events
        appmodel.categoriesChanged.connect(self.updateCategories)
        appmodel.cardsChanged.connect(lambda cards: self.setCards([ c.name for c in cards ]))

        self.updateIcons()
        self.reset()

    #----------------------------------------------------------
    # Public Methods
    def updateIcons(self):
        if not checkUpdateIconsNeeded(self.__theme):
            return
        
        self.__theme = updateIcons(self.__ui, (
            ('btnParams', 'params'),
            ('btnDeleteDetails', 'trash'),
            ('btnAdd', 'plus'),

            ('btnClear', 'eraser'),
            ('btnSave', 'save'),
            ('btnEdit', 'pen'),
            ('btnDelete', 'trash'),
            ('btnHide', 'eye-slash'),

            ('btnAddCard', 'plus'),
            ('btnEraseCard', 'eraser'),
            ('btnAddCat', 'plus'),
            ('btnEraseCat', 'eraser'),

            ('btnPrev', 'left-arrow'),
            ('btnNext', 'right-arrow'),
        ))

    def updateCategories(self, cats:tuple[Category]=None):
        if cats is None:
            cats = self.__appmodel.getCategories()

        self.__cats[RegType.IN] = sorted([ c.name for c in filter(lambda c: c.type == RegType.IN, cats) ])
        self.__cats[RegType.OUT] = sorted([ c.name for c in filter(lambda c: c.type == RegType.OUT, cats) ])

        self.__updateCatsToCurrentType()

    def setModel(self, model:RegModel):
        self.__model = model

    def setDetailsEditable(self, arg:bool):
        self.__ui.widDetails.show()

        self.__ui.btnEdit.setVisible(not arg)
        self.__ui.btnClear.setVisible(arg)
        self.__ui.btnSave.setVisible(arg)

        self.__ui.cbType.setEnabled(arg)
        self.__ui.leTitle.setReadOnly(not arg)
        self.__ui.dsVal.setReadOnly(not arg)
        self.__ui.dtDatetime.setReadOnly(not arg)
        self.__ui.cbCard.setEnabled(arg)
        self.__ui.btnEraseCard.setEnabled(arg)
        self.__ui.cbCat.setEnabled(arg)
        self.__ui.btnEraseCat.setEnabled(arg)
        self.__ui.ptDesc.setReadOnly(not arg)

    def setPreviousAvailable(self, arg:bool):
        self.__ui.btnPrev.setEnabled(arg)

    def setNextAvailable(self, arg:bool):
        self.__ui.btnNext.setEnabled(arg)

    def setDetailsData(self, data:Registry|None):
        self.__reg = data

        if data is None:
            return

        self.__ui.leTitle.setText(data.title)
        self.__ui.dsVal.setValue(data.value)
        self.__ui.dtDatetime.setDateTime(data.datetime)
        self.__ui.ptDesc.setPlainText(data.description)
        self.__ui.cbType.setCurrentText('Entrada' if data.type == RegType.IN else 'Saída')

        if data.card is None:
            self.__ui.cbCard.setCurrentIndex(-1)
        else:
            self.__ui.cbCard.setCurrentText(data.card.name)
        
        if data.category is None:
            self.__ui.cbCat.setCurrentIndex(-1)
        else:
            self.__ui.cbCat.setCurrentText(data.category.name)

    def clearDetails(self):
        self.__reg = None
        self.__ui.leTitle.clear()
        self.__ui.dsVal.setValue(0)
        self.__ui.dtDatetime.setDateTime(QDateTime.currentDateTime())
        self.__ui.cbCard.setCurrentIndex(-1)
        self.__ui.cbCat.setCurrentIndex(-1)
        self.__ui.ptDesc.clear()
        self.__ui.cbType.setCurrentText('Saída')

    def reset(self):
        self.__reg = None
        self.__ui.widDetails.hide()
        self.__ui.btnDelete.hide()
        self.updateCategories()

    def setTableLabel(self, start:int, end:int, total:int):
        self.__ui.lbTableNav.setText(f'{start} a {end} de {total}')

    def setTableData(self, data:tuple[Registry]):
        self.__ui.widTable.clear()
        self.__ui.widTable.setHorizontalHeaderLabels(TABLE_COLS_REG)

        if data is None: return

        self.__ui.widTable.setRowCount(len(data))
        for index, reg in enumerate(data):
            self.__ui.widTable.setItem(index, 0, QTableWidgetItem(reg.title))
            self.__ui.widTable.setItem(index, 1, QTableWidgetItem(f'R$ {reg.value:.2f}'))
            self.__ui.widTable.setItem(index, 2, QTableWidgetItem('Entrada' if reg.type == RegType.IN else 'Saída'))
            self.__ui.widTable.setItem(index, 3, QTableWidgetItem(reg.datetime.toString('dd/MM/yy hh:mm')))
            self.__ui.widTable.setItem(index, 4, QTableWidgetItem(reg.card.name if reg.card else ''))
            self.__ui.widTable.setItem(index, 5, QTableWidgetItem(reg.category.name if reg.category else ''))
            self.__ui.widTable.setItem(index, 6, QTableWidgetItem(reg.description))

        self.__ui.widDetails.hide()

    def setDetailsVisible(self, arg:bool):
        self.__ui.widDetails.setVisible(arg)

    def setDeleteVisible(self, arg:bool):
        self.__ui.btnDelete.setVisible(arg)

    def getNotEdittedData(self) -> Registry | None:
        return self.__reg
    
    def getCurrentData(self) -> Registry:
        regType = castToRegType(self.__ui.cbType.currentText())

        return Registry(
            self.__reg.id if self.__reg else None,
            regType,
            self.__ui.leTitle.text(),
            self.__ui.dsVal.value(),
            self.__ui.dtDatetime.dateTime(),
            self.__ui.ptDesc.toPlainText(),
            self.__appmodel.getCardByName(self.__ui.cbCard.currentText()) if self.__ui.cbCard.currentIndex() != -1 else None,
            self.__appmodel.getCategoryByName(self.__ui.cbCat.currentText(), regType) if self.__ui.cbCat.currentIndex() != -1 else None,
        )

    def setCards(self, arg:Sequence[str]):
        wid = self.__ui.cbCard

        text = wid.currentText()
        wid.clear()
        wid.addItems(sorted(arg))

        if text:
            wid.setCurrentText(text)
        else:
            wid.setCurrentIndex(-1)

    #----------------------------------------------------------
    # Events
    def on_btnParams_clicked(self):
        view = RegTableParamsDialog(self.__model.getTableParams(), self)

        if RegTableParamsDialog.Accepted == view.exec():
            self.__model.setTableParams(view.getValues())

    def on_widTable_itemSelectionChanged(self):
        self.tableSelectionChanged.emit({ i.row() for i in self.__ui.widTable.selectedItems() })

    def on_btnSave_clicked(self):
        title = self.__ui.leTitle.text()

        if not title:
            QMessageBox(QMessageBox.Icon.Warning, 'Validação de Entradas', 'O título não pode ser vazio!').exec()
            return
        
        self.saveRequired.emit(self.getCurrentData())

    def on_btnDelete_clicked(self):
        indexes = { i.row() for i in self.__ui.widTable.selectedIndexes() }

        if not self.__confirmDelete(len(indexes)):
            return

        regs = self.__model.getRegistries()
        self.deleteRequired.emit([regs[i].id for i in indexes])

    def on_btnDeleteDetails_clicked(self):
        if not self.__confirmDelete(1):
            return
        
        self.deleteRequired.emit([self.__reg.id])

    def on_btnAddCard_clicked(self):
        view = NewCardDialog(parent=self)

        if view.exec() == NewCardDialog.Accepted:
            self.newCardRequired.emit(view.getValues())

    def on_btnAddCat_clicked(self):
        view = NewCategoryDialog(parent=self)

        if view.exec() == NewCategoryDialog.Accepted:
            self.newCategoryRequired.emit(view.getValues())

    def on_cbType_currentTextChanged(self, text:str):
        self.__updateCatsToCurrentType()

    #----------------------------------------------------------
    # Private Methods
    def __confirmDelete(self, count:int):
        msg = f'Deseja excluir {count} {'item' if count == 1 else 'itens'}? Esta ação não pode ser desfeita!'
        role = QMessageBox(QMessageBox.Icon.Question, 'Confirmação de Exclusão', msg, QMessageBox.Ok | QMessageBox.Cancel, parent=self).exec()
        return role == QMessageBox.Ok
    
    def __updateCatsToCurrentType(self):
        typeReg = castToRegType(self.__ui.cbType.currentText())

        self.__ui.cbCat.clear()
        self.__ui.cbCat.addItems(self.__cats[typeReg])
        
        if self.__reg and self.__reg.type == typeReg:
            self.__ui.cbCat.setCurrentText(self.__reg.category.name)
        
        else:
            self.__ui.cbCat.setCurrentIndex(-1)

    #----------------------------------------------------------