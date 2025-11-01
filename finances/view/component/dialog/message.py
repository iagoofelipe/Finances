from PySide6.QtWidgets import QWidget, QLabel

from finances.view.component.dialog.dialog import Dialog

class MessageDialog(Dialog):
    def __init__(self, title:str, content:str, width:int=None, parent:QWidget=None):
        super().__init__(title, self.Button.Continue | self.Button.Cancel | self.Style.HideTitle | self.Style.LeftSpace, width=width, parent=parent)
        lb = QLabel(content, self.getParent())
        lb.setFont(self.getFont())
        lb.setWordWrap(True)
        self.setWidget(lb)