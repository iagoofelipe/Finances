from typing import Iterable
from dataclasses import fields
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget, QVBoxLayout, QComboBox, QSpinBox, QApplication
from PySide6.QtGui import QPalette
from uuid import uuid4
from .consts import FONT

from .consts import STYLE_PROPERTIES_LIGHT, STYLE_PROPERTIES_DARK

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
            background-color: transparent;
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
            background-color: transparent;
        }

        %(ids_label)s {
            color: %(COLOR_SUBTITLE)s;
        }

        %(ids_comboBox_dropdown)s {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px; 
            border: none;
            border-radius: 5px;
        }

        %(ids_comboBox_downarrow)s {
            image: url(%(ICON_DOWN)s);
            background-color: transparent;
            width: 25px;
            height: 25px;
        }
        
        /*%(ids_comboBox_item)s {
            border: %(BORDER)s;
        }*/
    """,
    'btns-highlight': """
        %(ids)s {
            background-color: %(BG_HIGHLIGHT)s;
            border: none;
            border-radius: %(BORDER_RADIUS)s;
            padding: 11 31;
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

    """,
    'title': """
        %(ids)s {
            color: %(COLOR_TITLE)s;
        }
    """,
    'abstractSpin': """
        %(ids)s {
            background-color: %(BG_PRIMARY)s;
            border: %(BORDER)s;
            border-radius: %(BORDER_RADIUS)s;
        }

        %(ids_spin)s {
            border: none;
            background-color: transparent;
        }

        %(ids_label)s {
            color: %(COLOR_SUBTITLE)s;
        }
    """
}

def isDarkTheme() -> bool:
    bg_color = QApplication.instance().palette().color(QPalette.ColorRole.Window)
    return bg_color.toHsv().value() < 127

def generateStyleSheet(inputs:Iterable[str]=None, highlightBtns:Iterable[str]=None, secondaryButtons:Iterable[str]=None, linkBtns:Iterable[str]=None, title:Iterable[str]=None, combobox:Iterable[str]=None, abstractSpin:Iterable[str]=None):
    isdark = isDarkTheme()
    props = (STYLE_PROPERTIES_DARK if isdark else STYLE_PROPERTIES_LIGHT).copy()
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
            'ids_comboBox_dropdown': ', '.join([x + ' QComboBox::drop-down' for x in combobox]),
            'ids_comboBox_dropdown_hover': ', '.join([x + ' QComboBox::drop-down:hover' for x in combobox]),
            'ids_comboBox_downarrow': ', '.join([x + ' QComboBox::down-arrow' for x in combobox]),
            'ids_comboBox_item': ', '.join([x + ' QAbstractItemView' for x in combobox]),
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

    if abstractSpin:
        props.update({
            'ids': ', '.join(abstractSpin),
            'ids_spin': ', '.join([x + ' QAbstractSpinBox' for x in abstractSpin]),
            'ids_label': ', '.join([x + ' QLabel' for x in abstractSpin]),
        })
        style += __style['abstractSpin'] % props

    return style

def dataclassToDict(obj:object):
    return { field.name : getattr(obj, field.name) for field in fields(obj) }

def generateInputForm(labelTitle:str, parent:QWidget=None, font=FONT):
    widget = QWidget(parent)
    widId = str(uuid4()).replace('-', '')
    widget.setObjectName(widId)

    layout = QVBoxLayout(widget)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(0)

    label = QLabel(labelTitle, widget)
    layout.addWidget(label)
    
    lineEdit = QLineEdit(widget)
    layout.addWidget(lineEdit)

    widget.setStyleSheet(generateStyleSheet(
        inputs=[f'QWidget#{widId}']
    ))

    if font:
        label.setFont(font)
        lineEdit.setFont(font)

    return widget, lineEdit, layout

def generateComboBox(labelTitle:str, parent:QWidget=None, font=FONT):
    widget = QWidget(parent)
    widId = str(uuid4()).replace('-', '')
    widget.setObjectName(widId)

    layout = QVBoxLayout(widget)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(0)

    label = QLabel(labelTitle, widget)
    layout.addWidget(label)
    
    comboBox = QComboBox(widget)
    layout.addWidget(comboBox)

    widget.setStyleSheet(generateStyleSheet(
        combobox=[f'QWidget#{widId}']
    ))

    if font:
        label.setFont(font)
        comboBox.setFont(font)

    return widget, comboBox, layout

def generateSpinBox(labelTitle:str, parent:QWidget=None, font=FONT, **spinParams):
    widget = QWidget(parent)
    widId = str(uuid4()).replace('-', '')
    widget.setObjectName(widId)

    layout = QVBoxLayout(widget)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(0)

    label = QLabel(labelTitle, widget)
    layout.addWidget(label)
    
    spin = QSpinBox(widget, **spinParams)
    spin.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
    layout.addWidget(spin)

    widget.setStyleSheet(generateStyleSheet(
        abstractSpin=[f'QWidget#{widId}']
    ))

    if font:
        label.setFont(font)
        spin.setFont(font)

    return widget, spin, layout