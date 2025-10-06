# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(1052, 639)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginPage.sizePolicy().hasHeightForWidth())
        LoginPage.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe Fluent Icons"])
        LoginPage.setFont(font)
        LoginPage.setStyleSheet(u"QWidget#MainForm {\n"
"	background-color: white;\n"
"}")
        self.horizontalLayout = QHBoxLayout(LoginPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(LoginPage)
        self.widget.setObjectName(u"widget")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.widget.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(308, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.widMain = QWidget(self.widget)
        self.widMain.setObjectName(u"widMain")
        self.widMain.setMinimumSize(QSize(400, 0))
        self.mainLayout = QVBoxLayout(self.widMain)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.widMain)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(29)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widMain)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.label_2)

        self.widContent = QWidget(self.widMain)
        self.widContent.setObjectName(u"widContent")

        self.mainLayout.addWidget(self.widContent)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.widMain)

        self.horizontalSpacer_2 = QSpacerItem(308, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.widget)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginPage", u"Finances", None))
        self.label_2.setText(QCoreApplication.translate("LoginPage", u"Seu controle financeiro em um s\u00f3 lugar.", None))
    # retranslateUi

