from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from enum import Enum, auto

from ..src.ui.auto.ui_RegForm import Ui_RegForm
from ..models.tools import isDark
from ..models.structs import Registry, RegType, NavigableData
from ..models.appModel import AppModel
from ..models.consts import MAX_ITEMS_TABLE

class RegView(QWidget):
    newRequired = Signal(Registry)
    editRequired = Signal(Registry)
    deleteRequired = Signal(tuple[str])

    class Mode(Enum):
        Delete = auto()
        Edit = auto()
        Add = auto()
        Details = auto()

    def __init__(self, model:AppModel, parent:QWidget=None):
        super().__init__(parent)
        self.__model = model
        self.__ui = Ui_RegForm()
        self.__navData = NavigableData(model.getRegistries(), MAX_ITEMS_TABLE)
        self.__cols = ['Título', 'Valor', 'Tipo', 'Data Hora', 'Cartão', 'Categoria']
        self.__numCols = len(self.__cols)

        self.__ui.setupUi(self)
        self.__ui.widDetails.hide()
        self.__ui.widTable.setColumnCount(self.__numCols)

        self.__ui.btnPrev.clicked.connect(self.on_btnPrev_clicked)
        self.__ui.btnNext.clicked.connect(self.on_btnNext_clicked)
        self.__ui.btnHide.clicked.connect(self.__ui.widTable.clearSelection)
        self.__ui.widTable.itemSelectionChanged.connect(self.on_widTable_itemSelectionChanged)
        self.__ui.btnEdit.clicked.connect(self.on_btnEdit_clicked)

        # updating icons
        if isDark():
            self.__ui.btnFilter.setIcon(QIcon(u":/root/imgs/dark-filter.svg"))
            self.__ui.btnDelete.setIcon(QIcon(u":/root/imgs/dark-trash.svg"))
            self.__ui.btnDeleteDetails.setIcon(QIcon(u":/root/imgs/dark-trash.svg"))
            self.__ui.btnEdit.setIcon(QIcon(u":/root/imgs/dark-pen.svg"))
            self.__ui.btnAdd.setIcon(QIcon(u":/root/imgs/dark-plus.svg"))
            self.__ui.btnPrev.setIcon(QIcon(u":/root/imgs/dark-left-arrow.svg"))
            self.__ui.btnNext.setIcon(QIcon(u":/root/imgs/dark-right-arrow.svg"))
            self.__ui.btnAddCard.setIcon(QIcon(u":/root/imgs/dark-plus.svg"))
            self.__ui.btnAddCat.setIcon(QIcon(u":/root/imgs/dark-plus.svg"))
            # self.__ui.btnDetails.setIcon(QIcon(u":/root/imgs/dark-eye.svg"))
            self.__ui.btnHide.setIcon(QIcon(u":/root/imgs/dark-eye-slash.svg"))

        self.__ui.cbCard.addItems([c.name for c in model.getCards()])
        self.__ui.cbCat.addItems([c.name for c in model.getCategories()])

        self.reset()

    def setMode(self, mode:Mode, data:Registry=None):
        self.__ui.widDetails.show()
        self.__editableDetails(False)

        if mode == self.Mode.Add:
            self.clearDetails()
            return
        
        if data is None:
            raise ValueError(f'data required to mode {mode}')
        
        self.__ui.leTitle.setText(data.title)
        self.__ui.dsVal.setValue(data.value)
        self.__ui.dtDatetime.setDateTime(data.datetime)
        self.__ui.ptDesc.setPlainText(data.description)

        if data.card is None:
            self.__ui.cbCard.setCurrentIndex(-1)
        else:
            self.__ui.cbCard.setCurrentText(data.card.name)
        
        if data.category is None:
            self.__ui.cbCat.setCurrentIndex(-1)
        else:
            self.__ui.cbCat.setCurrentText(data.category.name)

        if data.type == RegType.IN:
            self.__ui.rbIn.setChecked(True)
        else:
            self.__ui.rbOut.setChecked(True)

    def clearDetails(self):
        self.__ui.leTitle.clear()
        self.__ui.dsVal.clear()
        self.__ui.dtDatetime.clear()
        self.__ui.cbCard.setCurrentIndex(0)
        self.__ui.cbCat.setCurrentIndex(0)
        self.__ui.ptDesc.clear()
        self.__ui.rbOut.setChecked(True)

    def reset(self):
        self.__currentReg = None

        self.__ui.widDetails.hide()
        self.__setTableData(self.__navData.currentInterval())

    def on_model_regsChanged(self, data:tuple[Registry]):
        self.__navData.setData(data)
        self.reset()

    def on_btnPrev_clicked(self):
        self.__setTableData(self.__navData.previous())

    def on_btnNext_clicked(self):
        self.__setTableData(self.__navData.next())

    def on_widTable_itemSelectionChanged(self):
        items = self.__ui.widTable.selectedItems()

        if not len(items):
            self.__ui.widDetails.hide()
            self.__ui.btnDelete.hide()
            return
        
        self.__ui.btnDelete.show()
        self.setMode(self.Mode.Details, self.__navData.currentInterval()[self.__ui.widTable.currentRow()])

    def on_btnEdit_clicked(self):
        self.__editableDetails(True)

    def __editableDetails(self, v:bool):
        self.__ui.leTitle.setReadOnly(not v)
        self.__ui.dsVal.setReadOnly(not v)
        self.__ui.dtDatetime.setReadOnly(not v)
        self.__ui.cbCard.setEnabled(v)
        self.__ui.cbCat.setEnabled(v)
        self.__ui.ptDesc.setReadOnly(not v)
        self.__ui.rbOut.setChecked(not v)
        self.__ui.rbIn.setEnabled(v)
        self.__ui.rbOut.setEnabled(v)
        self.__ui.btnEdit.setVisible(not v)
        self.__ui.widDetailBtns.setVisible(v)

    def __setTableData(self, data:tuple[Registry]|None):
        self.__ui.lbTableNav.setText(f'{self.__navData.start} a {self.__navData.end} de {len(self.__navData)}')
        self.__ui.btnPrev.setEnabled(self.__navData.hasPrevious())
        self.__ui.btnNext.setEnabled(self.__navData.hasNext())
        self.__ui.widTable.clear()

        self.__ui.widTable.setHorizontalHeaderLabels(self.__cols)

        if data is None:
            return
        
        self.__ui.widTable.setRowCount(len(data))
        for index, reg in enumerate(data):
            self.__ui.widTable.setItem(index, 0, QTableWidgetItem(reg.title))
            self.__ui.widTable.setItem(index, 1, QTableWidgetItem(f'R$ {reg.value:.2f}'))
            self.__ui.widTable.setItem(index, 2, QTableWidgetItem('Entrada' if reg.type == RegType.IN else 'Saída'))
            self.__ui.widTable.setItem(index, 3, QTableWidgetItem(reg.datetime.toString('dd/MM/yy hh:mm')))
            self.__ui.widTable.setItem(index, 4, QTableWidgetItem(reg.card.name if reg.card else ''))
            self.__ui.widTable.setItem(index, 5, QTableWidgetItem(reg.category.name if reg.category else ''))
