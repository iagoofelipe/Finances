import os as __os

STYLE_PROPERTIES = {
    'BG_HIGHLIGHT': '#59A1FF',
    'BG_HIGHLIGHT_HOVER': "#2E70C7",
    'BG_PRIMARY': '#FFFFFF',
    'BG_SECONDARY': '#F6F6F6',
    'BORDER': '1px solid #EDEDED',
    'BORDER_RADIUS': 15,
    'COLOR_HIGHLIGHT': '#006FFF',
    'COLOR_TITLE': '#5E5E5E',
    'COLOR_SUBTITLE': '#636363',
}

MSG_DELETE_PROFILE = 'O perfil \'%s\' será agendado para exclusão em 30 dias, você pode desfazer esta ação durante esse período. Após o tempo, todos os dados serão perdidos, deseja continuar?'
MSG_SHARE_PROFILE = 'Ao transferir a propriedade, você perderá o acesso ao perfil e, caso necessário, você deverá solicitar acesso de edição ou visualização ao novo proprietário.'

FILE_CONFIG = __os.path.join(__os.environ.get('TMP', '.'), 'Finances.ini')

TABLE_MAX_LEN = 5

SHARE_TYPE_EDIT = 0
SHARE_TYPE_VIEW = 1
SHARE_TYPE_PROPERTY = 2

#region CMDs

# Authentication
CMD_AUTH = 'AUTH'
CMD_LOGOUT = 'LOGOUT'

# User
CMD_CREATE_USER = 'CREATE_USER'

# Profile
CMD_CREATE_PROFILE = 'CREATE_PROFILE'
CMD_GET_PROFILES = 'GET_PROFILES'
CMD_GET_ID_FROM_DEFAULT_PROFILE = 'GET_ID_FROM_DEFAULT_PROFILE'
CMD_UPDATE_DEF_PROFILE = 'UPDATE_DEF_PROFILE'
CMD_NO_PROFILE_FOUND = 'NO_PROFILE_FOUND'
CMD_PENDING_SHARE = 'PENDING_SHARE'
CMD_SHARE_PROFILE = 'SHARE_PROFILE'

# Third Parties
CMD_GET_PROFILE_THIRD_ACCESSES = 'GET_PROFILE_THIRD_ACCESSES'

#endregion
