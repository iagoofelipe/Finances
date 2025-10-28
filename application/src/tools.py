from typing import Iterable
from dataclasses import fields
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget, QVBoxLayout, QComboBox
from uuid import uuid4

from .consts import STYLE_PROPERTIES

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
    'combo': """
        %(ids)s {
            background-color: %(BG_PRIMARY)s;
            border: %(BORDER)s;
            border-radius: %(BORDER_RADIUS)s;
        }

        %(ids_comboBox)s {
            border: none;
        }

        %(ids_label)s {
            color: %(COLOR_SUBTITLE)s;
        }

        %(ids_comboBox)s::drop-down {
            /* Estilo da área do botão drop-down */
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px; 
            border: none;
            border-radius: 5px;
        }

        %(ids_comboBox)s::drop-down:hover {
            background-color: lightgray;
        }

        %(ids_comboBox)s::down-arrow {
            /* Estilo da seta (imagem ou cor) */
            image: url(application/src/ui/imgs/icons/down.svg); /* Se quiser usar uma imagem de seta */
            /* Ou apenas mudar a cor da seta nativa (pode variar o efeito) */
            background-color: transparent; /* Apenas para garantir */
            width: 25px;
            height: 25px;
        }

        %(ids_comboBox)s QAbstractItemView {
            border: 1px solid lightgray;
        }
    """,
    'btns-highlight': """
        %(ids)s {
            background-color: %(BG_HIGHLIGHT)s;
            border: none;
            border-radius: %(BORDER_RADIUS)s;
            padding: 10 30;
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
            padding: 10 30;
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
    """,
    'title': """
        %(ids)s {
            color: %(COLOR_TITLE)s;
        }
    """
}

def generateStyleSheet(inputs:Iterable[str]=None, highlightBtns:Iterable[str]=None, secondaryButtons:Iterable[str]=None, linkBtns:Iterable[str]=None, title:Iterable[str]=None, combobox:Iterable[str]=None):
    props = STYLE_PROPERTIES.copy()
    style = __style['default']

    if inputs:
        props.update({
            'ids': ', '.join(inputs),
            'ids_lineEdit': ', '.join([x + ' QLineEdit' for x in inputs]),
            'ids_label': ', '.join([x + ' QLabel' for x in inputs]),
        })
        style += __style['inputs'] % props

    if combobox:
        props.update({
            'ids': ', '.join(combobox),
            'ids_comboBox': ', '.join([x + ' QComboBox' for x in combobox]),
            'ids_label': ', '.join([x + ' QLabel' for x in combobox]),
        })
        style += __style['combo'] % props

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

    if title:
        props.update({
            'ids': ', '.join(title)
        })
        style += __style['title'] % props

    return style

def dataclassToDict(obj:object):
    return { field.name : getattr(obj, field.name) for field in fields(obj) }

def generateInputForm(labelTitle:str, parent:QWidget=None, font=None):
    widget = QWidget(parent)
    widId = str(uuid4()).replace('-', '')
    widget.setObjectName(widId)

    layout = QVBoxLayout(widget)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(0)

    label = QLabel(labelTitle, widget)
    layout.addWidget(label)
    
    lineEdit = QLineEdit(widget)
    if font: lineEdit.setFont(font)
    layout.addWidget(lineEdit)

    widget.setStyleSheet(generateStyleSheet(
        inputs=[f'QWidget#{widId}']
    ))

    return widget, lineEdit, layout

def generateComboBox(labelTitle:str, parent:QWidget=None, font=None):
    widget = QWidget(parent)
    widId = str(uuid4()).replace('-', '')
    widget.setObjectName(widId)

    layout = QVBoxLayout(widget)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(0)

    label = QLabel(labelTitle, widget)
    layout.addWidget(label)
    
    comboBox = QComboBox(widget)
    if font: comboBox.setFont(font)
    layout.addWidget(comboBox)

    widget.setStyleSheet(generateStyleSheet(
        combobox=[f'QWidget#{widId}']
    ))

    return widget, comboBox, layout