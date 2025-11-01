from PySide6.QtWidgets import QApplication

from finances.view.page import HomePage

def homePage():
    app = QApplication()
    view = HomePage()

    view.setUserName('Iago Costa')
    view.setProfiles(['Principal', 'All'])

    view.show()
    app.exec()