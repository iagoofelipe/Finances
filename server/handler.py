import json
import logging as log
import asyncio
from dataclasses import fields

from .consts import *
from . import database

def dataclassToDict(obj:database.AbstractTable) -> dict: return { field.name : getattr(obj, field.name) for field in fields(obj) }

class FinancesClientHandler:
    clients:dict[str, list['FinancesClientHandler']] = {} # the key is User.id

    def __init__(self, db:database.FinancesDatabase, id:int, reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
        self.__db = db
        self.__id = id
        self.__reader = reader
        self.__writer = writer
        self.__user = None
        self.__pref = f'(Client {self.__id})'

    #region Authentication
    async def auth(self, username:str, password:str):
        self.__user = self.__db.auth(username, password)
        name, dict_user = None, None

        # case success
        if self.__user:
            name = self.__user.name
            dict_user = dataclassToDict(self.__user)
            if self.__user.id not in self.clients:
                self.clients[self.__user.id] = []

            self.clients[self.__user.id].append(self)
        
        log.info(f'{self.__pref} user authenticated {name=}')

        await self.sendCommand(CMD_AUTH, { 'success': bool(self.__user), 'user': dict_user })

    async def logout(self):
        userId = self.__user.id
        self.__user = None
        
        if userId in self.clients and self in self.clients[userId]:
            self.clients[userId].remove(self)
        
        log.debug(f'{self.__pref} user logout')
        await self.sendCommand(CMD_LOGOUT)

    #endregion
    
    #region User
    async def createUser(self, **params):
        log.info(f'{self.__pref} create user required with {params=}')
        user = self.__db.createUser(**params)
        success = bool(user)
        log.info(f'{self.__pref} create user result {success=}')

        # create the default profile
        if success:
            await self.createProfile(send=False, name='Principal', user_id=user.id)
            
        
        await self.sendCommand(CMD_CREATE_USER, { 'success': success })
    
    #endregion
    
    #region Profile
    async def createProfile(self, send=True, defaultProfile=False, **params):
        log.info(f'{self.__pref} create profile required with {params=}')

        user_id = self.__user.id if self.__user else params.pop('user_id')
        data = {
            'success': False,
            'error': None,
        }
        
        # whether there is any profile with the same fields
        if self.__db.getCount(database.Profile, name=params['name'], user_id=user_id):
            if send:
                data['error'] = 'já existe um perfil com esse nome para este usuário!'
                await self.sendCommand(CMD_CREATE_PROFILE, data)
            return

        data['success'] = True
        profile = self.__db.create(database.Profile, **params, user_id=user_id)
        profileRole = self.__db.create(database.ProfileRole, profile_id=profile.id, user_id=user_id, pending=False, edit=True, view=True)

        if defaultProfile:
            await self.setDefaultProfile(profile.id, False)
        
        if not send: return

        await self.sendCommand(CMD_CREATE_PROFILE, data)
        await self.getProfiles() # if there is data, sends to user, sends NO_PROFILE_FOUND otherwise
    
    async def getProfiles(self, send=True, justOne=False) -> list[dict] | None:
        """ if there is data, sends to user, sends NO_PROFILE_FOUND otherwise """

        if not await self.checkProfile(): return
        
        sql = f"""
        SELECT
            profile.id, profile.name, profile_role.edit, profile_role.view, profile_role.pending,
            (SELECT user.name FROM profile INNER JOIN user ON profile.user_id = user.id WHERE profile.id = profile_role.profile_id) as ownerName,
            profile.user_id,
            profile_role.id
        FROM profile_role
        INNER JOIN profile ON profile_role.profile_id = profile.id
        INNER JOIN user ON profile_role.user_id = user.id
        WHERE
            profile_role.user_id = ?
            AND (profile_role.edit = 1 OR profile_role.view = 1)
        {'LIMIT 1' if justOne else ''}
        """
        self.__db.cursor.execute(sql, (self.__user.id, ))
        data = []

        for row in self.__db.cursor.fetchall():
            d = {
                'id': row[0],
                'name': row[1],
                'editPermission': bool(row[2]),
                'viewPermission': bool(row[3]),
                'pendingShare': bool(row[4]),
                'ownerName': row[5],
                'isOwner': self.__user.id == row[6],
                'accessType': 'Indefinido',
                'roleId': row[7],
            }

            if d['isOwner']: d['accessType'] = 'Proprietário'
            elif d['editPermission']: d['accessType'] = 'Edição'
            elif d['viewPermission']: d['accessType'] = 'Visualização'

            data.append(d)
        
        if send:
            await self.sendCommand(CMD_GET_PROFILES, data)

        return data
    
    async def getIdFromDefaultProfile(self, send=True) -> str | None:
        if not await self.checkProfile(): return

        sql = """
        SELECT profile_id FROM profile_role WHERE is_default=1 AND user_id=? AND (view=1 OR edit=1) LIMIT 1;
        """

        self.__db.cursor.execute(sql, (self.__user.id, ))

        r = self.__db.cursor.fetchone()
        if not r:
            # updates the default profile to a valid one
            profile = (await self.getProfiles(False, True))[0]
            profileId = profile['id']
            await self.setDefaultProfile(profileId, False)
        else:
            profileId = r[0]

        if send:
            await self.sendCommand(CMD_GET_ID_FROM_DEFAULT_PROFILE, { 'profileId': profileId })

        return profileId
    
    async def setDefaultProfile(self, profileId:str, send=True):
        sql = """
        UPDATE profile_role SET is_default = 0 WHERE user_id = '%(userId)s';
        UPDATE profile_role SET is_default = 1 WHERE profile_id = '%(profileId)s' AND user_id = '%(userId)s';
        """ % { 'profileId': profileId, 'userId': self.__user.id }
        
        self.__db.cursor.executescript(sql)
        self.__db.commit()

        if send:
            await self.sendCommand(CMD_UPDATE_DEF_PROFILE, { 'profileId': profileId })

    async def checkProfile(self):
        sql, args = f'SELECT COUNT(*) FROM {database.ProfileRole.__table__} WHERE user_id=? AND pending=0 AND (edit=1 OR view=1)', (self.__user.id, )
        self.__db.cursor.execute(sql, args)
        count = self.__db.cursor.fetchone()[0]
        found = bool(count)
        
        log.debug(f"checking profiles for <User id='{self.__user.id}' name='{self.__user.name}'>, {count} value(s) found")

        if not found:
            await self.sendCommand(CMD_NO_PROFILE_FOUND)
        
        return found
    
    async def pendingShare(self, roleId:str, accept:bool):
        # getting the ownerId to be notified later
        sql = """
        SELECT
            profile.user_id as ownerId
        FROM profile_role
        INNER JOIN profile ON profile_role.profile_id = profile.id
        WHERE
            profile_role.id = ?
        """
        self.__db.cursor.execute(sql, (roleId, ))
        ownerId = self.__db.cursor.fetchone()[0]
        
        # updating accept
        sql = """ UPDATE profile_role SET pending = 0 WHERE id = ? """ if accept else """ DELETE FROM profile_role WHERE id = ? """

        self.__db.cursor.execute(sql, (roleId, ))
        self.__db.commit()

        await self.sendCommand(CMD_PENDING_SHARE)

        # notifying the owner if connected
        if ownerId in self.clients:
            for handler in self.clients[ownerId]: # to all instances
                await handler.getProfileThridAccesses()

    async def shareProfile(self, email:str, profileId:str, shareType:int):
        #TODO: Add transfer property
        if shareType == SHARE_TYPE_PROPERTY:
            log.debug(f'{self.__pref} share property required, not available')
            await self.sendCommand(CMD_SHARE_PROFILE, { 'success': False, 'msg': 'o tipo de transferência não está disponível no momento' })
            return
        
        edit = shareType == SHARE_TYPE_EDIT
        view = shareType == SHARE_TYPE_VIEW or shareType == SHARE_TYPE_EDIT
        log.debug(f'{self.__pref} share {edit=} {view=}')
        
        # getting the user id by email
        self.__db.cursor.execute(' SELECT id FROM user WHERE email = ? ', (email, ))
        r = self.__db.cursor.fetchone()
        if not r:
            await self.sendCommand(CMD_SHARE_PROFILE, { 'success': False, 'msg': 'nenhum usuário encontrado para o E-mail informado!' })
            return
        
        userId = r[0]

        # check if the role already exists
        self.__db.cursor.execute('SELECT COUNT(*) FROM profile_role WHERE profile_id=? AND user_id=?', (profileId, userId))
        r = self.__db.cursor.fetchone()

        if not r:
            await self.sendCommand(CMD_SHARE_PROFILE, { 'success': False, 'msg': 'já existe um compartilhamento entre este perfil e usuário!' })
            return
        
        profileRole = self.__db.create(database.ProfileRole, edit=edit, view=view, pending=True, profile_id=profileId, user_id=userId)
        
        await self.sendCommand(CMD_SHARE_PROFILE, { 'success': bool(profileRole), 'msg': None })

        # notifying the owner if connected
        if userId in self.clients:
            for handler in self.clients[userId]: # to all instances
                await handler.getProfiles()

    #endregion
    
    #region Third Parties
    async def getProfileThridAccesses(self):

        # users with access to the profiles of the current user
        sql = """
        SELECT
            profile_id, profile.name as profileName,
            profile_role.edit, profile_role.view, profile_role.pending,
            user.name as userName,
            user.id as userId,
            profile_role.id
        FROM profile_role
        INNER JOIN user ON profile_role.user_id = user.id
        INNER JOIN profile ON profile_role.profile_id = profile.id
        WHERE
            profile_id IN (SELECT id FROM profile WHERE user_id = ?)
            AND profile_role.user_id != ?;
        """
        self.__db.cursor.execute(sql, (self.__user.id, self.__user.id))
        data = []

        for row in self.__db.cursor.fetchall():
            data.append({
                'profileId': row[0],
                'profileName': row[1],
                'editPermission': bool(row[2]),
                'viewPermission': bool(row[3]),
                'pendingShare': bool(row[4]),
                'status': 'Pendente' if row[4] else 'Liberado',
                'userName': row[5],
                'userId': row[6],
                'id': row[7]
            })

        await self.sendCommand(CMD_GET_PROFILE_THIRD_ACCESSES, data)

    #endregion

    #region Card
    async def createCard(self, **params):
        self.__db.create()

    #endregion

    #region Aux Methods
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

        elif cmd == CMD_CREATE_PROFILE:
            await self.createProfile(**params)

        elif cmd == CMD_GET_PROFILES:
            await self.getProfiles()

        elif cmd == CMD_GET_PROFILE_THIRD_ACCESSES:
            await self.getProfileThridAccesses()

        elif cmd == CMD_GET_ID_FROM_DEFAULT_PROFILE:
            await self.getIdFromDefaultProfile()

        elif cmd == CMD_UPDATE_DEF_PROFILE:
            await self.setDefaultProfile(params['profileId'])
        
        elif cmd == CMD_PENDING_SHARE:
            await self.pendingShare(**params)

        elif cmd == CMD_SHARE_PROFILE:
            await self.shareProfile(**params)

        else:
            log.info(f'{self.__pref} undefined command {cmd}')

    #endregion
    