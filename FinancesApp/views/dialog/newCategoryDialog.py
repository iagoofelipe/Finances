from PySide6.QtWidgets import QWidget, QDialog, QFormLayout, QDialogButtonBox, QLineEdit, QMessageBox, QComboBox

from ...models.structs import Category
from ...models.consts import FONT, SPACE_BETWEEN
from ...models.tools import castToRegType

class NewCategoryDialog(QDialog):
    def __init__(self, data:Category=None, parent:QWidget=None):
        super().__init__(parent, modal=True)
        self.setWindowTitle('Nova Categoria')
        self.setFont(FONT)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(self.on_btns_accepted)
        btns.rejected.connect(self.reject)

        self.__leName = QLineEdit(self)
        self.__leDesc = QLineEdit(self)

        self.__cbType = QComboBox(self)
        self.__cbType.addItems(['Entrada', 'Saída'])

        layout = QFormLayout(self, horizontalSpacing=SPACE_BETWEEN, verticalSpacing=SPACE_BETWEEN)
        layout.addRow('Nome', self.__leName)
        layout.addRow('Tipo', self.__cbType)
        layout.addRow('Descrição', self.__leDesc)
        layout.addRow(btns)

        if data:
            self.setValues(data)

        self.adjustSize()
        self.setFixedSize(self.size())

    def getValues(self):
        return Category(None, self.__leName.text(), castToRegType(self.__cbType.currentText()), self.__leDesc.text())
    
    def setValues(self, data:Category):
        self.__leName.setText(data.name)
        self.__leDesc.setText(data.description)

    def on_btns_accepted(self):
        name = self.__leName.text()

        if not name:
            QMessageBox(QMessageBox.Icon.Warning, 'Validação de Parâmetros', 'o campo Nome é obrigatório!', parent=self).exec()
            return

        self.accept()