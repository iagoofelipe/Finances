from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal, QDateTime

from ..src.ui.auto.ui_RegForm import Ui_RegForm
from .dialog.regTableParamsDialog import RegTableParamsDialog
from ..models.tools import isDark
from ..models.structs import Registry, RegType, NavigableData, RegTableParams
from ..models.appModel import AppModel
from ..models.consts import MAX_ITEMS_TABLE, TABLE_COLS_REG
from ..models.regModel import RegModel

class RegView(QWidget):
    previousRequired = Signal()
    nextRequired = Signal()
    paramsRequired = Signal()
    deleteRequired = Signal(list) # ids : list[int]
    editRequired = Signal()
    clearRequired = Signal()
    saveRequired = Signal(Registry)
    newRequired = Signal()
    newCategoryRequired = Signal()
    newCardRequired = Signal()
    tableSelectionChanged = Signal(set) # indexes : set[int]

    def __init__(self, appmodel:AppModel, parent:QWidget=None):
        super().__init__(parent)
        self.__model = None
        self.__appmodel = appmodel
        self.__ui = Ui_RegForm()

        self.__ui.setupUi(self)
        self.__ui.widTable.setColumnCount(len(TABLE_COLS_REG))
        self.__ui.cbCard.addItems([ c.name for c in appmodel.getCards() ])
        self.__ui.cbCat.addItems([ c.name for c in appmodel.getCategories() ])

        # Table Buttons
        self.__ui.btnParams.clicked.connect(self.paramsRequired)
        self.__ui.btnDelete.clicked.connect(self.on_btnDelete_clicked)
        self.__ui.btnAdd.clicked.connect(self.newRequired)

        # Table Buttons - Nav
        self.__ui.btnPrev.clicked.connect(self.previousRequired)
        self.__ui.btnNext.clicked.connect(self.nextRequired)

        # Details Buttons
        self.__ui.btnEdit.clicked.connect(self.editRequired)
        self.__ui.btnDeleteDetails.clicked.connect(self.on_btnDeleteDetails_clicked)
        self.__ui.btnHide.clicked.connect(self.__ui.widTable.clearSelection)
        self.__ui.btnAddCard.clicked.connect(self.newCategoryRequired)
        self.__ui.btnAddCat.clicked.connect(self.newCardRequired)
        self.__ui.btnEraseCard.clicked.connect(lambda: self.__ui.cbCard.setCurrentIndex(-1))
        self.__ui.btnEraseCat.clicked.connect(lambda: self.__ui.cbCat.setCurrentIndex(-1))
        self.__ui.btnClear.clicked.connect(self.clearRequired)
        self.__ui.btnSave.clicked.connect(self.on_btnSave_clicked)

        self.__ui.widTable.itemSelectionChanged.connect(self.on_widTable_itemSelectionChanged)

        # updating icons
        if isDark():
            self.__ui.btnParams.setIcon(QIcon(u":/root/imgs/dark-params.svg"))
            self.__ui.btnDelete.setIcon(QIcon(u":/root/imgs/dark-trash.svg"))
            self.__ui.btnDeleteDetails.setIcon(QIcon(u":/root/imgs/dark-trash.svg"))
            self.__ui.btnEdit.setIcon(QIcon(u":/root/imgs/dark-pen.svg"))
            self.__ui.btnAdd.setIcon(QIcon(u":/root/imgs/dark-plus.svg"))
            self.__ui.btnPrev.setIcon(QIcon(u":/root/imgs/dark-left-arrow.svg"))
            self.__ui.btnNext.setIcon(QIcon(u":/root/imgs/dark-right-arrow.svg"))
            self.__ui.btnAddCard.setIcon(QIcon(u":/root/imgs/dark-plus.svg"))
            self.__ui.btnAddCat.setIcon(QIcon(u":/root/imgs/dark-plus.svg"))
            self.__ui.btnHide.setIcon(QIcon(u":/root/imgs/dark-eye-slash.svg"))
            self.__ui.btnEraseCard.setIcon(QIcon(u":/root/imgs/dark-eraser.svg"))
            self.__ui.btnEraseCat.setIcon(QIcon(u":/root/imgs/dark-eraser.svg"))

        self.reset()

    #----------------------------------------------------------
    # Public Methods
    def setModel(self, model:RegModel):
        self.__model = model

    def setDetailsEditable(self, arg:bool):
        self.__ui.widDetails.show()
        self.__ui.cbType.setEnabled(arg)
        self.__ui.leTitle.setReadOnly(not arg)
        self.__ui.dsVal.setReadOnly(not arg)
        self.__ui.dtDatetime.setReadOnly(not arg)
        self.__ui.cbCard.setEnabled(arg)
        self.__ui.cbCat.setEnabled(arg)
        self.__ui.ptDesc.setReadOnly(not arg)
        self.__ui.btnEdit.setVisible(arg)
        self.__ui.widDetailBtns.setVisible(arg)
        self.__ui.btnEraseCard.setEnabled(arg)
        self.__ui.btnEraseCat.setEnabled(arg)

        self.__ui.btnEdit.setVisible(not arg)
        self.__ui.widDetailBtns.setVisible(arg)

    def setPreviousAvailable(self, arg:bool):
        self.__ui.btnPrev.setEnabled(arg)

    def setNextAvailable(self, arg:bool):
        self.__ui.btnNext.setEnabled(arg)

    def setDetailsData(self, data:Registry):
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
        self.__ui.leTitle.clear()
        self.__ui.dsVal.setValue(0)
        self.__ui.dtDatetime.setDateTime(QDateTime.currentDateTime())
        self.__ui.cbCard.setCurrentIndex(-1)
        self.__ui.cbCat.setCurrentIndex(-1)
        self.__ui.ptDesc.clear()
        self.__ui.cbType.setCurrentText('Saída')

    def reset(self):
        self.__ui.widDetails.hide()
        self.__ui.btnDelete.hide()

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

        self.__ui.widDetails.hide()

    def setDetailsVisible(self, arg:bool):
        self.__ui.widDetails.setVisible(arg)

    def setDeleteVisible(self, arg:bool):
        self.__ui.btnDelete.setVisible(arg)

    #----------------------------------------------------------
    # Events
    def on_widTable_itemSelectionChanged(self):
        self.tableSelectionChanged.emit({ i.row() for i in self.__ui.widTable.selectedItems() })

    def on_btnSave_clicked(self):
        title = self.__ui.leTitle.text()

        if not title:
            QMessageBox(QMessageBox.Icon.Warning, 'Validação de Entradas', 'O título não pode ser vazio!').exec()
            return
        
        reg = Registry(
            None,
            RegType.IN if self.__ui.cbType.currentText() == 'Entrada' else RegType.OUT,
            title,
            self.__ui.dsVal.value(),
            self.__ui.dtDatetime.dateTime(),
            self.__ui.ptDesc.toPlainText(),
            self.__appmodel.getCardByName(self.__ui.cbCard.currentText()) if self.__ui.cbCard.currentIndex() != -1 else None,
            self.__appmodel.getCategoryByName(self.__ui.cbCat.currentText()) if self.__ui.cbCat.currentIndex() != -1 else None,
        )

        self.saveRequired.emit(reg)

    def on_btnDelete_clicked(self):
        indexes = { i.row() for i in self.__ui.widTable.selectedIndexes() }

        if not self.__confirmDelete(len(indexes)):
            return

        regs = self.__model.getRegistries()
        self.deleteRequired.emit([regs[i].id for i in indexes])

    def on_btnDeleteDetails_clicked(self):
        if not self.__confirmDelete(1):
            return
        
        self.deleteRequired.emit([self.__model.getRegistry().id])

    #----------------------------------------------------------
    # Private Methods
    def __confirmDelete(self, count:int):
        msg = f'Deseja excluir {count} {'item' if count == 1 else 'itens'}? Esta ação não pode ser desfeita!'
        role = QMessageBox(QMessageBox.Icon.Question, 'Confirmação de Exclusão', msg, QMessageBox.Ok | QMessageBox.Cancel, parent=self).exec()
        return role == QMessageBox.Ok

    #----------------------------------------------------------