# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainPage.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(949, 529)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        MainPage.setFont(font)
        self.gridLayout = QGridLayout(MainPage)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(MainPage)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        self.frame.setFont(font1)
        self.frame.setStyleSheet(u"color: #5E5E5E;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnQuantitativos = QPushButton(self.frame)
        self.btnQuantitativos.setObjectName(u"btnQuantitativos")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        self.btnQuantitativos.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/root/icons/pie-chart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnQuantitativos.setIcon(icon)
        self.btnQuantitativos.setIconSize(QSize(25, 25))
        self.btnQuantitativos.setFlat(True)

        self.verticalLayout.addWidget(self.btnQuantitativos)

        self.btnRegs = QPushButton(self.frame)
        self.btnRegs.setObjectName(u"btnRegs")
        self.btnRegs.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/root/icons/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegs.setIcon(icon1)
        self.btnRegs.setIconSize(QSize(25, 25))
        self.btnRegs.setFlat(True)

        self.verticalLayout.addWidget(self.btnRegs)

        self.btnCartoes = QPushButton(self.frame)
        self.btnCartoes.setObjectName(u"btnCartoes")
        self.btnCartoes.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/root/icons/credit-card.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCartoes.setIcon(icon2)
        self.btnCartoes.setIconSize(QSize(25, 25))
        self.btnCartoes.setFlat(True)

        self.verticalLayout.addWidget(self.btnCartoes)

        self.verticalSpacer = QSpacerItem(20, 244, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnConfig = QPushButton(self.frame)
        self.btnConfig.setObjectName(u"btnConfig")
        self.btnConfig.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/root/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConfig.setIcon(icon3)
        self.btnConfig.setIconSize(QSize(25, 25))
        self.btnConfig.setFlat(True)

        self.verticalLayout.addWidget(self.btnConfig)

        self.btnSair = QPushButton(self.frame)
        self.btnSair.setObjectName(u"btnSair")
        self.btnSair.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/root/icons/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSair.setIcon(icon4)
        self.btnSair.setIconSize(QSize(25, 25))
        self.btnSair.setFlat(True)

        self.verticalLayout.addWidget(self.btnSair)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.widget_2 = QWidget(MainPage)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)

        self.widget = QWidget(MainPage)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbText = QLabel(self.widget)
        self.lbText.setObjectName(u"lbText")
        font3 = QFont()
        font3.setPointSize(18)
        self.lbText.setFont(font3)

        self.horizontalLayout.addWidget(self.lbText)

        self.horizontalSpacer = QSpacerItem(707, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cbProfile = QComboBox(self.widget)
        self.cbProfile.setObjectName(u"cbProfile")

        self.horizontalLayout.addWidget(self.cbProfile)

        self.btnNotificacoes = QPushButton(self.widget)
        self.btnNotificacoes.setObjectName(u"btnNotificacoes")
        self.btnNotificacoes.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	border: 1px solid #EDEDED;\n"
"	border-radius: 18;\n"
"    padding: 5;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: transparent;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/root/icons/bell.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNotificacoes.setIcon(icon5)
        self.btnNotificacoes.setIconSize(QSize(25, 25))
        self.btnNotificacoes.setFlat(True)

        self.horizontalLayout.addWidget(self.btnNotificacoes)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)


        self.retranslateUi(MainPage)

        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"Form", None))
        self.btnQuantitativos.setText(QCoreApplication.translate("MainPage", u"Quantitativos      ", None))
        self.btnRegs.setText(QCoreApplication.translate("MainPage", u"Registros             ", None))
        self.btnCartoes.setText(QCoreApplication.translate("MainPage", u"Cart\u00f5es e Contas", None))
        self.btnConfig.setText(QCoreApplication.translate("MainPage", u"Configura\u00e7\u00f5es     ", None))
        self.btnSair.setText(QCoreApplication.translate("MainPage", u"Sair                      ", None))
        self.lbText.setText(QCoreApplication.translate("MainPage", u"-TEXT-", None))
        self.btnNotificacoes.setText("")
    # retranslateUi

