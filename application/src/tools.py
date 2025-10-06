from typing import Iterable

STYLE_PROPERTIES = {
    'BG_HIGHLIGHT': '#59A1FF',
    'BG_HIGHLIGHT_HOVER': "#2E70C7",
    'BG_PRIMARY': '#FFFFFF',
    'BG_SECONDARY': '#F6F6F6',
    'BORDER': '1px solid #EDEDED',
    'BORDER_RADIUS': 15,
    'COLOR_HIGHLIGHT': '#006FFF',
    'COLOR_TITLE': '#000000',
    'COLOR_SUBTITLE': '#636363',
}

__style = {
    'default': """

    """,
    'inputs': """
        %(ids)s {
            background-color: %(BG_PRIMARY)s;
            border: %(BORDER)s;
            border-radius: %(BORDER_RADIUS)s;
        }

        %(ids_lineEdit)s {
            border: none;
        }

        %(ids_label)s {
            color: %(COLOR_SUBTITLE)s;
        }
    """,
    'btns-highlight': """
        %(ids)s {
            background-color: %(BG_HIGHLIGHT)s;
            border: none;
            border-radius: %(BORDER_RADIUS)s;
            padding: 10;
            color: white;
        }

        %(ids_hover)s {
            background-color: %(BG_HIGHLIGHT_HOVER)s;
        }
    """,
    'btns-secondary': """
        %(ids)s {
            background-color: %(BG_PRIMARY)s;
            color: %(COLOR_SUBTITLE)s;
            border: %(BORDER)s;
            border-radius: %(BORDER_RADIUS)s;
            padding: 10;
        }

        %(ids_hover)s {
            color: %(BG_HIGHLIGHT_HOVER)s;
            border: 1px solid %(BG_HIGHLIGHT_HOVER)s;
        }
    """,
    'btns-link': """ 
        %(ids)s {
            color: %(COLOR_HIGHLIGHT)s;
            background-color: transparent;
            padding: 0;
        }

        %(ids_hover)s {
            background-color: %(BG_SECONDARY)s;
        }
    """
}

def generateStyleSheet(inputs:Iterable[str]=None, highlightBtns:Iterable[str]=None, secondaryButtons:Iterable[str]=None, linkBtns:Iterable[str]=None):
    props = STYLE_PROPERTIES.copy()
    style = __style['default']

    if inputs:
        props.update({
            'ids': ', '.join(inputs),
            'ids_lineEdit': ', '.join([x + ' QLineEdit' for x in inputs]),
            'ids_label': ', '.join([x + ' QLabel' for x in inputs]),
        })
        style += __style['inputs'] % props

    if highlightBtns:
        props.update({
            'ids': ', '.join(highlightBtns),
            'ids_hover': ', '.join([x + '::hover' for x in highlightBtns]),
        })
        style += __style['btns-highlight'] % props

    if secondaryButtons:
        props.update({
            'ids': ', '.join(secondaryButtons),
            'ids_hover': ', '.join([x + '::hover' for x in secondaryButtons]),
        })
        style += __style['btns-secondary'] % props

    if linkBtns:
        props.update({
            'ids': ', '.join(linkBtns),
            'ids_hover': ', '.join([x + '::hover' for x in linkBtns]),
        })
        style += __style['btns-link'] % props

    return style