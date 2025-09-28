from PySide6.QtCore import QObject, Signal, QDateTime
from threading import Thread
from configparser import ConfigParser
from cryptography.fernet import Fernet
import os
import logging as log
from uuid import uuid4
from typing import Iterable
import json

from .consts import FILE_TMP
from .structs import Card, Category, Registry, RegType
from .tools import hasAll, castToRegType

class AppModel(QObject):
    initializationFinished = Signal(bool, str)
    authFinished = Signal(bool)
    regsChanged = Signal(tuple)
    cardsChanged = Signal(tuple)
    categoriesChanged = Signal(tuple)

    def __init__(self):
        super().__init__()
        log.basicConfig(level=log.DEBUG)

        
        self.useTestData() # temporary data
        self.__updateStructs()
    
    #----------------------------------------------------------
    #region Public Methods
    def initialize(self):
        def func():
            self.__config = ConfigParser()
            crypto = None
            if os.path.exists(FILE_TMP):
                self.__config.read(FILE_TMP)

                try:
                    crypto = Fernet(self.__config['crypto']['key'])
                except:
                    crypto = None
            
            if not self.__config.has_section('crypto'):
                self.__config.add_section('crypto')
                
            if not self.__config.has_section('credentials'):
                self.__config.add_section('credentials')

            if crypto is None:
                key = Fernet.generate_key()
                crypto = Fernet(key)

                self.__config['crypto']['key'] = key.decode()

                with open(FILE_TMP, 'w') as f:
                    self.__config.write(f)

            self.__crypto = crypto

            self.initializationFinished.emit(True, '')
        
        Thread(target=func).start()

    def getSavedCredentials(self) -> tuple[str, str] | None:
        log.debug('[AppModel::getSavedCredentials] getting credentials...')
        try:
            user = self.__crypto.decrypt(self.__config['credentials']['user']).decode()
            password = self.__crypto.decrypt(self.__config['credentials']['password']).decode()
            log.debug(f'[AppModel::getSavedCredentials] {user=} {password=}')

            return user, password

        except:
            log.debug('[AppModel::getSavedCredentials] could not be extracted')
            return
        
    def rememberCredentials(self) -> bool:
        valid = self.__config.has_option('credentials', 'remember') and self.__config.has_option('credentials', 'user') and self.__config.has_option('credentials', 'password')
        remember = valid and self.__config['credentials']['remember'] == 'True'

        log.debug(f'[AppModel::rememberCredentials] {remember=}')
        return remember

    def clearCredentials(self):
        if not self.rememberCredentials():
            return
        
        if self.__config.has_option('credentials', 'user'):
            self.__config['credentials'].pop('user')

        if self.__config.has_option('credentials', 'password'):
            self.__config['credentials'].pop('password')

        self.__config['credentials']['remember'] = 'False'

        with open(FILE_TMP, 'w') as f:
            self.__config.write(f)

    def auth(self, user:str, password:str, remember:bool):
        def func():
            success = user == 'iago' and password == '1234'
            log.debug(f'[AppModel::auth] {user=} {password=} {success=}')
            
            if success:
                if remember:
                    self.__config['credentials']['user'] = self.__crypto.encrypt(user.encode()).decode()
                    self.__config['credentials']['password'] = self.__crypto.encrypt(password.encode()).decode()
                    self.__config['credentials']['remember'] = 'True'

                else:
                    if self.__config.has_option('credentials', 'user'):
                        self.__config['credentials'].pop('user')

                    if self.__config.has_option('credentials', 'password'):
                        self.__config['credentials'].pop('password')

                    self.__config['credentials']['remember'] = 'False'

                with open(FILE_TMP, 'w') as f:
                    self.__config.write(f)

            self.authFinished.emit(success)

        Thread(target=func).start()

    def useTestData(self):
        file = 'FinancesApp/src/tests/data.json'
        
        if not os.path.exists(file):
            log.info('[AppModel] data file not available, using data set instead')
            self.__generateTestData()
            return
        
        with open(file, encoding='utf-8') as f:
            data = json.load(f)

        self.__categories = { c['id'] : Category(type=castToRegType(c.pop("type")), **c) for c in data['categories'] }
        self.__cards = { c['id'] : Card(**c) for c in data['cards'] }
        self.__regs = {}

        for r in data['registries']:
            card = self.__cards.get(r.pop("cardId"))
            category = self.__categories.get(r.pop("categoryId"))
            datetime = QDateTime.fromString(r.pop("datetime"), "yyyy-MM-dd hh:mm:ss")

            self.__regs[r['id']] = Registry(card=card, category=category, datetime=datetime, type=castToRegType(r.pop("type")), **r)

    #region Registry

    def newRegistry(self, reg:Registry) -> bool:
        if not reg.title or reg.value <= 0:
            return False
        
        reg.id = str(uuid4())
        self.__regs[reg.id] = reg
        self.__updateStructRegs()

        return True
    
    def updateRegistry(self, reg:Registry) -> bool:
        if reg.id not in self.__regs:
            return False
        
        self.__regs[reg.id] = reg
        self.__updateStructRegs()

        return True
    
    def deleteRegistry(self, id:str) -> bool:
        if id not in self.__regs:
            return False
        
        self.__regs.pop(id)
        self.__updateStructRegs()

        return True

    def deleteRegistries(self, ids:Iterable[str]) -> bool:
        if not hasAll(ids, self.__regs):
            return False
        
        for _id in ids: self.__regs.pop(_id)
        self.__updateStructRegs()

        return True

    def getRegistryById(self, id:str) -> Registry | None:
        return self.__regs.get(id)

    def getRegistries(self) -> tuple[Registry]:
        return self.__tupleRegs
    
    #endregion
    
    #region Card

    def newCard(self, card:Card) -> bool:
        if not card.name:
            return False
        
        card.id = str(uuid4())
        self.__cards[card.id] = card
        self.__updateStructCards()

        return True

    def updateCard(self, card:Card) -> bool:
        if card.id not in self.__cards:
            return False
    
        self.__cards[card.id] = card
        self.__updateStructCards()
        
        return True

    def deleteCard(self, id:str) -> bool:
        if id not in self.__cards:
            return False
        
        self.__cards.pop(id)
        self.__updateStructCards()

        return True

    def deleteCards(self, ids:Iterable[str]) -> bool:
        if not hasAll(ids, self.__cards):
            return False

        for _id in ids: self.__regs.pop(_id)
        self.__updateStructCats()

        return True

    def getCardById(self, id:str): return self.__cards.get(id)
    
    def getCardByName(self, name:str): return self.__cardsByName.get(name)
    
    def getCards(self): return self.__tupleCards
    
    #endregion

    #region Category

    def newCategory(self, cat:Category) -> bool:
        if not cat.name:
            return False
        
        cat.id = str(uuid4())
        self.__categories[cat.id] = cat
        self.__updateStructCats()

        return True

    def updateCategory(self, cat:Category) -> bool:
        if cat.id not in self.__categories:
            return False
    
        self.__categories[cat.id] = cat
        self.__updateStructCats()
        
        return True

    def deleteCard(self, id:str) -> bool:
        if id not in self.__categories:
            return False
        
        self.__categories.pop(id)
        self.__updateStructCats()

        return True

    def deleteCats(self, ids:Iterable[str]) -> bool:
        if not hasAll(ids, self.__categories):
            return False

        for _id in ids: self.__categories.pop(_id)
        self.__updateStructCats()

        return True

    def getCategoryById(self, id:str): return self.__categories.get(id)
    
    def getCategories(self): return self.__tupleCategories
    
    def getCategoryByName(self, name:str, regType:RegType): return self.__catsByName[regType].get(name)

    #endregion

    #endregion
    #----------------------------------------------------------
    #region Private Methods
    def __updateStructs(self):
        self.__updateStructRegs()
        self.__updateStructCards()
        self.__updateStructCats()

    def __updateStructRegs(self):
        self.__tupleRegs = tuple(self.__regs.values())
        self.regsChanged.emit(self.__tupleRegs)

    def __updateStructCards(self):
        self.__tupleCards = tuple(self.__cards.values())
        self.__cardsByName = { c.name: c for c in self.__tupleCards }
        self.cardsChanged.emit(self.__tupleCards)

    def __updateStructCats(self):
        self.__tupleCategories = tuple(self.__categories.values())
        self.__catsByName = {
            RegType.IN : { c.name: c for c in filter(lambda x: x.type == RegType.IN, self.__tupleCategories) },
            RegType.OUT : { c.name: c for c in filter(lambda x: x.type == RegType.OUT, self.__tupleCategories) },
        }

        self.categoriesChanged.emit(self.__tupleCategories)

    def __generateTestData(self):
        self.__categories = {
            '0': Category('0', 'Alimentação', RegType.OUT),
            '1': Category('1', 'Transporte', RegType.OUT),
            '2': Category('2', 'Pagamento', RegType.IN),
        }

        self.__cards = {
            '0': Card('0', 'Nubank'),
            '1': Card('1', 'Will'),
        }

        self.__regs = {
            '0': Registry('0', RegType.IN, 'salário', 2000, QDateTime(2025, 9, 1, 6, 0, 0), category=self.__categories['2']),
            '1': Registry('1', RegType.OUT, 'Uber', 12, QDateTime(2025, 9, 10, 11, 48, 0), category=self.__categories['1']),
            '2': Registry('2', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '3': Registry('3', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '4': Registry('4', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '5': Registry('5', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '6': Registry('6', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '7': Registry('7', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '8': Registry('8', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '9': Registry('9', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '10': Registry('10', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '11': Registry('11', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '12': Registry('12', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '13': Registry('13', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '14': Registry('14', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '15': Registry('15', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '16': Registry('16', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '17': Registry('17', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '18': Registry('18', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '19': Registry('19', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '20': Registry('20', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '21': Registry('21', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
            '22': Registry('22', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
        }

    #endregion
    #----------------------------------------------------------