from PySide6.QtCore import QDate

CURRENT_DATE = QDate.currentDate()
DASH_DATE_START = QDate(CURRENT_DATE.year(), CURRENT_DATE.month(), 1)
DASH_DATE_END = QDate(CURRENT_DATE.year(), CURRENT_DATE.month(), DASH_DATE_START.daysInMonth())