# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_ConfigForm(object):
    def setupUi(self, ConfigForm):
        if not ConfigForm.objectName():
            ConfigForm.setObjectName(u"ConfigForm")
        ConfigForm.resize(743, 700)
        self.verticalLayout_13 = QVBoxLayout(ConfigForm)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(ConfigForm)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 741, 698))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #5E5E5E;")

        self.verticalLayout_8.addWidget(self.label_5)

        self.widSenhaAtual = QWidget(self.frame_2)
        self.widSenhaAtual.setObjectName(u"widSenhaAtual")
        self.widSenhaAtual.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.widSenhaAtual)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.widSenhaAtual)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.leSenhaAtual = QLineEdit(self.widSenhaAtual)
        self.leSenhaAtual.setObjectName(u"leSenhaAtual")

        self.verticalLayout_4.addWidget(self.leSenhaAtual)


        self.verticalLayout_8.addWidget(self.widSenhaAtual)

        self.widSenhaNova = QWidget(self.frame_2)
        self.widSenhaNova.setObjectName(u"widSenhaNova")
        self.widSenhaNova.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.widSenhaNova)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.widSenhaNova)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.leSenhaNova = QLineEdit(self.widSenhaNova)
        self.leSenhaNova.setObjectName(u"leSenhaNova")

        self.verticalLayout_5.addWidget(self.leSenhaNova)


        self.verticalLayout_8.addWidget(self.widSenhaNova)

        self.widSenhaConfirm = QWidget(self.frame_2)
        self.widSenhaConfirm.setObjectName(u"widSenhaConfirm")
        self.widSenhaConfirm.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.widSenhaConfirm)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.label_8 = QLabel(self.widSenhaConfirm)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_6.addWidget(self.label_8)

        self.leSenhaConfirm = QLineEdit(self.widSenhaConfirm)
        self.leSenhaConfirm.setObjectName(u"leSenhaConfirm")

        self.verticalLayout_6.addWidget(self.leSenhaConfirm)


        self.verticalLayout_8.addWidget(self.widSenhaConfirm)

        self.widget_6 = QWidget(self.frame_2)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnCancelarSenha = QPushButton(self.widget_6)
        self.btnCancelarSenha.setObjectName(u"btnCancelarSenha")
        self.btnCancelarSenha.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnCancelarSenha)

        self.btnSalvarSenha = QPushButton(self.widget_6)
        self.btnSalvarSenha.setObjectName(u"btnSalvarSenha")
        self.btnSalvarSenha.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnSalvarSenha)

        self.btnAtualizarSenha = QPushButton(self.widget_6)
        self.btnAtualizarSenha.setObjectName(u"btnAtualizarSenha")
        self.btnAtualizarSenha.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnAtualizarSenha)


        self.verticalLayout_8.addWidget(self.widget_6)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_8 = QWidget(self.frame_4)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: #5E5E5E;")
        self.label_9.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.horizontalSpacer_5 = QSpacerItem(49, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btnAceitarShare = QPushButton(self.widget_8)
        self.btnAceitarShare.setObjectName(u"btnAceitarShare")
        icon = QIcon()
        icon.addFile(u":/root/icons/Vector.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAceitarShare.setIcon(icon)
        self.btnAceitarShare.setIconSize(QSize(20, 20))
        self.btnAceitarShare.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btnAceitarShare)

        self.btnCancelarShare = QPushButton(self.widget_8)
        self.btnCancelarShare.setObjectName(u"btnCancelarShare")
        icon1 = QIcon()
        icon1.addFile(u":/root/icons/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancelarShare.setIcon(icon1)
        self.btnCancelarShare.setIconSize(QSize(20, 20))
        self.btnCancelarShare.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btnCancelarShare)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.tableShare = QTableWidget(self.frame_4)
        self.tableShare.setObjectName(u"tableShare")

        self.verticalLayout_2.addWidget(self.tableShare)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_7 = QWidget(self.frame_3)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #5E5E5E;")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(225, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btnDelPerfil = QPushButton(self.widget_7)
        self.btnDelPerfil.setObjectName(u"btnDelPerfil")
        icon2 = QIcon()
        icon2.addFile(u":/root/icons/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelPerfil.setIcon(icon2)
        self.btnDelPerfil.setIconSize(QSize(20, 20))
        self.btnDelPerfil.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnDelPerfil)

        self.btnAddPerfil = QPushButton(self.widget_7)
        self.btnAddPerfil.setObjectName(u"btnAddPerfil")
        icon3 = QIcon()
        icon3.addFile(u":/root/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddPerfil.setIcon(icon3)
        self.btnAddPerfil.setIconSize(QSize(20, 20))
        self.btnAddPerfil.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnAddPerfil)


        self.verticalLayout_9.addWidget(self.widget_7)

        self.tablePerfis = QTableWidget(self.frame_3)
        self.tablePerfis.setObjectName(u"tablePerfis")

        self.verticalLayout_9.addWidget(self.tablePerfis)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #5E5E5E;")

        self.verticalLayout_7.addWidget(self.label)

        self.widNome = QWidget(self.frame)
        self.widNome.setObjectName(u"widNome")
        self.widNome.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widNome)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.widNome)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.leNome = QLineEdit(self.widNome)
        self.leNome.setObjectName(u"leNome")

        self.verticalLayout.addWidget(self.leNome)


        self.verticalLayout_7.addWidget(self.widNome)

        self.widEmail = QWidget(self.frame)
        self.widEmail.setObjectName(u"widEmail")
        self.widEmail.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.widEmail)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.widEmail)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.leEmail = QLineEdit(self.widEmail)
        self.leEmail.setObjectName(u"leEmail")

        self.verticalLayout_3.addWidget(self.leEmail)


        self.verticalLayout_7.addWidget(self.widEmail)

        self.widget_17 = QWidget(self.frame)
        self.widget_17.setObjectName(u"widget_17")

        self.verticalLayout_7.addWidget(self.widget_17)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCancelarUser = QPushButton(self.widget)
        self.btnCancelarUser.setObjectName(u"btnCancelarUser")
        self.btnCancelarUser.setFont(font)

        self.horizontalLayout.addWidget(self.btnCancelarUser)

        self.btnSalvarUser = QPushButton(self.widget)
        self.btnSalvarUser.setObjectName(u"btnSalvarUser")
        self.btnSalvarUser.setFont(font)

        self.horizontalLayout.addWidget(self.btnSalvarUser)

        self.btnEditarUser = QPushButton(self.widget)
        self.btnEditarUser.setObjectName(u"btnEditarUser")
        self.btnEditarUser.setFont(font)

        self.horizontalLayout.addWidget(self.btnEditarUser)


        self.verticalLayout_7.addWidget(self.widget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_15 = QWidget(self.frame_5)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: #5E5E5E;")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.horizontalSpacer_7 = QSpacerItem(529, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.cbPerfil = QComboBox(self.widget_15)
        self.cbPerfil.setObjectName(u"cbPerfil")

        self.horizontalLayout_7.addWidget(self.cbPerfil)


        self.verticalLayout_12.addWidget(self.widget_15)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.widget_16 = QWidget(self.frame_5)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.widget_16)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_9 = QWidget(self.frame_6)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: #5E5E5E;")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.horizontalSpacer_3 = QSpacerItem(208, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btnDelEdicao = QPushButton(self.widget_9)
        self.btnDelEdicao.setObjectName(u"btnDelEdicao")
        self.btnDelEdicao.setIcon(icon2)
        self.btnDelEdicao.setIconSize(QSize(20, 20))
        self.btnDelEdicao.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btnDelEdicao)

        self.pushButton_12 = QPushButton(self.widget_9)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QSize(20, 20))
        self.pushButton_12.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_12)


        self.verticalLayout_10.addWidget(self.widget_9)

        self.tableEdicao = QTableWidget(self.frame_6)
        self.tableEdicao.setObjectName(u"tableEdicao")

        self.verticalLayout_10.addWidget(self.tableEdicao)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.widget_16)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_10 = QWidget(self.frame_7)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: #5E5E5E;")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.horizontalSpacer_6 = QSpacerItem(167, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.btnDelVisu = QPushButton(self.widget_10)
        self.btnDelVisu.setObjectName(u"btnDelVisu")
        self.btnDelVisu.setIcon(icon2)
        self.btnDelVisu.setIconSize(QSize(20, 20))
        self.btnDelVisu.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnDelVisu)

        self.btnAddVisu = QPushButton(self.widget_10)
        self.btnAddVisu.setObjectName(u"btnAddVisu")
        self.btnAddVisu.setIcon(icon3)
        self.btnAddVisu.setIconSize(QSize(20, 20))
        self.btnAddVisu.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnAddVisu)


        self.verticalLayout_11.addWidget(self.widget_10)

        self.tableVisu = QTableWidget(self.frame_7)
        self.tableVisu.setObjectName(u"tableVisu")

        self.verticalLayout_11.addWidget(self.tableVisu)


        self.horizontalLayout_8.addWidget(self.frame_7)


        self.verticalLayout_12.addWidget(self.widget_16)


        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.leNome, self.leEmail)
        QWidget.setTabOrder(self.leEmail, self.btnCancelarUser)
        QWidget.setTabOrder(self.btnCancelarUser, self.btnSalvarUser)
        QWidget.setTabOrder(self.btnSalvarUser, self.btnEditarUser)
        QWidget.setTabOrder(self.btnEditarUser, self.leSenhaAtual)
        QWidget.setTabOrder(self.leSenhaAtual, self.leSenhaNova)
        QWidget.setTabOrder(self.leSenhaNova, self.leSenhaConfirm)
        QWidget.setTabOrder(self.leSenhaConfirm, self.btnCancelarSenha)
        QWidget.setTabOrder(self.btnCancelarSenha, self.btnSalvarSenha)
        QWidget.setTabOrder(self.btnSalvarSenha, self.btnAtualizarSenha)
        QWidget.setTabOrder(self.btnAtualizarSenha, self.btnDelPerfil)
        QWidget.setTabOrder(self.btnDelPerfil, self.btnAddPerfil)
        QWidget.setTabOrder(self.btnAddPerfil, self.btnAceitarShare)
        QWidget.setTabOrder(self.btnAceitarShare, self.btnCancelarShare)
        QWidget.setTabOrder(self.btnCancelarShare, self.cbPerfil)
        QWidget.setTabOrder(self.cbPerfil, self.btnDelEdicao)
        QWidget.setTabOrder(self.btnDelEdicao, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.btnDelVisu)
        QWidget.setTabOrder(self.btnDelVisu, self.btnAddVisu)
        QWidget.setTabOrder(self.btnAddVisu, self.scrollArea)

        self.retranslateUi(ConfigForm)

        QMetaObject.connectSlotsByName(ConfigForm)
    # setupUi

    def retranslateUi(self, ConfigForm):
        ConfigForm.setWindowTitle(QCoreApplication.translate("ConfigForm", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("ConfigForm", u"Senha de usu\u00e1rio", None))
        self.label_6.setText(QCoreApplication.translate("ConfigForm", u"Senha Atual", None))
        self.label_7.setText(QCoreApplication.translate("ConfigForm", u"Nova Senha", None))
        self.label_8.setText(QCoreApplication.translate("ConfigForm", u"Confirmar Senha", None))
        self.btnCancelarSenha.setText(QCoreApplication.translate("ConfigForm", u"cancelar", None))
        self.btnSalvarSenha.setText(QCoreApplication.translate("ConfigForm", u"salvar", None))
        self.btnAtualizarSenha.setText(QCoreApplication.translate("ConfigForm", u"atualizar", None))
        self.label_9.setText(QCoreApplication.translate("ConfigForm", u"Compartilhamentos Pendentes", None))
        self.label_3.setText(QCoreApplication.translate("ConfigForm", u"Perfis", None))
        self.label.setText(QCoreApplication.translate("ConfigForm", u"Dados de usu\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("ConfigForm", u"Nome", None))
        self.label_4.setText(QCoreApplication.translate("ConfigForm", u"Email", None))
        self.btnCancelarUser.setText(QCoreApplication.translate("ConfigForm", u"cancelar", None))
        self.btnSalvarUser.setText(QCoreApplication.translate("ConfigForm", u"salvar", None))
        self.btnEditarUser.setText(QCoreApplication.translate("ConfigForm", u"editar", None))
        self.label_10.setText(QCoreApplication.translate("ConfigForm", u"Acesso ao Perfil", None))
        self.label_11.setText(QCoreApplication.translate("ConfigForm", u"Edi\u00e7\u00e3o", None))
        self.label_12.setText(QCoreApplication.translate("ConfigForm", u"Visualiza\u00e7\u00e3o", None))
    # retranslateUi

