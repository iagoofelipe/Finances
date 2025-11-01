from PySide6.QtWidgets import QWidget, QMessageBox

from finances.view.component.dialog import Dialog
from finances.core.tools import generateInputForm

class NewProfileDialog(Dialog):
    def __init__(self, parent:QWidget=None):
        super().__init__('Novo Perfil', self.Button.Save | self.Button.Cancel, width=400, parent=parent)
        widName, self.__leName, _ = generateInputForm('Nome', self.getParent(), self.getFont())
        self.setWidget(widName)

    def isValid(self):
        return bool(self.__leName.text())
    
    def alertNotValid(self):
        QMessageBox(QMessageBox.Warning, 'Validação de Parâmetros', 'O campo Nome não pode ser vazio!', parent=self.getParent()).exec()
    
    def getValues(self) -> str:
        return self.__leName.text()