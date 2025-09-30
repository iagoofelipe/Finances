from PySide6.QtCore import QObject, Signal
import socket
from threading import Thread
from time import sleep
import logging as log
import json

from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    username: str
    password: str

BUFFER_SIZE = 1024
IP = '127.0.0.1'
PORT = 8888
SEP = '!0'

CMD_AUTH = 'AUTH'
CMD_LOGOUT = 'LOGOUT'

class FinancesClient(QObject):
    authFinished = Signal(bool)
    logoutFinished = Signal()
    closed = Signal()

    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__thread = None
        self.__pref = '(Client)'
        self.__user = None

    #----------------------------------------------------------------
    #region Public Methods
    def initialize(self) -> bool:
        try:
            self.__sock.connect((IP, PORT))

        except:
            return False
        
        self.__thread = Thread(target=self.__loop)
        self.__thread.start()

        return True
    
    def isAuthenticated(self):
        return bool(self.__user)
    
    def getUser(self) -> User | None:
        return self.__user
    
    def auth(self, username:str, password:str):
        data = {
            'username': username,
            'password': password
        }

        self.sendCommand(CMD_AUTH, data)

    def logout(self):
        self.sendCommand(CMD_LOGOUT)

    def close(self):
        self.__sock.shutdown(socket.SHUT_WR)

        if self.__thread:
            self.__thread.join()

        self.__user = None
        self.__thread = None

    def sendCommand(self, cmd:str, data:dict|list=None):
        d = { 'cmd': cmd }

        if data is not None:
            d['data'] = data

        str_cmd = json.dumps(d) + SEP
        self.__sock.sendall(str_cmd.encode())

    #endregion
    #----------------------------------------------------------------
    #region Private Methods
    def __processData(self, data:str):
        """ process the dava received from server """

        try:
            json_data = json.loads(data)
            cmd = json_data['cmd']

        except:
            log.error(f'{self.__pref} unprocessable data received: "{data}"')
            return
        
        params = json_data.get('data')

        log.debug(f'{self.__pref} command received: {cmd}')

        if cmd == CMD_AUTH:
            success = params['success']
            self.__user = User(**params['user']) if success else None
            self.authFinished.emit(success)

        elif cmd == CMD_LOGOUT:
            self.__user = None
            self.logoutFinished.emit()

        else:
            log.info(f'{self.__pref} undefined command {cmd}')

    def __loop(self):
        buffer = ''

        while True:
            try:
                data = self.__sock.recv(BUFFER_SIZE)
            except:
                print('exception')
                break

            if not data:
                break

            buffer += data.decode()
            
            while SEP in buffer:
                d, buffer = buffer.split(SEP, 1)
                self.__processData(d)

        self.closed.emit()
    
    #endregion
   #----------------------------------------------------------------