# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegForm.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_RegForm(object):
    def setupUi(self, RegForm):
        if not RegForm.objectName():
            RegForm.setObjectName(u"RegForm")
        RegForm.resize(913, 567)
        self.mainLayout = QVBoxLayout(RegForm)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.frameNovoReg = QFrame(RegForm)
        self.frameNovoReg.setObjectName(u"frameNovoReg")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameNovoReg.sizePolicy().hasHeightForWidth())
        self.frameNovoReg.setSizePolicy(sizePolicy)
        self.frameNovoReg.setFrameShape(QFrame.StyledPanel)
        self.frameNovoReg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameNovoReg)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.lbTitleReg = QLabel(self.frameNovoReg)
        self.lbTitleReg.setObjectName(u"lbTitleReg")
        sizePolicy.setHeightForWidth(self.lbTitleReg.sizePolicy().hasHeightForWidth())
        self.lbTitleReg.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.lbTitleReg.setFont(font)

        self.verticalLayout_2.addWidget(self.lbTitleReg)

        self.widRegInputs = QWidget(self.frameNovoReg)
        self.widRegInputs.setObjectName(u"widRegInputs")
        self.gridLayout = QGridLayout(self.widRegInputs)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widTitulo = QWidget(self.widRegInputs)
        self.widTitulo.setObjectName(u"widTitulo")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.widTitulo.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.widTitulo)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.widTitulo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.leTitulo = QLineEdit(self.widTitulo)
        self.leTitulo.setObjectName(u"leTitulo")
        self.leTitulo.setFont(font1)
        self.leTitulo.setFrame(True)

        self.verticalLayout_3.addWidget(self.leTitulo)


        self.gridLayout.addWidget(self.widTitulo, 0, 0, 1, 1)

        self.widContab = QWidget(self.widRegInputs)
        self.widContab.setObjectName(u"widContab")
        self.widContab.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.widContab)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_11 = QLabel(self.widContab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_11)

        self.cbContab = QComboBox(self.widContab)
        self.cbContab.addItem("")
        self.cbContab.addItem("")
        self.cbContab.setObjectName(u"cbContab")
        self.cbContab.setFont(font1)
        self.cbContab.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbContab.setFrame(False)

        self.verticalLayout_4.addWidget(self.cbContab)


        self.gridLayout.addWidget(self.widContab, 0, 1, 1, 1)

        self.widDesc = QWidget(self.widRegInputs)
        self.widDesc.setObjectName(u"widDesc")
        self.widDesc.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.widDesc)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.label_12 = QLabel(self.widDesc)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_12)

        self.leDesc = QLineEdit(self.widDesc)
        self.leDesc.setObjectName(u"leDesc")
        self.leDesc.setFont(font1)
        self.leDesc.setFrame(True)

        self.verticalLayout_5.addWidget(self.leDesc)


        self.gridLayout.addWidget(self.widDesc, 0, 2, 1, 1)

        self.widVal = QWidget(self.widRegInputs)
        self.widVal.setObjectName(u"widVal")
        self.widVal.setFont(font1)
        self.verticalLayout_6 = QVBoxLayout(self.widVal)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.label_13 = QLabel(self.widVal)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_13)

        self.dsVal = QDoubleSpinBox(self.widVal)
        self.dsVal.setObjectName(u"dsVal")
        self.dsVal.setFont(font1)
        self.dsVal.setFrame(True)
        self.dsVal.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_6.addWidget(self.dsVal)


        self.gridLayout.addWidget(self.widVal, 1, 0, 1, 1)

        self.widData = QWidget(self.widRegInputs)
        self.widData.setObjectName(u"widData")
        self.widData.setFont(font1)
        self.verticalLayout_7 = QVBoxLayout(self.widData)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.label_14 = QLabel(self.widData)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_14)

        self.dtData = QDateEdit(self.widData)
        self.dtData.setObjectName(u"dtData")
        self.dtData.setFont(font1)
        self.dtData.setFrame(True)
        self.dtData.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dtData.setCalendarPopup(False)

        self.verticalLayout_7.addWidget(self.dtData)


        self.gridLayout.addWidget(self.widData, 1, 1, 1, 1)

        self.lbTitleOp = QLabel(self.widRegInputs)
        self.lbTitleOp.setObjectName(u"lbTitleOp")
        self.lbTitleOp.setFont(font)
        self.lbTitleOp.setMargin(0)

        self.gridLayout.addWidget(self.lbTitleOp, 2, 0, 1, 3)

        self.widOperacao = QWidget(self.widRegInputs)
        self.widOperacao.setObjectName(u"widOperacao")
        self.widOperacao.setFont(font1)
        self.verticalLayout_9 = QVBoxLayout(self.widOperacao)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.label_16 = QLabel(self.widOperacao)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_16)

        self.cbOperacao = QComboBox(self.widOperacao)
        self.cbOperacao.setObjectName(u"cbOperacao")
        self.cbOperacao.setFont(font1)
        self.cbOperacao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbOperacao.setFrame(False)

        self.verticalLayout_9.addWidget(self.cbOperacao)


        self.gridLayout.addWidget(self.widOperacao, 3, 0, 1, 1)

        self.widCat = QWidget(self.widRegInputs)
        self.widCat.setObjectName(u"widCat")
        self.widCat.setFont(font1)
        self.verticalLayout_8 = QVBoxLayout(self.widCat)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.label_15 = QLabel(self.widCat)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_15)

        self.cbCat = QComboBox(self.widCat)
        self.cbCat.setObjectName(u"cbCat")
        self.cbCat.setFont(font1)
        self.cbCat.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.cbCat.setEditable(True)
        self.cbCat.setFrame(True)

        self.verticalLayout_8.addWidget(self.cbCat)


        self.gridLayout.addWidget(self.widCat, 1, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout_2.addWidget(self.widRegInputs)

        self.widget_2 = QWidget(self.frameNovoReg)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(718, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnLimpar = QPushButton(self.widget_2)
        self.btnLimpar.setObjectName(u"btnLimpar")
        self.btnLimpar.setFont(font1)

        self.horizontalLayout.addWidget(self.btnLimpar)

        self.btnSalvar = QPushButton(self.widget_2)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setFont(font1)

        self.horizontalLayout.addWidget(self.btnSalvar)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.mainLayout.addWidget(self.frameNovoReg)

        self.frameHistorico = QFrame(RegForm)
        self.frameHistorico.setObjectName(u"frameHistorico")
        self.frameHistorico.setFrameShape(QFrame.StyledPanel)
        self.frameHistorico.setFrameShadow(QFrame.Raised)

        self.mainLayout.addWidget(self.frameHistorico)


        self.retranslateUi(RegForm)

        QMetaObject.connectSlotsByName(RegForm)
    # setupUi

    def retranslateUi(self, RegForm):
        RegForm.setWindowTitle(QCoreApplication.translate("RegForm", u"Form", None))
        self.lbTitleReg.setText(QCoreApplication.translate("RegForm", u"Novo Registro", None))
        self.label_2.setText(QCoreApplication.translate("RegForm", u"T\u00edtulo", None))
        self.label_11.setText(QCoreApplication.translate("RegForm", u"Contabilizado", None))
        self.cbContab.setItemText(0, QCoreApplication.translate("RegForm", u"Pendente", None))
        self.cbContab.setItemText(1, QCoreApplication.translate("RegForm", u"Contabilizado", None))

        self.label_12.setText(QCoreApplication.translate("RegForm", u"Descri\u00e7\u00e3o", None))
        self.label_13.setText(QCoreApplication.translate("RegForm", u"Valor", None))
        self.label_14.setText(QCoreApplication.translate("RegForm", u"Data", None))
        self.lbTitleOp.setText(QCoreApplication.translate("RegForm", u"Detalhes da Opera\u00e7\u00e3o", None))
        self.label_16.setText(QCoreApplication.translate("RegForm", u"Tipo de Opera\u00e7\u00e3o", None))
        self.label_15.setText(QCoreApplication.translate("RegForm", u"Categoria", None))
        self.btnLimpar.setText(QCoreApplication.translate("RegForm", u"limpar", None))
        self.btnSalvar.setText(QCoreApplication.translate("RegForm", u"salvar", None))
    # retranslateUi

