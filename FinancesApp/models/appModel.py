from PySide6.QtCore import QObject, Signal, QDateTime
from threading import Thread
from time import sleep
from configparser import ConfigParser
from cryptography.fernet import Fernet
import os
import logging as log
from uuid import uuid4

from .consts import FILE_TMP
from .structs import Card, Category, Registry, RegType

class AppModel(QObject):
    initializationFinished = Signal(bool, str)
    authFinished = Signal(bool)
    regsChanged = Signal(tuple[Registry])


    def __init__(self):
        super().__init__()
        log.basicConfig(level=log.DEBUG)

        # temporary data
        self.__categories = {
            '0': Category('0', 'Alimentação', ''),
            '1': Category('1', 'Transporte', ''),
            '2': Category('2', 'Pagamento', ''),
        }

        self.__cards = {
            '0': Card('0', 'Nubank'),
            '1': Card('1', 'Will'),
        }

        self.__regs = {
            '0': Registry('0', RegType.IN, 'salário', 2000, QDateTime(2025, 9, 1, 6, 0, 0), category=self.__categories['2']),
            '1': Registry('1', RegType.OUT, 'Uber', 12, QDateTime(2025, 9, 10, 11, 48, 0), category=self.__categories['1']),
            '2': Registry('2', RegType.OUT, 'onibus', 5.5, QDateTime(2025, 9, 11, 11, 48, 0), category=self.__categories['1']),
        }
        self.__tupleCategories = tuple(self.__categories.values())
        self.__tupleCards = tuple(self.__cards.values())
        self.__tupleRegs = tuple(self.__regs.values())
        
    #----------------------------------------------------------
    # Public Methods
    def initialize(self):
        def func():
            # sleep(3)
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

            self.initializationFinished.emit(True, 'TEST_ERROR')
        
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

    #region Registry

    def newRegistry(self, reg:Registry) -> bool:
        if reg.id in self.__regs:
            return False
        
        reg.id = str(uuid4())
        self.__regs[reg.id] = reg
        self.__tupleRegs = tuple(self.__regs.values())

        self.regsChanged.emit(self.__tupleRegs)
        return True
    
    def updateRegistry(self, reg:Registry) -> bool:
        self.__regs[reg.id] = reg
        self.__tupleRegs = tuple(self.__regs.values())

        self.regsChanged.emit(self.__tupleRegs)
        return True
    
    def deleteRegistry(self, id:str) -> bool:
        if id not in self.__regs:
            return False
        
        self.__regs.pop(id)
        self.__tupleRegs = tuple(self.__regs.values())

        self.regsChanged.emit(self.__tupleRegs)
        return True

    def getRegistryById(self, id:str) -> Registry | None:
        return self.__regs.get(id)

    def getRegistries(self) -> tuple[Registry]:
        return self.__tupleRegs
    
    #endregion
    
    #region Card

    def getCardById(self, id:str) -> Card | None:
        return self.__cards.get(id)
    
    def getCards(self) -> tuple[Card]:
        return self.__tupleCards
    
    def getCategoryById(self, id:str) -> Category | None:
        return self.__categories.get(id)
    
    def getCategories(self) -> tuple[Category]:
        return self.__tupleCategories
    
    #endregion

    #----------------------------------------------------------
    # Private Methods

    #----------------------------------------------------------