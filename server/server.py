import logging as log
import asyncio
import json
from dataclasses import fields

from . import database

BUFFER_SIZE = 1024
IP = '127.0.0.1'
PORT = 8888
SEP = '<CMD_END>'

CMD_AUTH = 'AUTH'
CMD_LOGOUT = 'LOGOUT'
CMD_CREATE_USER = 'CREATE_USER'
CMD_CREATE_PROFILE = 'CREATE_PROFILE'

def dataclassToDict(obj:database.AbstractTable) -> dict:
    return { field.name : getattr(obj, field.name) for field in fields(obj) }

class FinancesClientHandler:
    def __init__(self, db:database.FinancesDatabase, id:int, reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
        self.__db = db
        self.__id = id
        self.__reader = reader
        self.__writer = writer
        self.__user = None
        self.__pref = f'(Client {self.__id})'

    #----------------------------------------------------------------
    #region Public Methods
    async def auth(self, username:str, password:str):
        self.__user = self.__db.auth(username, password)
        success = bool(self.__user)
        name = self.__user.name if success else None
        dict_user = dataclassToDict(self.__user) if success else None

        log.info(f'{self.__pref} user authenticated {success} {name=}')

        await self.sendCommand(CMD_AUTH, { 'success': success, 'user': dict_user })

    async def createUser(self, **params):
        log.info(f'{self.__pref} create user required with {params=}')
        success = bool(self.__db.createUser(**params))
        log.info(f'{self.__pref} create user result {success=}')
        
        await self.sendCommand(CMD_CREATE_USER, { 'success': success })

    async def logout(self):
        self.__user = None
        log.debug(f'{self.__pref} user logout')
        await self.sendCommand(CMD_LOGOUT)

    async def run(self):
        log.info(f'{self.__pref} new connection received')
        buffer = ''

        try:
            while True:
                data = await self.__reader.read(BUFFER_SIZE)

                if not data:
                    break

                message = data.decode()
                buffer += message

                while SEP in buffer:
                    fullData, buffer = buffer.split(SEP, 1)
                    await self.__processData(fullData)

            log.info(f'{self.__pref} closing connection...')
            self.__writer.close()
            await self.__writer.wait_closed()

        except Exception as e:
            log.error(f'{self.__pref} connection error: {e}')

        log.info(f'{self.__pref} connection closed')

    async def sendCommand(self, cmd:str, data:dict|list=None):
        d = { 'cmd': cmd }

        if data is not None:
            d['data'] = data

        str_cmd = json.dumps(d)
        log.debug(f"{self.__pref} sending '{str_cmd}'")
        str_cmd += SEP

        self.__writer.write(str_cmd.encode())
        await self.__writer.drain()

    #endregion
    #----------------------------------------------------------------
    #region Private Methods
    async def __processData(self, data:str):
        """ process the dava received from client """

        try:
            json_data = json.loads(data)
            cmd = json_data['cmd']

        except:
            log.error(f'{self.__pref} unprocessable data received: "{data}"')
            return
        
        params = json_data.get('data')

        log.debug(f'{self.__pref} command received: {cmd}')

        if cmd == CMD_AUTH:
            await self.auth(**params)

        elif cmd == CMD_LOGOUT:
            await self.logout()

        elif cmd == CMD_CREATE_USER:
            await self.createUser(**params)

        else:
            log.info(f'{self.__pref} undefined command {cmd}')

    #endregion
    #----------------------------------------------------------------

class FinancesServer:
    def __init__(self):
        log.basicConfig(level=log.DEBUG)

        self.__clients = {}
        self.__db = database.FinancesDatabase()

    def exec(self):
        self.__db.initialize()
        
        try:
            asyncio.run(self.__main())
        except KeyboardInterrupt:
            pass

    async def __handleClient(self, reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
        ip, id = writer.get_extra_info('peername')
        self.__clients[id] = client = FinancesClientHandler(self.__db, id, reader, writer)

        await client.run()

    async def __main(self):
        server = await asyncio.start_server(
            self.__handleClient, IP, PORT
        )

        addr = server.sockets[0].getsockname()
        print(f"Servidor rodando em {addr}")

        async with server:
            await server.serve_forever()


if __name__ == '__main__':    
    server = FinancesServer()
    server.exec()