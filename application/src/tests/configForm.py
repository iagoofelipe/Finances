from PySide6.QtWidgets import QApplication

from ...views.configView import ConfigView

def configForm():
    app = QApplication()
    view = ConfigView()

    view.show()
    app.exec()