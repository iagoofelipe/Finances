from PySide6.QtGui import QFont as __qfont
import os as __os

STYLE_PROPERTIES_LIGHT = {
    'BG_HIGHLIGHT': '#59A1FF',
    'BG_HIGHLIGHT_HOVER': "#2E70C7",
    'BG_APP': 'white',
    'BG_PRIMARY': '#FFFFFF',
    'BG_SECONDARY': '#F6F6F6',
    'BG_NAV_BUTTON': '#F7F7F7',
    'BORDER': '1px solid #EDEDED',
    'BORDER_RADIUS': 15,
    'COLOR_HIGHLIGHT': '#006FFF',
    'COLOR_TITLE': '#5E5E5E',
    'COLOR_SUBTITLE': '#636363',
    'ICON_DOWN': ':/root/icons/light_down.svg',
}

STYLE_PROPERTIES_DARK = {
    'BG_HIGHLIGHT': '#59A1FF',
    'BG_HIGHLIGHT_HOVER': "#2E70C7",
    'BG_APP': '#1E1E1E',
    'BG_PRIMARY': '#323232',
    'BG_SECONDARY': '#F6F6F6',
    'BG_NAV_BUTTON': '#4f4e4e',
    'BORDER': '1px solid #585858',
    'BORDER_RADIUS': 15,
    'COLOR_HIGHLIGHT': '#006FFF',
    'COLOR_TITLE': "#D6D6D6",
    'COLOR_SUBTITLE': "#A5A5A5",
    'ICON_DOWN': ':/root/icons/dark_down.svg',
}

FONT = __qfont('Segoe UI')
FONT.setPointSize(11)

MSG_DELETE_PROFILE = 'O perfil \'%s\' será agendado para exclusão em 30 dias, você pode desfazer esta ação durante esse período. Após o tempo, todos os dados serão perdidos, deseja continuar?'
MSG_SHARE_PROFILE = 'Ao transferir a propriedade, você perderá o acesso ao perfil e, caso necessário, você deverá solicitar acesso de edição ou visualização ao novo proprietário.'

FILE_CONFIG = __os.path.join(__os.environ.get('TMP', '.'), 'Finances.ini')

TABLE_MAX_LEN = 5

#-----------------------------------------------------------------------
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
#-----------------------------------------------------------------------
#region CMDs Consts
SHARE_TYPE_EDIT = 0
SHARE_TYPE_VIEW = 1
SHARE_TYPE_PROPERTY = 2

REG_OP_BETWEEN_ACCOUNTS = 0
REG_OP_INVOICE_PAYMENT = 1
REG_OP_CREDIT = 2
REG_OP_IN = 3
REG_OP_OUT = 4

REG_OPERATION_IDS_BY_NAME = {
    'Transferência': REG_OP_BETWEEN_ACCOUNTS,
    'Pagamento Fatura': REG_OP_INVOICE_PAYMENT,
    'Compra Crédito': REG_OP_CREDIT,
    'Depósito': REG_OP_IN,
    'Débito': REG_OP_OUT,
}

REG_OPERATION_NAMES_BY_ID = {
    REG_OP_BETWEEN_ACCOUNTS: 'Transferência',
    REG_OP_INVOICE_PAYMENT: 'Pagamento Fatura',
    REG_OP_CREDIT: 'Compra Crédito',
    REG_OP_IN: 'Depósito',
    REG_OP_OUT: 'Débito',
}

#endregion
#-----------------------------------------------------------------------