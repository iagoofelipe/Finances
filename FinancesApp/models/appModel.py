from PySide6.QtCore import QObject, Signal

class AppModel(QObject):
    initializationFinished = Signal(bool, str)

    def __init__(self):
        super().__init__()

    def initialize(self):
        self.initializationFinished.emit(True, '')