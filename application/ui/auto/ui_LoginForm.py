# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(400, 312)
        LoginForm.setMinimumSize(QSize(400, 0))
        self.verticalLayout_5 = QVBoxLayout(LoginForm)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widUser = QWidget(LoginForm)
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


        self.verticalLayout_5.addWidget(self.widUser)

        self.widPass = QWidget(LoginForm)
        self.widPass.setObjectName(u"widPass")
        self.verticalLayout_4 = QVBoxLayout(self.widPass)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbPass = QLabel(self.widPass)
        self.lbPass.setObjectName(u"lbPass")
        self.lbPass.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbPass)

        self.lePassword = QLineEdit(self.widPass)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setFont(font1)
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.lePassword)


        self.verticalLayout_5.addWidget(self.widPass)

        self.widLembrar = QWidget(LoginForm)
        self.widLembrar.setObjectName(u"widLembrar")
        self.horizontalLayout_5 = QHBoxLayout(self.widLembrar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.cbLembrar = QCheckBox(self.widLembrar)
        self.cbLembrar.setObjectName(u"cbLembrar")
        self.cbLembrar.setFont(font1)
        self.cbLembrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.cbLembrar)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addWidget(self.widLembrar)

        self.btnAcessar = QPushButton(LoginForm)
        self.btnAcessar.setObjectName(u"btnAcessar")
        self.btnAcessar.setFont(font)
        self.btnAcessar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAcessar.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btnAcessar)

        self.widCriarConta = QWidget(LoginForm)
        self.widCriarConta.setObjectName(u"widCriarConta")
        self.horizontalLayout_3 = QHBoxLayout(self.widCriarConta)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.label_8 = QLabel(self.widCriarConta)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.btnCriar = QPushButton(self.widCriarConta)
        self.btnCriar.setObjectName(u"btnCriar")
        self.btnCriar.setFont(font1)
        self.btnCriar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCriar.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnCriar)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addWidget(self.widCriarConta)

        self.btnEsqueci = QPushButton(LoginForm)
        self.btnEsqueci.setObjectName(u"btnEsqueci")
        self.btnEsqueci.setFont(font1)
        self.btnEsqueci.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEsqueci.setFlat(True)

        self.verticalLayout_5.addWidget(self.btnEsqueci)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.lbUser.setText(QCoreApplication.translate("LoginForm", u"Usu\u00e1rio", None))
        self.lbPass.setText(QCoreApplication.translate("LoginForm", u"Senha", None))
        self.cbLembrar.setText(QCoreApplication.translate("LoginForm", u"lembrar neste dispositivo", None))
        self.btnAcessar.setText(QCoreApplication.translate("LoginForm", u"acessar", None))
        self.label_8.setText(QCoreApplication.translate("LoginForm", u"N\u00e3o tem uma conta?", None))
        self.btnCriar.setText(QCoreApplication.translate("LoginForm", u"Crie agora", None))
        self.btnEsqueci.setText(QCoreApplication.translate("LoginForm", u"Esqueci a senha", None))
    # retranslateUi

