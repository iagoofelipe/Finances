import os as __os

CMD_AUTH = 'AUTH'
CMD_LOGOUT = 'LOGOUT'
CMD_CREATE_USER = 'CREATE_USER'

FILE_CONFIG = __os.path.join(__os.environ.get('TMP', '.'), 'Finances.ini')