from PySide6.QtCore import QObject, Signal
from threading import Thread
import logging as log
from time import sleep

from finances.api.server import ServerClient
from finances.core import structs
from finances.core.tools import dataclassToDict
from finances.core.consts import *
from finances.api.config import Configuration

class AppModel(QObject):
    __instance = None
    initializationFinished = Signal(bool)
    currentProfileChanged = Signal(object) # Profile | None
    
    #region Server Events
    
    # Authentication
    authenticationFinished = Signal(bool)
    logoutFinished = Signal()

    # User
    createUserFinished = Signal(bool)
    
    # Profile
    createProfileFinished = Signal(bool)
    profilesUpdated = Signal(dict) # dict[id, Profile]
    defaultProfileUpdated = Signal(structs.Profile)
    noProfileFound = Signal()
    pendingShareFinished = Signal()
    shareProfileFinished = Signal(bool, str)
    
    # Third Parties
    thirdAccessesUpdated = Signal(list) # list[ProfileThirdAccess]
    
    #endregion

    def __init__(self):
        super().__init__()
        self.__profileNames = {}
        self.__thirdAcessesByProfileId = {}
        self.__server = ServerClient(self)
        self.__config = Configuration()
        self.__clearSessionData()

        self.__server.connectionError.connect(self.on_server_connectionError)
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
        self.__clearSessionData()
        self.clearSavedCredentials()
        self.__server.sendCommand(CMD_LOGOUT)
    
    def createUser(self, data:structs.User):
        log.debug(f'[AppModel] create user {data}')
        self.__server.sendCommand(CMD_CREATE_USER, dataclassToDict(data))

    def createProfile(self, name:str):
        self.__server.sendCommand(CMD_CREATE_PROFILE, { 'name': name })

    def shareProfile(self, shareData:structs.ShareProfile):
        log.debug(f'[AppModel] share profile {shareData}')
        d = dataclassToDict(shareData)
        d['profileId'] = d.pop('profile').id
        self.__server.sendCommand(CMD_SHARE_PROFILE, d)

    def pendingShare(self, roleId:str, accept:bool):
        self.__server.sendCommand(CMD_PENDING_SHARE, { 'roleId': roleId, 'accept': accept })
    
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
    #region SET
    def setCurrentProfile(self, profile:structs.Profile|None):
        self.__currentProfile = profile
        self.currentProfileChanged.emit(profile)

    #endregion
    #----------------------------------------------------------------------
    #region GET
    def getDefaultProfile(self) -> structs.Profile | None: return self.__defaultProfile
    def getUser(self) -> structs.User | None: return self.__user
    def getProfiles(self) -> dict[str, structs.Profile] | None: return self.__profiles
    def getOwnProfiles(self) -> dict[str, structs.Profile] | None: return self.__ownProfiles
    def getProfileById(self, pId:str): return self.__profiles.get(pId) if self.__profiles else None
    def getCurrentProfile(self): return self.__currentProfile
    def getProfileThirdAcesses(self): return self.__thirdAcesses
    def getProfileThirdByProfileId(self, profileId:str): return self.__thirdAcessesByProfileId.get(profileId)

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

    def on_server_commandReceived(self, cmd:str, params:list|dict|None):
        log.debug(f'[AppModel] command received from server {cmd=} {params=}')

        # Authentication
        if cmd == CMD_AUTH: self.__responseAuth(params)
        elif cmd == CMD_LOGOUT: self.logoutFinished.emit()
        
        # User
        elif cmd == CMD_CREATE_USER: self.createUserFinished.emit(params['success'])
        
        # Profile
        elif cmd == CMD_CREATE_PROFILE: self.createProfileFinished.emit(params['success'])
        elif cmd == CMD_GET_PROFILES: self.__responseGetProfiles(params)
        elif cmd == CMD_GET_ID_FROM_DEFAULT_PROFILE: self.__responseGetIdFromDefaultProfile(params)
        elif cmd == CMD_UPDATE_DEF_PROFILE: ...
        elif cmd == CMD_NO_PROFILE_FOUND: self.noProfileFound.emit()
        elif cmd == CMD_PENDING_SHARE: self.__responsePendingShare(params)
        elif cmd == CMD_SHARE_PROFILE: self.shareProfileFinished.emit(params['success'], params['msg'])

        # Third Parties
        elif cmd == CMD_GET_PROFILE_THIRD_ACCESSES: self.__responseGetProfileThirdAccesses(params)
        
        else: log.error(f'undefined command {cmd=} {params=}')

    #endregion
    #----------------------------------------------------------------------
    def __clearSessionData(self):
        self.__user = None
        self.__loginData = None
        self.__profiles = None
        self.__ownProfiles = None
        self.__currentProfile = None
        self.__thirdAcesses = None
        self.__defaultProfile = None
        self.__profileNames.clear()
        self.__thirdAcessesByProfileId.clear()
    
    #region Server Response

    # Authentication
    def __responseAuth(self, params):
        success = params['success']

        if success:
            self.__user = structs.User(**params['user'])
            self.requireInitialValues()

        else:
            self.__user = None
            self.clearSavedCredentials()

        self.authenticationFinished.emit(success)

    # User

    # Profile
    def __responseGetProfiles(self, params):
        self.__profiles = { d['id'] : structs.Profile(**d) for d in params }
        self.__profileNames = { p.id : (p.name if p.isOwner else f'{p.name} ({p.ownerName})') for p in filter(lambda p: not p.pendingShare, self.__profiles.values()) }
        self.__ownProfiles = { p.id : p for p in filter(lambda p: p.isOwner, self.__profiles.values()) }

        self.profilesUpdated.emit(self.__profiles)
    
    def __responseGetIdFromDefaultProfile(self, params):
        self.__defaultProfile = self.__profiles[params['profileId']]
        self.defaultProfileUpdated.emit(self.__defaultProfile)

    def __responsePendingShare(self, params):
        self.pendingShareFinished.emit()
        self.requireProfiles()
    
    # Third Parties
    def __responseGetProfileThirdAccesses(self, params):
        self.__thirdAcesses = [ structs.ProfileThirdAccess(**d) for d in params ]

        # splitting by profileId
        self.__thirdAcessesByProfileId = { t.profileId : list(filter(lambda x: x.profileId == t.profileId, self.__thirdAcesses)) for t in self.__thirdAcesses }

        self.thirdAccessesUpdated.emit(self.__thirdAcesses)


    #endregion
    #----------------------------------------------------------------------
