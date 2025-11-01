from PySide6.QtWidgets import QApplication

from finances.view.form import ConfigForm

def configForm():
    app = QApplication()
    view = ConfigForm()

    view.show()
    app.exec()