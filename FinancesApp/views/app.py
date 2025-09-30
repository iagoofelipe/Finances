from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCoreApplication
import logging as log
from threading import Thread

from ..models.appModel import AppModel
from .appView import AppView
from ..controllers.appController import AppController
from ..models.server import FinancesClient

class FinancesApp(QApplication):
    def __init__(self):
        super().__init__()
        self.__model = AppModel()
        self.__view = AppView(self.__model)
        self.__control = AppController(self.__model, self.__view)

    def exec(self) -> int:
        self.__control.initialize()
        return super().exec()
    
class FinancesAppConsole(QCoreApplication):
    def __init__(self):
        super().__init__()
        log.basicConfig(level=log.DEBUG)

        self.__server = FinancesClient(self)
        self.__server.closed.connect(self.on_server_closed)
        self.__server.authFinished.connect(self.on_server_authFinished)
        self.__server.logoutFinished.connect(self.on_server_logoutFinished)

    def on_server_closed(self):
        print('server connection closed')
        self.quit()

    def on_server_authFinished(self, success:bool):
        print(f'authentication finished {success=}')

    def on_server_logoutFinished(self):
        print('user logout')

    def exec(self):
        if not self.__server.initialize():
            print('it was not possible to connect with the server')
            return

        Thread(target=self.__menu).start()
        return super().exec()
    
    def __menu(self):
        while True:
            print(
                '-' * 50,
                'FinancesAppConsole Menu',
                '\t1. Authentication',
                '\t2. User',
                '\t3. Logout',
                '',
                '\t0. Quit',
                '',
                sep='\n'
            )

            op = input('Option: ')
            print('-' * 50)

            match op:
                case '1': self.__menuAuth()
                case '2': self.__menuUser()
                case '3': self.__server.logout()

                case '0':
                    self.__server.close()
                    break

                case _: print('Invalid option!')


    def __menuAuth(self):
        connected = self.__server.isAuthenticated()
        print(f'AuthenticationStatus: {'Authenticated' if connected else 'AuthenticationRequired'}')

        if connected: return

        username = input('Username: ')
        password = input('Password: ')

        self.__server.auth(username, password)

    def __menuUser(self):
        if self.__server.isAuthenticated():
            print(f'User: {self.__server.getUser().name}')
        else:
            print('AuthenticationRequired')
