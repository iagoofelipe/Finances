# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
        LoginForm.resize(681, 469)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        LoginForm.setFont(font)
        self.horizontalLayout = QHBoxLayout(LoginForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(173, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget = QWidget(LoginForm)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.leUser = QLineEdit(self.widget)
        self.leUser.setObjectName(u"leUser")

        self.verticalLayout.addWidget(self.leUser)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lePassword = QLineEdit(self.widget)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lePassword)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.cbKeep = QCheckBox(self.widget_2)
        self.cbKeep.setObjectName(u"cbKeep")

        self.horizontalLayout_2.addWidget(self.cbKeep)

        self.horizontalSpacer_4 = QSpacerItem(51, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_2)

        self.lbAlert = QLabel(self.widget)
        self.lbAlert.setObjectName(u"lbAlert")
        self.lbAlert.setAlignment(Qt.AlignCenter)
        self.lbAlert.setMargin(5)

        self.verticalLayout.addWidget(self.lbAlert)

        self.btnLogin = QPushButton(self.widget)
        self.btnLogin.setObjectName(u"btnLogin")

        self.verticalLayout.addWidget(self.btnLogin)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(172, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        QWidget.setTabOrder(self.leUser, self.lePassword)
        QWidget.setTabOrder(self.lePassword, self.cbKeep)
        QWidget.setTabOrder(self.cbKeep, self.btnLogin)

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"Finances", None))
        self.label_2.setText(QCoreApplication.translate("LoginForm", u"usu\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("LoginForm", u"senha", None))
        self.cbKeep.setText(QCoreApplication.translate("LoginForm", u"manter conectado", None))
        self.lbAlert.setText(QCoreApplication.translate("LoginForm", u"-ALERT-", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginForm", u"login", None))
    # retranslateUi

