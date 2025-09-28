from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QIcon
from typing import Iterable

from .structs import RegType

def castToRegType(arg:str|int|RegType) -> RegType:
    t = type(arg)

    if t == RegType:
        return arg
    
    if t == str:
        arg = arg.upper()

        if arg == 'IN' or arg == 'ENTRADA':
            return RegType.IN
    
    elif arg == 1:
        return RegType.IN
    
    return RegType.OUT

def isDark() -> bool:
    return QApplication.instance().palette().color(QPalette.ColorRole.Window).lightness() < 128

def hasAll(v1:Iterable, v2:Iterable):
    """ whether all values in v1 are set in v2 """
    for v in v1:
        if v not in v2:
            return False
    return True

def updateIcons(ui:object, args:tuple[tuple[str, str]]) -> str:
    """
    update the button icons 
    
    params:
        - ui:object - with the button instances
        - args:tuple[tuple[str, str]] - tuple with the pair BTN_NAME and SVG_NAME

    return:
        it returns a str with the theme set

    to works, ui object must contains a QPushButton instance named by `<BTN_NAME>` and,
    set on .qrc file, the files named by `:/root/imgs/<dark | light>-<SVG_FILE>.svg`
    """

    currentTheme = 'dark' if isDark() else 'light'

    for btnName, svg in args:
        ui.__getattribute__(btnName).setIcon(QIcon(f':/root/imgs/{currentTheme}-{svg}.svg'))

    return currentTheme

def checkUpdateIconsNeeded(currentTheme:str):
    dark = isDark()
    return (dark and currentTheme == 'light') or (not dark and currentTheme == 'dark')