from PySide6.QtCore import QObject, Signal
import socket, json
from threading import Thread
import logging as log

BUFFER_SIZE = 1024
IP = '127.0.0.1'
PORT = 8888
SEP = '<CMD_END>'

class ServerClient(QObject):
    connectionError = Signal()
    connectionClosed = Signal()
    commandReceived = Signal(str, object)

    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connected = False

    def connect(self) -> bool:
        try:
            self.__sock.connect((IP, PORT))
            self.__connected = True

        except:
            self.__connected = False
            return False
        
        Thread(target=self.__loop).start()

        return True
    
    def sendCommand(self, cmd:str, data:dict|list=None):
        log.debug(f'[ServerClient] sending {cmd=} {data=}')
        d = { 'cmd': cmd }

        if data is not None:
            d['data'] = data

        str_cmd = json.dumps(d) + SEP
        self.__sock.sendall(str_cmd.encode())

    def close(self):
        if self.__connected:
            self.__sock.shutdown(socket.SHUT_WR)

    def __loop(self):
        buffer = ''

        while True:
            try:
                data = self.__sock.recv(BUFFER_SIZE)

            except:
                self.connectionError.emit()
                break

            if not data:
                break

            buffer += data.decode()
            
            while SEP in buffer:
                d, buffer = buffer.split(SEP, 1)

                try:
                    json_data = json.loads(d)
                    cmd = json_data['cmd']

                except:
                    log.error(f'[ServerClient] unprocessable data received: "{d}"')
                    continue
                
                self.commandReceived.emit(cmd, json_data.get('data'))


        self.connectionClosed.emit()