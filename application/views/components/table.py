from PySide6.QtWidgets import QWidget, QTableWidgetItem, QFrame
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from typing import Iterable, Any

from ...src.ui.auto.ui_TableForm import Ui_TableForm
from ...models.tableData import NavigableTableData
from ...src.consts import TABLE_MAX_LEN
from ...src.tools import isDarkTheme, generateStyleSheet

class TableWidget(QWidget):

    class Button:
        NoFlags = 0
        Add = 2
        Edit = 4
        Delete = 8
        Accept = 16
        Reject = 32
        Params = 64
        Details = 128
    
    class Style:
        ShowNavAsNeeded = 256
        InsideNoFrame = 512
    
    class Behavior:
        DeleteJustOne = 1024
        SelectJustOne = 2048

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
        self.__theme = 'light'
        
        self.__ui.setupUi(self)
        self.setFlags(flags)
        self.setTitle(title)
        
        table = self.__ui.tableWid
        table.setColumnCount(len(columns) + 1)
        table.setHorizontalHeaderLabels(['Key'] + list(columns))
        table.hideColumn(0)

        if flags & self.Behavior.SelectJustOne:
            table.setSelectionMode(table.SelectionMode.SingleSelection)

        self.__ui.btnAdd.clicked.connect(self.addRequired)
        self.__ui.btnEdit.clicked.connect(self.editRequired)
        self.__ui.btnDelete.clicked.connect(self.deleteRequired)
        self.__ui.btnAccept.clicked.connect(self.acceptRequired)
        self.__ui.btnReject.clicked.connect(self.rejectRequired)
        self.__ui.btnParams.clicked.connect(self.paramsRequired)
        self.__ui.btnDetails.clicked.connect(self.detailsRequired)
        self.__ui.btnPrev.clicked.connect(self.on_btnPrev_clicked)
        self.__ui.btnNext.clicked.connect(self.on_btnNext_clicked)
        table.itemSelectionChanged.connect(self.on_itemSelectionChanged)
        
        self.setStyleSheet(generateStyleSheet(
            title=['QLabel#lbTitle', 'QLabel#lbNav'],
        ))

        self.__updateNav()
        self.updateTheme()

    def setTitle(self, title:str):
        self.__ui.lbTitle.setText(title)

    def updateTheme(self):
        isdark = isDarkTheme()
        
        # if is up to date
        if (isdark and self.__theme == 'dark') or (not isdark and self.__theme == 'light'):
            return
        
        prefix = 'dark_' if isdark else 'light_'
        self.__ui.btnReject.setIcon(QIcon(f':/root/icons/{prefix}x.svg'))
        self.__ui.btnAccept.setIcon(QIcon(f":/root/icons/{prefix}check.svg"))
        self.__ui.btnDelete.setIcon(QIcon(f":/root/icons/{prefix}trash.svg"))
        self.__ui.btnDetails.setIcon(QIcon(f":/root/icons/{prefix}detail.svg"))
        self.__ui.btnAdd.setIcon(QIcon(f":/root/icons/{prefix}plus.svg"))
        self.__ui.btnParams.setIcon(QIcon(f":/root/icons/{prefix}sliders.svg"))
        self.__ui.btnEdit.setIcon(QIcon(f":/root/icons/{prefix}edit.svg"))

    def setFlags(self, flags:int):
        self.__flags = flags

        # Buttons
        self.__ui.btnAdd.setVisible(flags & self.Button.Add)
        self.__ui.btnEdit.setVisible(flags & self.Button.Edit)
        self.__ui.btnDelete.setVisible(flags & self.Button.Delete)
        self.__ui.btnAccept.setVisible(flags & self.Button.Accept)
        self.__ui.btnReject.setVisible(flags & self.Button.Reject)
        self.__ui.btnParams.setVisible(flags & self.Button.Params)
        self.__ui.btnDetails.setVisible(flags & self.Button.Details)
        
        # Style
        self.__showNavAsNeeded = flags & self.Style.ShowNavAsNeeded
        
        if flags & self.Style.InsideNoFrame:
            shape = QFrame.Shape.NoFrame
            margins = 0, 0, 0, 0
        else:
            shape = QFrame.Shape.StyledPanel
            margins = 5, 5, 5, 5

        self.__ui.frameTableLayout.setContentsMargins(*margins)
        self.__ui.frameTable.setFrameShape(shape)

        self.on_itemSelectionChanged()

    def setData(self, data:dict[str, Iterable]):
        self.__nav.setData(data)
        self.updateValues()

    def getData(self): return self.__nav.getData()

    def getSelectedKeys(self) -> list[str]:
        return [self.__ui.tableWid.item(row, 0).text() for row in { item.row() for item in self.__ui.tableWid.selectedItems() }]

    def updateValues(self):
        table = self.__ui.tableWid
        table.clearContents()
        data = self.__nav.currentInterval()
        self.__updateNav()

        if data is None: return

        count = len(data)
        table.setRowCount(count)

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

    def on_itemSelectionChanged(self):
        numRows = len({ item.row() for item in self.__ui.tableWid.selectedItems() })

        if numRows == 0:
            if self.__flags & self.Button.Reject: self.__ui.btnReject.hide()
            if self.__flags & self.Button.Accept: self.__ui.btnAccept.hide()
            if self.__flags & self.Button.Delete: self.__ui.btnDelete.hide()
            if self.__flags & self.Button.Details: self.__ui.btnDetails.hide()
            # if self.__flags & self.Button.Add: Always visible
            # if self.__flags & self.Button.Params: Always visible
            if self.__flags & self.Button.Edit: self.__ui.btnEdit.hide()

        elif numRows == 1:
            if self.__flags & self.Button.Reject: self.__ui.btnReject.show()
            if self.__flags & self.Button.Accept: self.__ui.btnAccept.show()
            if self.__flags & self.Button.Delete: self.__ui.btnDelete.show()
            if self.__flags & self.Button.Details: self.__ui.btnDetails.show()
            # if self.__flags & self.Button.Add: Always visible
            # if self.__flags & self.Button.Params: Always visible
            if self.__flags & self.Button.Edit: self.__ui.btnEdit.show()

        else: # > 1
            if self.__flags & self.Button.Reject: self.__ui.btnReject.hide()
            if self.__flags & self.Button.Accept: self.__ui.btnAccept.hide()
            if self.__flags & self.Button.Delete: self.__ui.btnDelete.setVisible(not self.__flags & self.Behavior.DeleteJustOne)
            if self.__flags & self.Button.Details: self.__ui.btnDetails.hide()
            # if self.__flags & self.Button.Add: Always visible
            # if self.__flags & self.Button.Params: Always visible
            if self.__flags & self.Button.Edit: self.__ui.btnEdit.hide()
