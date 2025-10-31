import logging as log
import asyncio

from . import database
from .consts import IP, PORT
from .handler import FinancesClientHandler

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
        log.info(f"Servidor rodando em {addr}")

        async with server:
            await server.serve_forever()


if __name__ == '__main__':    
    server = FinancesServer()
    server.exec()
