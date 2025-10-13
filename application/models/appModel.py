from PySide6.QtCore import QObject, Signal
from threading import Thread
import logging as log
from time import sleep

from . import serverClient as server
from ..src import structs
from ..src.tools import dataclassToDict
from ..src.consts import *
from .config import Configuration

class AppModel(QObject):
    initializationFinished = Signal(bool)
    authenticationFinished = Signal(bool)
    createUserFinished = Signal(bool)
    createProfileFinished = Signal(bool)
    logoutFinished = Signal()
    noProfileFound = Signal()
    profilesUpdated = Signal(dict) # dict[id, Profile]
    thirdAccessesUpdated = Signal(list) # list[ProfileThirdAccess]
    defaultProfileUpdated = Signal(structs.Profile)
    __instance = None

    def __init__(self):
        super().__init__()
        self.__user = None
        self.__server = server.ServerClient(self)
        self.__loginData = None
        self.__profiles = None
        self.__ownProfiles = None
        self.__currentProfile = None
        self.__profileNames = {}
        self.__thirdAcesses = None
        self.__defaultProfile = None
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
            sleep(1)
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

    def createProfile(self, name:str):
        self.__server.sendCommand(CMD_CREATE_PROFILE, { 'name': name })
    
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

    #----------------------------------------------------------------------
    #region GET
    def getDefaultProfile(self) -> structs.Profile | None: return self.__defaultProfile
    def getUser(self) -> structs.User | None: return self.__user
    def getProfiles(self) -> dict[str, structs.Profile] | None: return self.__profiles
    def getOwnProfiles(self) -> dict[str, structs.Profile] | None: return self.__ownProfiles
    def getProfileById(self, pId:str): return self.__profiles.get(pId) if self.__profiles else None
    def getCurrentProfile(self): return self.__currentProfile
    def getProfileThirdAcesses(self): return self.__thirdAcesses

    def getProfileNames(self) -> dict[str, str]:
        """
        returns the id and the name of the profile, add the owner's name if
        the profile is not from the current user
        """
        return self.__profileNames
    
    #endregion
    #----------------------------------------------------------------------
    #region REQUIRE
    def requireInitialValues(self):
        self.requireProfiles()
        self.requireProfileThirdAcesses()
        self.requireDefaultProfile()

    def requireProfiles(self):
        # TODO: add cache verification
        self.__server.sendCommand(CMD_GET_PROFILES)

    def requireProfileThirdAcesses(self):
        self.__server.sendCommand(CMD_GET_PROFILE_THIRD_ACCESSES)

    def requireDefaultProfile(self):
        self.__server.sendCommand(CMD_GET_ID_FROM_DEFAULT_PROFILE)

    #endregion
    #----------------------------------------------------------------------
    #region Events
    def on_server_connectionError(self):
        log.info('[AppModel] connection error with the server')

    def on_server_connectionClosed(self):
        log.info('[AppModel] connection closed with the server')

    def on_server_commandReceived(self, cmd:str, params:list|dict|None):
        log.debug(f'[AppModel] command received from server {cmd=} {params=}')

        if cmd == CMD_AUTH: self.__responseAuth(params)
        elif cmd == CMD_LOGOUT: self.logoutFinished.emit()
        elif cmd == CMD_CREATE_USER: self.createUserFinished.emit(params['success'])
        elif cmd == CMD_CREATE_PROFILE: self.createProfileFinished.emit(params['success'])
        elif cmd == CMD_NO_PROFILE_FOUND: self.noProfileFound.emit()
        elif cmd == CMD_GET_PROFILES: self.__responseGetProfiles(params)
        elif cmd == CMD_GET_PROFILE_THIRD_ACCESSES: self.__responseGetProfileThirdAccesses(params)
        elif cmd == CMD_GET_ID_FROM_DEFAULT_PROFILE: self.__responseGetIdFromDefaultProfile(params)
        elif cmd == CMD_UPDATE_DEF_PROFILE: ...
        else: log.error(f'undefined command {cmd=} {params=}')

    #endregion
    #----------------------------------------------------------------------
    #region Server Response
    def __responseAuth(self, params):
        success = params['success']

        if success:
            self.__user = structs.User(**params['user'])
            self.requireInitialValues()

        else:
            self.__user = None
            self.clearSavedCredentials()

        self.authenticationFinished.emit(success)

    def __responseGetProfiles(self, params):
        self.__profiles = { d['id'] : structs.Profile(**d) for d in params }
        self.__profileNames = { p.id : (p.name if p.isOwner else f'{p.name} ({p.ownerName})') for p in filter(lambda p: not p.pendingShare, self.__profiles.values()) }
        self.__ownProfiles = { p.id : p for p in filter(lambda p: p.isOwner, self.__profiles.values()) }

        self.profilesUpdated.emit(self.__profiles)
        
    def __responseGetProfileThirdAccesses(self, params):
        self.__thirdAcesses = [ structs.ProfileThirdAccess(**d) for d in params ]
        self.thirdAccessesUpdated.emit(self.__thirdAcesses)

    def __responseGetIdFromDefaultProfile(self, params):
        self.__defaultProfile = self.__profiles[params['profileId']]
        self.defaultProfileUpdated.emit(self.__defaultProfile)

    #endregion
    #----------------------------------------------------------------------
        

AppModel._AppModel__instance = AppModel()