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

CMD_AUTH = 'AUTH'
CMD_LOGOUT = 'LOGOUT'
CMD_CREATE_USER = 'CREATE_USER'
CMD_CREATE_PROFILE = 'CREATE_PROFILE'
CMD_NO_PROFILE_FOUND = 'NO_PROFILE_FOUND'
CMD_GET_PROFILES = 'GET_PROFILES'

MSG_DELETE_PROFILE = 'O perfil Principal será agendado para exclusão em 30 dias, você pode desfazer esta ação durante esse período. Após o tempo, todos os dados serão perdidos, deseja continuar?'

FILE_CONFIG = __os.path.join(__os.environ.get('TMP', '.'), 'Finances.ini')

TABLE_MAX_LEN = 3