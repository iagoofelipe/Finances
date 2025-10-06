from PySide6.QtCore import QObject, Signal
from threading import Thread
from time import sleep

class AppModel(QObject):
    initializationFinished = Signal(bool)

    def __init__(self):
        super().__init__()
    
    def initialize(self):

        def func():
            sleep(2)
            self.initializationFinished.emit(True)

        Thread(target=func).start()