# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateAccountForm.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CreateAccountForm(object):
    def setupUi(self, CreateAccountForm):
        if not CreateAccountForm.objectName():
            CreateAccountForm.setObjectName(u"CreateAccountForm")
        CreateAccountForm.resize(427, 437)
        CreateAccountForm.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(CreateAccountForm)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widUser = QWidget(CreateAccountForm)
        self.widUser.setObjectName(u"widUser")
        self.widUser.setMinimumSize(QSize(0, 0))
        self.widUser.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widUser)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.lbUser = QLabel(self.widUser)
        self.lbUser.setObjectName(u"lbUser")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        self.lbUser.setFont(font)

        self.verticalLayout_3.addWidget(self.lbUser)

        self.leUsername = QLineEdit(self.widUser)
        self.leUsername.setObjectName(u"leUsername")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.leUsername.setFont(font1)

        self.verticalLayout_3.addWidget(self.leUsername)


        self.verticalLayout.addWidget(self.widUser)

        self.widNome = QWidget(CreateAccountForm)
        self.widNome.setObjectName(u"widNome")
        self.verticalLayout_4 = QVBoxLayout(self.widNome)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.lbName = QLabel(self.widNome)
        self.lbName.setObjectName(u"lbName")
        self.lbName.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbName)

        self.leName = QLineEdit(self.widNome)
        self.leName.setObjectName(u"leName")
        self.leName.setFont(font1)

        self.verticalLayout_4.addWidget(self.leName)


        self.verticalLayout.addWidget(self.widNome)

        self.widEmail = QWidget(CreateAccountForm)
        self.widEmail.setObjectName(u"widEmail")
        self.verticalLayout_5 = QVBoxLayout(self.widEmail)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.lbEmail = QLabel(self.widEmail)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setFont(font1)

        self.verticalLayout_5.addWidget(self.lbEmail)

        self.leEmail = QLineEdit(self.widEmail)
        self.leEmail.setObjectName(u"leEmail")
        self.leEmail.setFont(font1)

        self.verticalLayout_5.addWidget(self.leEmail)


        self.verticalLayout.addWidget(self.widEmail)

        self.widPass = QWidget(CreateAccountForm)
        self.widPass.setObjectName(u"widPass")
        self.verticalLayout_6 = QVBoxLayout(self.widPass)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.lbPass = QLabel(self.widPass)
        self.lbPass.setObjectName(u"lbPass")
        self.lbPass.setFont(font1)

        self.verticalLayout_6.addWidget(self.lbPass)

        self.lePassword = QLineEdit(self.widPass)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setFont(font1)
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.lePassword)


        self.verticalLayout.addWidget(self.widPass)

        self.widPassConfirm = QWidget(CreateAccountForm)
        self.widPassConfirm.setObjectName(u"widPassConfirm")
        self.verticalLayout_7 = QVBoxLayout(self.widPassConfirm)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.lbPassConfirm = QLabel(self.widPassConfirm)
        self.lbPassConfirm.setObjectName(u"lbPassConfirm")
        self.lbPassConfirm.setFont(font1)

        self.verticalLayout_7.addWidget(self.lbPassConfirm)

        self.lePassConfirm = QLineEdit(self.widPassConfirm)
        self.lePassConfirm.setObjectName(u"lePassConfirm")
        self.lePassConfirm.setFont(font1)
        self.lePassConfirm.setEchoMode(QLineEdit.Password)

        self.verticalLayout_7.addWidget(self.lePassConfirm)


        self.verticalLayout.addWidget(self.widPassConfirm)

        self.widget = QWidget(CreateAccountForm)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnVoltar = QPushButton(self.widget)
        self.btnVoltar.setObjectName(u"btnVoltar")
        self.btnVoltar.setFont(font1)

        self.horizontalLayout.addWidget(self.btnVoltar)

        self.btnSalvar = QPushButton(self.widget)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setFont(font1)

        self.horizontalLayout.addWidget(self.btnSalvar)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(CreateAccountForm)

        QMetaObject.connectSlotsByName(CreateAccountForm)
    # setupUi

    def retranslateUi(self, CreateAccountForm):
        CreateAccountForm.setWindowTitle(QCoreApplication.translate("CreateAccountForm", u"Form", None))
        self.lbUser.setText(QCoreApplication.translate("CreateAccountForm", u"Usu\u00e1rio", None))
        self.lbName.setText(QCoreApplication.translate("CreateAccountForm", u"Nome", None))
        self.lbEmail.setText(QCoreApplication.translate("CreateAccountForm", u"E-mail", None))
        self.lbPass.setText(QCoreApplication.translate("CreateAccountForm", u"Senha", None))
        self.lbPassConfirm.setText(QCoreApplication.translate("CreateAccountForm", u"Confirmar senha", None))
        self.btnVoltar.setText(QCoreApplication.translate("CreateAccountForm", u"voltar", None))
        self.btnSalvar.setText(QCoreApplication.translate("CreateAccountForm", u"salvar", None))
    # retranslateUi

