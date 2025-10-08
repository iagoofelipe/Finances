from PySide6.QtWidgets import QApplication

from ...views.mainPageView import MainPageView

def mainPage():
    app = QApplication()
    view = MainPageView()

    view.setUserName('Iago Costa')
    view.setProfiles(['Principal', 'All'])

    view.show()
    app.exec()