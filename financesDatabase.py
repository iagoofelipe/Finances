from sqlite3 import connect
from uuid import uuid4
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass, fields
import datetime as dt
from typing import TypeVar

FILE_DB = 'database.db'
FILE_DB_CREATE = 'server/create.sql'

_T = TypeVar('_T')

@dataclass
class AbstractTable:
    __table__ = None
    __encryptedFields__ = None

@dataclass
class User(AbstractTable):
    id: str
    name: str
    username: str
    password: str
    __table__ = 'user'
    __encryptedFields__ = ['password']

@dataclass
class Category(AbstractTable):
    id: str
    name: str
    type: int
    description: str = ''
    userId: str = None
    __table__ = 'category'

@dataclass
class Card(AbstractTable):
    id: str
    name: str
    userId: str = None
    __table__ = 'card'

@dataclass
class Third(AbstractTable):
    id: str
    name: str
    userId: str = None
    __table__ = 'third'

@dataclass
class Registry(AbstractTable):
    id: str
    type: int
    title: str
    value: float
    datetime: dt.datetime
    description: str = ''
    userId: str = None
    cardId: str | None = None
    categoryId: str | None = None
    thirdId: str | None = None
    __table__ = 'registry'

class FinancesDatabase:
    def __init__(self):
        self.__exists = os.path.exists(FILE_DB)
        self.__user = None

    def initialize(self):
        self.__conn = conn = connect(FILE_DB)
        self.__cursor = cursor = self.__conn.cursor()

        if not self.__exists:
            with open('server/create.sql', encoding='utf-8') as f:
                script = f.read()
                cursor.executescript(script)

            key = Fernet.generate_key()

            cursor.execute("INSERT INTO system (key, value) VALUES ('crypto', ?)", (key.decode(), ))
            conn.commit()

        else:
            cursor.execute("SELECT value FROM system WHERE key='crypto'")
            key = cursor.fetchone()[0]

        self.__crypto = Fernet(key)
    
    def auth(self, username:str, password:str) -> bool:
        self.__user = self.get(User, True, username=username)

        if not self.__user:
            return False

        # checking password
        if self.__user.password != password:
            self.__user = None
            return False
        
        return True

    def createUser(self, name:str, username:str, password:str) -> User | None:
        # if already exists
        self.__cursor.execute('SELECT id FROM user WHERE username=?', (username, ))
        if self.__cursor.fetchone():
            return

        return self.create(User, name=name, username=username, password=password)
    
    def getUser(self) -> User | None:
        return self.__user

    def create(self, classType:_T, **params) -> _T | None:
        """ insert a new value from a dataclass object. The dataclass must exist in the database, with the same fields """

        _fields = [ x.name for x in fields(classType) ]

        if 'userId' in _fields:
            if not self.__user:
                return
            
            params['userId'] = self.__user.id

        # generating id
        if 'id' in _fields:
            params['id'] = id = str(uuid4())

        # encrypting fields
        if classType.__encryptedFields__:
            for field in filter(lambda x: x in params, classType.__encryptedFields__):
                params[field] = self.__crypto.encrypt(params[field]).decode()
            
        places = self.__getPlace(params)
        keys = ','.join(params)
        args = tuple(params.values())
        sql = f'INSERT INTO `{classType.__table__}` ({keys}) VALUES ({places})'
        
        self.__cursor.execute(sql, args)
        self.__conn.commit()

        return self.get(classType, True, id=id)

    def get(self, classType:_T, returnsOne=False, **params) -> _T | tuple[_T] | None:
        places, args = self.__getPlaceWithArgs(params)
        sql = f'SELECT * FROM `{classType.__table__}`'
        
        if params:
            sql += ' WHERE ' + places

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

    def __getPlace(self, data, dataclass=False):
        return ','.join(['?' for _ in (fields(data) if dataclass else data)])

    def __getPlaceWithArgs(self, data, dataclass=False):
        if dataclass:
            dataFields = [ x.name for x in fields(data) ]
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

        db.create(Card, name='Nubank')
        db.create(Card, name='Mercado Pago')

    print('user connected')
    print('Users', db.get(User))
    # print('update', db.update(User, db.getUser().id, name='Iago Carvalho'))
    # print('Users', db.get(User))

    # id1 = 'f516613e-c1a6-4e8c-8001-1bccd87d6b3e'
    # id2 = 'aaaaaaa'
    # print(db.get(Card, userId=id1))                     # [<Card id=...>, ...]
    # print(db.get(Card, returnsOne=True, userId=id1))    # <Card id=...>
    # print(db.get(Card, userId=id2))                     # ()
    # print(db.get(Card, returnsOne=True, userId=id2))    # None
    # print(db.get(Card))                                 # [<Card id=...>, ...]
    # print(db.get(Card, returnsOne=True))                # <Card id=...>
    # print(db.get(User, username='iago'))                # <User>