from PySide6.QtCore import QDate
import os

CURRENT_DATE = QDate.currentDate()
DASH_DATE_START = QDate(CURRENT_DATE.year(), CURRENT_DATE.month(), 1)
DASH_DATE_END = QDate(CURRENT_DATE.year(), CURRENT_DATE.month(), DASH_DATE_START.daysInMonth())

MAX_ITEMS_TABLE = 20

TABLE_COLS_REG = ['Título', 'Valor', 'Tipo', 'Data Hora', 'Cartão', 'Categoria']

FILE_TMP = os.path.join(os.environ.get('TEMP', '.'), 'finances.ini')