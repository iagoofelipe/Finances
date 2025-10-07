from sqlite3 import connect
from uuid import uuid4
from cryptography.fernet import Fernet
import os
import logging as log
from dataclasses import dataclass, fields
import datetime as dt
from typing import TypeVar, Iterable

FILE_DB = 'database.db'
FILE_DB_CREATE = 'server/src/create.sql'

_T = TypeVar('_T')

@dataclass
class AbstractTable:
    __table__ = None
    __encryptedFields__ = None

@dataclass
class User(AbstractTable):
    id: str
    name: str
    email: str
    username: str
    password: str
    __table__ = 'user'
    __encryptedFields__ = ['password']

# @dataclass
# class Category(AbstractTable):
#     id: str
#     name: str
#     type: int
#     description: str = ''
#     userId: str = None
#     __table__ = 'category'

# @dataclass
# class Card(AbstractTable):
#     id: str
#     name: str
#     userId: str = None
#     __table__ = 'card'

# @dataclass
# class Third(AbstractTable):
#     id: str
#     name: str
#     userId: str = None
#     __table__ = 'third'

# @dataclass
# class Registry(AbstractTable):
#     id: str
#     type: int
#     title: str
#     value: float
#     datetime: dt.datetime
#     description: str = ''
#     userId: str = None
#     cardId: str | None = None
#     categoryId: str | None = None
#     thirdId: str | None = None
#     __table__ = 'registry'

class FinancesDatabase:
    __classFields = {}

    def __init__(self):
        self.__exists = os.path.exists(FILE_DB)

    def initialize(self):
        self.__conn = conn = connect(FILE_DB)
        self.__cursor = cursor = self.__conn.cursor()

        if not self.__exists:
            with open(FILE_DB_CREATE, encoding='utf-8') as f:
                script = f.read()
                cursor.executescript(script)

            key = Fernet.generate_key()

            cursor.execute("INSERT INTO system (key, value) VALUES ('crypto', ?)", (key.decode(), ))
            conn.commit()

        else:
            cursor.execute("SELECT value FROM system WHERE key='crypto'")
            key = cursor.fetchone()[0]

        self.__crypto = Fernet(key)
    
    @staticmethod
    def tableClassFields(classType:AbstractTable) -> list[str]:
        cls = __class__.__classFields
        
        if classType not in cls:
            cls[classType] = [ x.name for x in fields(classType) ]
        
        return cls[classType]
    
    @staticmethod
    def tableClassHasField(classType:AbstractTable, field:str) -> bool:
        return field in __class__.tableClassFields(classType)

    def auth(self, username:str, password:str) -> User | None:
        user = self.get(User, True, username=username)

        if not user:
            return

        # checking password
        if user.password != password:
            return
        
        return user

    def createUser(self, **params) -> User | None:
        if self.getCount(User, username=params['username']) or self.getCount(User, email=params['email']):
            log.debug('[Database] users found with the same username or email')
            return

        log.debug('[Database] no users found with the same username or email')
        return self.create(User, **params)
    
    def getCount(self, classType:AbstractTable, **params) -> int:
        """ return the number of matches from the table by params """

        sql = f'SELECT COUNT(*) FROM `{classType.__table__}`'

        if params:
            places, args = self.__getPlaceWithArgs(params)
            sql += ' WHERE ' + places
            self.__cursor.execute(sql, args)

        else:
            self.__cursor.execute(sql)

        return self.__cursor.fetchone()[0]

    def create(self, classType:_T, **params) -> _T | None:
        """ insert a new value from a dataclass object. The dataclass must exist in the database, with the same fields """

        # generating id
        if self.tableClassHasField(classType, 'id'):
            params['id'] = id = str(uuid4())

        # encrypting fields
        log.debug(f'[Database] new {classType} with {params=}')
        if classType.__encryptedFields__:
            for field in filter(lambda x: x in params, classType.__encryptedFields__):
                params[field] = self.__crypto.encrypt(params[field].encode()).decode()
            
        places = self.__getPlace(params)
        keys = ','.join(params)
        args = tuple(params.values())
        sql = f'INSERT INTO `{classType.__table__}` ({keys}) VALUES ({places})'
        
        self.__cursor.execute(sql, args)
        self.__conn.commit()

        return self.get(classType, True, id=id)

    def get(self, classType:_T, returnsOne=False, **params) -> _T | tuple[_T] | None:
        sql = f'SELECT * FROM `{classType.__table__}`'
        
        if params:
            places, args = self.__getPlaceWithArgs(params)
            sql += ' WHERE ' + places
        else:
            args = []

        self.__cursor.execute(sql, args)

        if returnsOne:
            r = self.__cursor.fetchone()
            return self.__decryptFields(classType(*r)) if r else None
        
        return tuple([ self.__decryptFields(classType(*tuple(r))) for r in self.__cursor.fetchall() ])

    def update(self, classType:AbstractTable, pk, pkField='id', data=None, **params) -> bool:
        if not params and data is None:
            return False
        
        isdataclass = bool(data)
        places, args = self.__getPlaceWithArgs(data if isdataclass else params, isdataclass)

        self.__cursor.execute(f"UPDATE `{classType.__table__}` SET {places} WHERE `{pkField}`='{pk}'", args)
        self.__conn.commit()

        return True

    def __decryptFields(self, obj):
        if obj.__encryptedFields__:
            for field in obj.__encryptedFields__:
                decrypted = self.__crypto.decrypt(getattr(obj, field)).decode()
                setattr(obj, field, decrypted)

        return obj

    def __getPlace(self, data:Iterable|AbstractTable, dataclass=False):
        """ ?,?, ... ,? """
        return ','.join(['?' for _ in (self.tableClassFields(type(data)) if dataclass else data)])

    def __getPlaceWithArgs(self, data:dict|AbstractTable, dataclass=False):
        """ returns ('?,?, ... ,?', [arg1, arg2, ..., argN]) """

        if dataclass:
            dataFields = self.tableClassFields(type(data))
            places = ['?' for _ in dataFields]
            args = [ getattr(data, field) for field in dataFields ]

        else:
            places = []
            args = []

            for k, v in data.items():
                places.append(f'`{k}`=?')
                args.append(v)

        return ','.join(places), args
    

if __name__ == '__main__':    
    db = FinancesDatabase()
    db.initialize()

    user = 'iago'
    password = '1234'

    if not db.auth(user, password):
        if not db.createUser('Iago Carvalho', user, password):
            print('it was not possible to create a new user with these credentials')
            exit()

        if not db.auth(user, password):
            print('user not connected')
            exit()

        # db.create(Card, name='Nubank')
        # db.create(Card, name='Santander')

    print(f'Welcome, {db.getUser().name}!')
    print('Users', *db.get(User), sep='\n\t')