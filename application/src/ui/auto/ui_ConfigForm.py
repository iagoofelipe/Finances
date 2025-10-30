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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from . import resource_rc

class Ui_ConfigForm(object):
    def setupUi(self, ConfigForm):
        if not ConfigForm.objectName():
            ConfigForm.setObjectName(u"ConfigForm")
        ConfigForm.resize(743, 699)
        self.verticalLayout_13 = QVBoxLayout(ConfigForm)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(ConfigForm)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 741, 697))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(10)
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
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.lbSenhaUsuario = QLabel(self.frame_2)
        self.lbSenhaUsuario.setObjectName(u"lbSenhaUsuario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbSenhaUsuario.sizePolicy().hasHeightForWidth())
        self.lbSenhaUsuario.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.lbSenhaUsuario.setFont(font)

        self.verticalLayout_8.addWidget(self.lbSenhaUsuario)

        self.widSenhaAtual = QWidget(self.frame_2)
        self.widSenhaAtual.setObjectName(u"widSenhaAtual")
        self.widSenhaAtual.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.widSenhaAtual)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.widSenhaAtual)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.label_6.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_6)

        self.widget_2 = QWidget(self.widSenhaAtual)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leSenhaAtual = QLineEdit(self.widget_2)
        self.leSenhaAtual.setObjectName(u"leSenhaAtual")
        self.leSenhaAtual.setFont(font1)
        self.leSenhaAtual.setEchoMode(QLineEdit.Password)
        self.leSenhaAtual.setDragEnabled(False)
        self.leSenhaAtual.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.leSenhaAtual)

        self.btnSenhaAtualHide = QPushButton(self.widget_2)
        self.btnSenhaAtualHide.setObjectName(u"btnSenhaAtualHide")
        self.btnSenhaAtualHide.setFont(font)
        self.btnSenhaAtualHide.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/root/icons/light_eye-off.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSenhaAtualHide.setIcon(icon)
        self.btnSenhaAtualHide.setIconSize(QSize(18, 18))
        self.btnSenhaAtualHide.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnSenhaAtualHide)

        self.btnSenhaAtualShow = QPushButton(self.widget_2)
        self.btnSenhaAtualShow.setObjectName(u"btnSenhaAtualShow")
        self.btnSenhaAtualShow.setFont(font)
        self.btnSenhaAtualShow.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/root/icons/light_eye.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSenhaAtualShow.setIcon(icon1)
        self.btnSenhaAtualShow.setIconSize(QSize(18, 18))
        self.btnSenhaAtualShow.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnSenhaAtualShow)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_8.addWidget(self.widSenhaAtual)

        self.widSenhaNova = QWidget(self.frame_2)
        self.widSenhaNova.setObjectName(u"widSenhaNova")
        self.widSenhaNova.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.widSenhaNova)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.widSenhaNova)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_7)

        self.widget_3 = QWidget(self.widSenhaNova)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leSenhaNova = QLineEdit(self.widget_3)
        self.leSenhaNova.setObjectName(u"leSenhaNova")
        self.leSenhaNova.setFont(font1)
        self.leSenhaNova.setEchoMode(QLineEdit.Password)
        self.leSenhaNova.setDragEnabled(False)
        self.leSenhaNova.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.leSenhaNova)

        self.btnSenhaNovaHide = QPushButton(self.widget_3)
        self.btnSenhaNovaHide.setObjectName(u"btnSenhaNovaHide")
        font2 = QFont()
        font2.setPointSize(12)
        self.btnSenhaNovaHide.setFont(font2)
        self.btnSenhaNovaHide.setStyleSheet(u"background-color: transparent;")
        self.btnSenhaNovaHide.setIcon(icon)
        self.btnSenhaNovaHide.setIconSize(QSize(18, 18))
        self.btnSenhaNovaHide.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btnSenhaNovaHide)

        self.btnSenhaNovaShow = QPushButton(self.widget_3)
        self.btnSenhaNovaShow.setObjectName(u"btnSenhaNovaShow")
        self.btnSenhaNovaShow.setFont(font2)
        self.btnSenhaNovaShow.setStyleSheet(u"background-color: transparent;")
        self.btnSenhaNovaShow.setIcon(icon1)
        self.btnSenhaNovaShow.setIconSize(QSize(18, 18))
        self.btnSenhaNovaShow.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btnSenhaNovaShow)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_8.addWidget(self.widSenhaNova)

        self.widSenhaConfirm = QWidget(self.frame_2)
        self.widSenhaConfirm.setObjectName(u"widSenhaConfirm")
        self.widSenhaConfirm.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.widSenhaConfirm)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.label_8 = QLabel(self.widSenhaConfirm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_8)

        self.widget_4 = QWidget(self.widSenhaConfirm)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leSenhaConfirm = QLineEdit(self.widget_4)
        self.leSenhaConfirm.setObjectName(u"leSenhaConfirm")
        self.leSenhaConfirm.setFont(font1)
        self.leSenhaConfirm.setEchoMode(QLineEdit.Password)
        self.leSenhaConfirm.setDragEnabled(False)
        self.leSenhaConfirm.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.leSenhaConfirm)

        self.btnSenhaConfirmHide = QPushButton(self.widget_4)
        self.btnSenhaConfirmHide.setObjectName(u"btnSenhaConfirmHide")
        self.btnSenhaConfirmHide.setFont(font)
        self.btnSenhaConfirmHide.setStyleSheet(u"background-color: transparent;")
        self.btnSenhaConfirmHide.setIcon(icon)
        self.btnSenhaConfirmHide.setIconSize(QSize(18, 18))
        self.btnSenhaConfirmHide.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnSenhaConfirmHide)

        self.btnSenhaConfirmShow = QPushButton(self.widget_4)
        self.btnSenhaConfirmShow.setObjectName(u"btnSenhaConfirmShow")
        self.btnSenhaConfirmShow.setFont(font)
        self.btnSenhaConfirmShow.setStyleSheet(u"background-color: transparent;")
        self.btnSenhaConfirmShow.setIcon(icon1)
        self.btnSenhaConfirmShow.setIconSize(QSize(18, 18))
        self.btnSenhaConfirmShow.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnSenhaConfirmShow)


        self.verticalLayout_5.addWidget(self.widget_4)


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

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.lbDadosUsuario = QLabel(self.frame)
        self.lbDadosUsuario.setObjectName(u"lbDadosUsuario")
        sizePolicy1.setHeightForWidth(self.lbDadosUsuario.sizePolicy().hasHeightForWidth())
        self.lbDadosUsuario.setSizePolicy(sizePolicy1)
        self.lbDadosUsuario.setFont(font)

        self.verticalLayout_7.addWidget(self.lbDadosUsuario)

        self.widNome = QWidget(self.frame)
        self.widNome.setObjectName(u"widNome")
        self.widNome.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widNome)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.widNome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.leNome = QLineEdit(self.widNome)
        self.leNome.setObjectName(u"leNome")
        self.leNome.setFont(font1)

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
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.leEmail = QLineEdit(self.widEmail)
        self.leEmail.setObjectName(u"leEmail")
        self.leEmail.setFont(font1)

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
        self.lbTerceiros = QLabel(self.widget_15)
        self.lbTerceiros.setObjectName(u"lbTerceiros")
        self.lbTerceiros.setFont(font)

        self.horizontalLayout_7.addWidget(self.lbTerceiros)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.cbPerfil = QComboBox(self.widget_15)
        self.cbPerfil.setObjectName(u"cbPerfil")
        self.cbPerfil.setFont(font)

        self.horizontalLayout_7.addWidget(self.cbPerfil)


        self.verticalLayout_12.addWidget(self.widget_15)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.widget_16 = QWidget(self.frame_5)
        self.widget_16.setObjectName(u"widget_16")
        self.acessoPerfilLayout = QHBoxLayout(self.widget_16)
        self.acessoPerfilLayout.setObjectName(u"acessoPerfilLayout")
        self.acessoPerfilLayout.setContentsMargins(0, 0, 0, 0)
        self.widEdicao = QWidget(self.widget_16)
        self.widEdicao.setObjectName(u"widEdicao")
        self.widEdicao.setMinimumSize(QSize(0, 0))

        self.acessoPerfilLayout.addWidget(self.widEdicao)

        self.widVisu = QWidget(self.widget_16)
        self.widVisu.setObjectName(u"widVisu")
        self.widVisu.setMinimumSize(QSize(0, 0))

        self.acessoPerfilLayout.addWidget(self.widVisu)

        self.acessoPerfilLayout.setStretch(0, 1)
        self.acessoPerfilLayout.setStretch(1, 1)

        self.verticalLayout_12.addWidget(self.widget_16)


        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 2)

        self.widPerfis = QWidget(self.scrollAreaWidgetContents)
        self.widPerfis.setObjectName(u"widPerfis")
        self.widPerfis.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.widPerfis, 1, 0, 1, 1)

        self.widShare = QWidget(self.scrollAreaWidgetContents)
        self.widShare.setObjectName(u"widShare")
        self.widShare.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.widShare, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.leNome, self.leEmail)
        QWidget.setTabOrder(self.leEmail, self.btnCancelarUser)
        QWidget.setTabOrder(self.btnCancelarUser, self.btnSalvarUser)
        QWidget.setTabOrder(self.btnSalvarUser, self.btnEditarUser)
        QWidget.setTabOrder(self.btnEditarUser, self.btnCancelarSenha)
        QWidget.setTabOrder(self.btnCancelarSenha, self.btnSalvarSenha)
        QWidget.setTabOrder(self.btnSalvarSenha, self.btnAtualizarSenha)
        QWidget.setTabOrder(self.btnAtualizarSenha, self.cbPerfil)
        QWidget.setTabOrder(self.cbPerfil, self.scrollArea)

        self.retranslateUi(ConfigForm)

        QMetaObject.connectSlotsByName(ConfigForm)
    # setupUi

    def retranslateUi(self, ConfigForm):
        ConfigForm.setWindowTitle(QCoreApplication.translate("ConfigForm", u"Form", None))
        self.lbSenhaUsuario.setText(QCoreApplication.translate("ConfigForm", u"Senha de usu\u00e1rio", None))
        self.label_6.setText(QCoreApplication.translate("ConfigForm", u"Senha Atual", None))
        self.btnSenhaAtualHide.setText("")
        self.btnSenhaAtualShow.setText("")
        self.label_7.setText(QCoreApplication.translate("ConfigForm", u"Nova Senha", None))
        self.btnSenhaNovaHide.setText("")
        self.btnSenhaNovaShow.setText("")
        self.label_8.setText(QCoreApplication.translate("ConfigForm", u"Confirmar Senha", None))
        self.btnSenhaConfirmHide.setText("")
        self.btnSenhaConfirmShow.setText("")
        self.btnCancelarSenha.setText(QCoreApplication.translate("ConfigForm", u"cancelar", None))
        self.btnSalvarSenha.setText(QCoreApplication.translate("ConfigForm", u"salvar", None))
        self.btnAtualizarSenha.setText(QCoreApplication.translate("ConfigForm", u"atualizar", None))
        self.lbDadosUsuario.setText(QCoreApplication.translate("ConfigForm", u"Dados de usu\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("ConfigForm", u"Nome", None))
        self.label_4.setText(QCoreApplication.translate("ConfigForm", u"Email", None))
        self.btnCancelarUser.setText(QCoreApplication.translate("ConfigForm", u"cancelar", None))
        self.btnSalvarUser.setText(QCoreApplication.translate("ConfigForm", u"salvar", None))
        self.btnEditarUser.setText(QCoreApplication.translate("ConfigForm", u"editar", None))
        self.lbTerceiros.setText(QCoreApplication.translate("ConfigForm", u"Acessos de Terceiros", None))
    # retranslateUi

