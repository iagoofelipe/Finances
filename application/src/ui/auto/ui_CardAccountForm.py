# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardAccountForm.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_CardAccountForm(object):
    def setupUi(self, CardAccountForm):
        if not CardAccountForm.objectName():
            CardAccountForm.setObjectName(u"CardAccountForm")
        CardAccountForm.resize(899, 728)
        self.gridLayout = QGridLayout(CardAccountForm)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CardAccountForm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.lbNovoCartao = QLabel(self.frame)
        self.lbNovoCartao.setObjectName(u"lbNovoCartao")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.lbNovoCartao.setFont(font)

        self.verticalLayout_4.addWidget(self.lbNovoCartao)

        self.widNomeCartao = QWidget(self.frame)
        self.widNomeCartao.setObjectName(u"widNomeCartao")
        self.verticalLayout = QVBoxLayout(self.widNomeCartao)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.widNomeCartao)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.leNomeCartao = QLineEdit(self.widNomeCartao)
        self.leNomeCartao.setObjectName(u"leNomeCartao")
        self.leNomeCartao.setFont(font1)

        self.verticalLayout.addWidget(self.leNomeCartao)


        self.verticalLayout_4.addWidget(self.widNomeCartao)

        self.widVencimento = QWidget(self.frame)
        self.widVencimento.setObjectName(u"widVencimento")
        self.verticalLayout_2 = QVBoxLayout(self.widVencimento)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.widVencimento)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.sbVencimento = QSpinBox(self.widVencimento)
        self.sbVencimento.setObjectName(u"sbVencimento")
        self.sbVencimento.setFont(font1)
        self.sbVencimento.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbVencimento.setMinimum(1)
        self.sbVencimento.setMaximum(31)

        self.verticalLayout_2.addWidget(self.sbVencimento)


        self.verticalLayout_4.addWidget(self.widVencimento)

        self.widLimite = QWidget(self.frame)
        self.widLimite.setObjectName(u"widLimite")
        self.verticalLayout_3 = QVBoxLayout(self.widLimite)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.widLimite)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.sbLimite = QSpinBox(self.widLimite)
        self.sbLimite.setObjectName(u"sbLimite")
        self.sbLimite.setFont(font1)
        self.sbLimite.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbLimite.setMaximum(99999)

        self.verticalLayout_3.addWidget(self.sbLimite)


        self.verticalLayout_4.addWidget(self.widLimite)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnLimparCartao = QPushButton(self.widget)
        self.btnLimparCartao.setObjectName(u"btnLimparCartao")
        self.btnLimparCartao.setFont(font1)

        self.horizontalLayout.addWidget(self.btnLimparCartao)

        self.btnSalvarCartao = QPushButton(self.widget)
        self.btnSalvarCartao.setObjectName(u"btnSalvarCartao")
        self.btnSalvarCartao.setFont(font1)

        self.horizontalLayout.addWidget(self.btnSalvarCartao)


        self.verticalLayout_4.addWidget(self.widget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frameCartoes = QFrame(CardAccountForm)
        self.frameCartoes.setObjectName(u"frameCartoes")
        self.frameCartoes.setFrameShape(QFrame.StyledPanel)
        self.frameCartoes.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frameCartoes, 0, 1, 1, 1)

        self.frame_2 = QFrame(CardAccountForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.lbNovaConta = QLabel(self.frame_2)
        self.lbNovaConta.setObjectName(u"lbNovaConta")
        self.lbNovaConta.setFont(font)

        self.verticalLayout_5.addWidget(self.lbNovaConta)

        self.widNomeConta = QWidget(self.frame_2)
        self.widNomeConta.setObjectName(u"widNomeConta")
        self.verticalLayout_6 = QVBoxLayout(self.widNomeConta)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.widNomeConta)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_5)

        self.leNomeConta = QLineEdit(self.widNomeConta)
        self.leNomeConta.setObjectName(u"leNomeConta")
        self.leNomeConta.setFont(font1)

        self.verticalLayout_6.addWidget(self.leNomeConta)


        self.verticalLayout_5.addWidget(self.widNomeConta)

        self.widInicial = QWidget(self.frame_2)
        self.widInicial.setObjectName(u"widInicial")
        self.verticalLayout_7 = QVBoxLayout(self.widInicial)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.widInicial)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_6)

        self.sbInicial = QSpinBox(self.widInicial)
        self.sbInicial.setObjectName(u"sbInicial")
        self.sbInicial.setFont(font1)
        self.sbInicial.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbInicial.setMinimum(0)
        self.sbInicial.setMaximum(99999)

        self.verticalLayout_7.addWidget(self.sbInicial)


        self.verticalLayout_5.addWidget(self.widInicial)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnLimparConta = QPushButton(self.widget_2)
        self.btnLimparConta.setObjectName(u"btnLimparConta")
        self.btnLimparConta.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btnLimparConta)

        self.btnSalvarConta = QPushButton(self.widget_2)
        self.btnSalvarConta.setObjectName(u"btnSalvarConta")
        self.btnSalvarConta.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btnSalvarConta)


        self.verticalLayout_5.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frameContas = QFrame(CardAccountForm)
        self.frameContas.setObjectName(u"frameContas")
        self.frameContas.setFrameShape(QFrame.StyledPanel)
        self.frameContas.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frameContas, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 300)

        self.retranslateUi(CardAccountForm)

        QMetaObject.connectSlotsByName(CardAccountForm)
    # setupUi

    def retranslateUi(self, CardAccountForm):
        CardAccountForm.setWindowTitle(QCoreApplication.translate("CardAccountForm", u"Form", None))
        self.lbNovoCartao.setText(QCoreApplication.translate("CardAccountForm", u"Novo Cart\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("CardAccountForm", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("CardAccountForm", u"Dia de Vencimento", None))
        self.label_4.setText(QCoreApplication.translate("CardAccountForm", u"Limite", None))
        self.btnLimparCartao.setText(QCoreApplication.translate("CardAccountForm", u"limpar", None))
        self.btnSalvarCartao.setText(QCoreApplication.translate("CardAccountForm", u"salvar", None))
        self.lbNovaConta.setText(QCoreApplication.translate("CardAccountForm", u"Nova Conta", None))
        self.label_5.setText(QCoreApplication.translate("CardAccountForm", u"Nome", None))
        self.label_6.setText(QCoreApplication.translate("CardAccountForm", u"Saldo Inicial", None))
        self.btnLimparConta.setText(QCoreApplication.translate("CardAccountForm", u"limpar", None))
        self.btnSalvarConta.setText(QCoreApplication.translate("CardAccountForm", u"salvar", None))
    # retranslateUi

