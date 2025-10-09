from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Signal
from enum import Enum
from typing import Iterable, Any

from ...src.ui.auto.ui_TableForm import Ui_TableForm
from ...models.tableData import NavigableTableData
from ...src.consts import TABLE_MAX_LEN

class TableWidget(QWidget):
    NoFlags = 0
    BtnAdd = 2
    BtnEdit = 4
    BtnDelete = 8
    BtnAccept = 16
    BtnReject = 32
    BtnParams = 64
    BtnDetails = 128
    ShowNavAsNeeded = 256

    addRequired = Signal()
    editRequired = Signal()
    deleteRequired = Signal()
    acceptRequired = Signal()
    rejectRequired = Signal()
    paramsRequired = Signal()
    detailsRequired = Signal()

    def __init__(self, columns:Iterable[str], title:str='', flags:int=0, maxLen=TABLE_MAX_LEN, parent:QWidget=None):
        super().__init__(parent)
        self.__showNavAsNeeded = False
        self.__ui = Ui_TableForm()
        self.__nav = NavigableTableData(maxLen)
        
        self.__ui.setupUi(self)
        self.setFlags(flags)
        self.setTitle(title)
        
        table = self.__ui.tableWid
        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)

        self.__ui.btnAdd.clicked.connect(self.addRequired)
        self.__ui.btnEdit.clicked.connect(self.editRequired)
        self.__ui.btnDelete.clicked.connect(self.deleteRequired)
        self.__ui.btnAccept.clicked.connect(self.acceptRequired)
        self.__ui.btnReject.clicked.connect(self.rejectRequired)
        self.__ui.btnParams.clicked.connect(self.paramsRequired)
        self.__ui.btnDetails.clicked.connect(self.detailsRequired)
        self.__ui.btnPrev.clicked.connect(self.on_btnPrev_clicked)
        self.__ui.btnNext.clicked.connect(self.on_btnNext_clicked)
        
        self.__updateNav()

    def setTitle(self, title:str):
        self.__ui.lbTitle.setText(title)

    def setFlags(self, flags:int):
        self.__ui.btnAdd.setVisible(flags & self.BtnAdd)
        self.__ui.btnEdit.setVisible(flags & self.BtnEdit)
        self.__ui.btnDelete.setVisible(flags & self.BtnDelete)
        self.__ui.btnAccept.setVisible(flags & self.BtnAccept)
        self.__ui.btnReject.setVisible(flags & self.BtnReject)
        self.__ui.btnParams.setVisible(flags & self.BtnParams)
        self.__ui.btnDetails.setVisible(flags & self.BtnDetails)
        self.__showNavAsNeeded = flags & self.ShowNavAsNeeded

    def setData(self, data:Iterable[Any]):
        self.__nav.setData(data)
        self.updateValues()

    def updateValues(self):
        table = self.__ui.tableWid
        table.clearContents()
        data = self.__nav.currentInterval()
        self.__updateNav()

        if data is None: return

        table.setRowCount(len(data))
        for rowIndex, rowData in enumerate(data):
            for colIndex, d in enumerate(rowData):
                table.setItem(rowIndex, colIndex, QTableWidgetItem(str(d)))

    def on_btnPrev_clicked(self):
        self.__ui.btnPrev.setEnabled(self.__nav.hasPrevious())
        self.__ui.btnNext.setEnabled(self.__nav.hasNext())
        self.__nav.previous()
        self.updateValues()

    def on_btnNext_clicked(self):
        self.__ui.btnPrev.setEnabled(self.__nav.hasPrevious())
        self.__ui.btnNext.setEnabled(self.__nav.hasNext())
        self.__nav.next()
        self.updateValues()

    def __updateNav(self):
        hasPrev = self.__nav.hasPrevious()
        hasNext = self.__nav.hasNext()

        self.__ui.btnPrev.setEnabled(hasPrev)
        self.__ui.btnNext.setEnabled(hasNext)

        if not hasPrev and not hasNext and self.__showNavAsNeeded:
            self.__ui.widNav.hide()
            return

        self.__ui.widNav.show()
        start, end, total = self.__nav.start, self.__nav.end, self.__nav.total
        self.__ui.lbNav.setText(f'{start} a {end} de {total} {'items' if total > 0 else 'item'}')