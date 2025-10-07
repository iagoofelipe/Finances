from PySide6.QtCore import QObject, Signal
from threading import Thread
import logging as log

from . import serverClient as server
from ..src import structs
from ..src.tools import dataclassToDict
from ..src.consts import *
from .config import Configuration

class AppModel(QObject):
    initializationFinished = Signal(bool)
    authenticationFinished = Signal(bool)
    createUserFinished = Signal(bool)
    logoutFinished = Signal()
    __instance = None

    def __init__(self):
        super().__init__()
        self.__user = None
        self.__server = server.ServerClient(self)
        self.__loginData = None
        self.__config = Configuration()

        self.__server.connectionError.connect(self.on_server_connectionError)
        self.__server.connectionClosed.connect(self.on_server_connectionClosed)
        self.__server.commandReceived.connect(self.on_server_commandReceived)

    @staticmethod
    def instance() -> 'AppModel':
        return __class__.__instance
    
    @property
    def credentials(self):
        return self.__loginData
    
    def initialize(self):

        def func():
            success = self.__server.connect()
            log.debug(f'[AppModel] initialization {success=}')

            username = self.__config.get('credentials', 'username')
            password = self.__config.get('credentials', 'password')

            if username and password:
                log.debug(f'[AppModel] local credentials found')
                self.__loginData = structs.LoginData(username, password, True)

            self.initializationFinished.emit(success)

        Thread(target=func).start()

    def close(self):
        self.__server.close()

    def authenticate(self, data:structs.LoginData):
        log.debug(f'[AppModel] authenticate username={data.username}')
        self.__loginData = data

        self.__server.sendCommand(CMD_AUTH, {
            'username': data.username,
            'password': data.password
        })

    def logout(self):
        self.__loginData = None
        self.__user = None
        self.clearSavedCredentials()
        self.__server.sendCommand(CMD_LOGOUT)
    
    def createUser(self, data:structs.User):
        log.debug(f'[AppModel] create user {data}')
        self.__server.sendCommand(CMD_CREATE_USER, dataclassToDict(data))

    def getUser(self) -> structs.User | None:
        return self.__user

    def on_server_connectionError(self):
        log.info('[AppModel] connection error with the server')

    def on_server_connectionClosed(self):
        log.info('[AppModel] connection closed with the server')

    def on_server_commandReceived(self, cmd:str, params:list|dict|None):
        log.debug(f'[AppModel] command received from server {cmd=} {params=}')

        if cmd == CMD_AUTH:
            success = params['success']

            if not success:
                self.clearSavedCredentials()

            self.__user = structs.User(**params['user']) if success else None
            self.authenticationFinished.emit(success)

        elif cmd == CMD_CREATE_USER:
            self.createUserFinished.emit(params['success'])

        elif cmd == CMD_LOGOUT:
            self.logoutFinished.emit()

    def clearSavedCredentials(self):
        self.__config.removeOptions(('credentials', 'username'), ('credentials', 'password'))

    def saveCredentials(self, data:structs.LoginData=None):
        if data:
            self.__loginData = data
        
        if not self.__loginData:
            return
        
        self.__config.parser['credentials']['username'] = self.__loginData.username
        self.__config.parser['credentials']['password'] = self.__loginData.password
        self.__config.updateFile()
        

AppModel._AppModel__instance = AppModel()