from PySide6.QtWidgets import (
    QLabel, QLineEdit, QWidget, QVBoxLayout,
    QComboBox, QSpinBox, QApplication
)
from PySide6.QtGui import QPalette
from dataclasses import fields
from typing import Iterable
from uuid import uuid4

from finances.core.consts import FONT, STYLE_PROPERTIES_LIGHT, STYLE_PROPERTIES_DARK, STYLE_SCHEMA

def isDarkTheme() -> bool:
    bg_color = QApplication.instance().palette().color(QPalette.ColorRole.Window)
    return bg_color.toHsv().value() < 127

def generateStyleSheet(inputs:Iterable[str]=None, highlightBtns:Iterable[str]=None, secondaryButtons:Iterable[str]=None, linkBtns:Iterable[str]=None, title:Iterable[str]=None, combobox:Iterable[str]=None, abstractSpin:Iterable[str]=None):
    isdark = isDarkTheme()
    props = (STYLE_PROPERTIES_DARK if isdark else STYLE_PROPERTIES_LIGHT).copy()
    style = STYLE_SCHEMA['default']

    if inputs:
        props.update({
            'ids': ', '.join(inputs),
            'ids_lineEdit': ', '.join([x + ' QLineEdit' for x in inputs]),
            'ids_label': ', '.join([x + ' QLabel' for x in inputs]),
        })
        style += STYLE_SCHEMA['inputs'] % props

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
        style += STYLE_SCHEMA['combo'] % props

    if highlightBtns:
        props.update({
            'ids': ', '.join(highlightBtns),
            'ids_hover': ', '.join([x + '::hover' for x in highlightBtns]),
        })
        style += STYLE_SCHEMA['btns-highlight'] % props

    if secondaryButtons:
        props.update({
            'ids': ', '.join(secondaryButtons),
            'ids_hover': ', '.join([x + '::hover' for x in secondaryButtons]),
        })
        style += STYLE_SCHEMA['btns-secondary'] % props

    if linkBtns:
        props.update({
            'ids': ', '.join(linkBtns),
            'ids_hover': ', '.join([x + '::hover' for x in linkBtns]),
        })
        style += STYLE_SCHEMA['btns-link'] % props

    if title:
        props.update({
            'ids': ', '.join(title)
        })
        style += STYLE_SCHEMA['title'] % props

    if abstractSpin:
        props.update({
            'ids': ', '.join(abstractSpin),
            'ids_spin': ', '.join([x + ' QAbstractSpinBox' for x in abstractSpin]),
            'ids_label': ', '.join([x + ' QLabel' for x in abstractSpin]),
        })
        style += STYLE_SCHEMA['abstractSpin'] % props

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