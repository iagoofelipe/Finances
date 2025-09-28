from PySide6.QtWidgets import QWidget, QDialog, QFormLayout, QDialogButtonBox, QLineEdit, QMessageBox

from ...models.structs import Card
from ...models.consts import FONT, SPACE_BETWEEN

class NewCardDialog(QDialog):
    def __init__(self, data:Card=None, parent:QWidget=None):
        super().__init__(parent, modal=True)
        self.setWindowTitle('Novo Cartão')
        self.setFont(FONT)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(self.on_btns_accepted)
        btns.rejected.connect(self.reject)

        self.__leName = QLineEdit(self)

        layout = QFormLayout(self, horizontalSpacing=SPACE_BETWEEN, verticalSpacing=SPACE_BETWEEN)
        layout.addRow('Nome', self.__leName)
        layout.addRow(btns)

        if data:
            self.setValues(data)

        self.adjustSize()
        self.setFixedSize(self.size())

    def getValues(self):
        return Card(None, self.__leName.text())
    
    def setValues(self, data:Card):
        self.__leName.setText(data.name)

    def on_btns_accepted(self):
        name = self.__leName.text()

        if not name:
            QMessageBox(QMessageBox.Icon.Warning, 'Validação de Parâmetros', 'o campo Nome é obrigatório!', parent=self).exec()
            return

        self.accept()