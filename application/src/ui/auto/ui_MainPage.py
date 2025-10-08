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
        self.mainLayout = QGridLayout(MainPage)
        self.mainLayout.setObjectName(u"mainLayout")
        self.widget = QWidget(MainPage)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbTextUser = QLabel(self.widget)
        self.lbTextUser.setObjectName(u"lbTextUser")
        font1 = QFont()
        font1.setPointSize(18)
        self.lbTextUser.setFont(font1)

        self.horizontalLayout.addWidget(self.lbTextUser)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lbTitle = QLabel(self.widget)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setStyleSheet(u"color: #5E5E5E;")

        self.horizontalLayout.addWidget(self.lbTitle)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        icon = QIcon()
        icon.addFile(u":/root/icons/bell.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNotificacoes.setIcon(icon)
        self.btnNotificacoes.setIconSize(QSize(25, 25))
        self.btnNotificacoes.setFlat(True)

        self.horizontalLayout.addWidget(self.btnNotificacoes)


        self.mainLayout.addWidget(self.widget, 0, 0, 1, 2)

        self.frame = QFrame(MainPage)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(11)
        self.frame.setFont(font2)
        self.frame.setStyleSheet(u"QWidget {\n"
"	color: #5E5E5E;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"	padding: 10;\n"
"	border-radius: 10;\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"QPushButton::hover, QPushButton:checked {\n"
"	border-left:4px solid #003F87;\n"
"	background-color: #CEE5FF;\n"
"}\n"
"\n"
"/* bot\u00f5es para n\u00e3o aplicar cores */\n"
"QPushButton#btnSair::hover, QPushButton#btnNav::hover { background-color: transparent; border: none;}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frameLayout = QVBoxLayout(self.frame)
        self.frameLayout.setObjectName(u"frameLayout")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frameLayout.addWidget(self.widget_2)

        self.btnNav = QPushButton(self.frame)
        self.btnNav.setObjectName(u"btnNav")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        self.btnNav.setFont(font3)
        self.btnNav.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/root/icons/bars-solid-full.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNav.setIcon(icon1)
        self.btnNav.setIconSize(QSize(25, 25))
        self.btnNav.setFlat(True)

        self.frameLayout.addWidget(self.btnNav)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.frameLayout.addWidget(self.line_2)

        self.btnQuantitativos = QPushButton(self.frame)
        self.btnQuantitativos.setObjectName(u"btnQuantitativos")
        self.btnQuantitativos.setFont(font3)
        self.btnQuantitativos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/root/icons/pie-chart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnQuantitativos.setIcon(icon2)
        self.btnQuantitativos.setIconSize(QSize(25, 25))
        self.btnQuantitativos.setCheckable(True)
        self.btnQuantitativos.setFlat(True)

        self.frameLayout.addWidget(self.btnQuantitativos)

        self.btnRegs = QPushButton(self.frame)
        self.btnRegs.setObjectName(u"btnRegs")
        self.btnRegs.setFont(font3)
        self.btnRegs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/root/icons/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegs.setIcon(icon3)
        self.btnRegs.setIconSize(QSize(25, 25))
        self.btnRegs.setCheckable(True)
        self.btnRegs.setFlat(True)

        self.frameLayout.addWidget(self.btnRegs)

        self.btnCartoes = QPushButton(self.frame)
        self.btnCartoes.setObjectName(u"btnCartoes")
        self.btnCartoes.setFont(font3)
        self.btnCartoes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/root/icons/credit-card.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCartoes.setIcon(icon4)
        self.btnCartoes.setIconSize(QSize(25, 25))
        self.btnCartoes.setCheckable(True)
        self.btnCartoes.setFlat(True)

        self.frameLayout.addWidget(self.btnCartoes)

        self.btnConfig = QPushButton(self.frame)
        self.btnConfig.setObjectName(u"btnConfig")
        self.btnConfig.setFont(font3)
        self.btnConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnConfig.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/root/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConfig.setIcon(icon5)
        self.btnConfig.setIconSize(QSize(25, 25))
        self.btnConfig.setCheckable(True)
        self.btnConfig.setFlat(True)

        self.frameLayout.addWidget(self.btnConfig)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.frameLayout.addItem(self.verticalSpacer)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.frameLayout.addWidget(self.line)

        self.btnSair = QPushButton(self.frame)
        self.btnSair.setObjectName(u"btnSair")
        self.btnSair.setFont(font3)
        self.btnSair.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSair.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/root/icons/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSair.setIcon(icon6)
        self.btnSair.setIconSize(QSize(25, 25))
        self.btnSair.setFlat(True)

        self.frameLayout.addWidget(self.btnSair)


        self.mainLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.widContent = QWidget(MainPage)
        self.widContent.setObjectName(u"widContent")

        self.mainLayout.addWidget(self.widContent, 1, 1, 1, 1)


        self.retranslateUi(MainPage)

        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"Form", None))
        self.lbTextUser.setText(QCoreApplication.translate("MainPage", u"-TEXT-", None))
        self.lbTitle.setText(QCoreApplication.translate("MainPage", u"-TITLE-", None))
        self.btnNotificacoes.setText("")
#if QT_CONFIG(tooltip)
        self.btnNav.setToolTip(QCoreApplication.translate("MainPage", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.btnNav.setText(QCoreApplication.translate("MainPage", u"Menu                   ", None))
#if QT_CONFIG(tooltip)
        self.btnQuantitativos.setToolTip(QCoreApplication.translate("MainPage", u"Quantitativos", None))
#endif // QT_CONFIG(tooltip)
        self.btnQuantitativos.setText(QCoreApplication.translate("MainPage", u"Quantitativos       ", None))
#if QT_CONFIG(tooltip)
        self.btnRegs.setToolTip(QCoreApplication.translate("MainPage", u"Registros", None))
#endif // QT_CONFIG(tooltip)
        self.btnRegs.setText(QCoreApplication.translate("MainPage", u"Registros             ", None))
#if QT_CONFIG(tooltip)
        self.btnCartoes.setToolTip(QCoreApplication.translate("MainPage", u"Cart\u00f5es e Contas", None))
#endif // QT_CONFIG(tooltip)
        self.btnCartoes.setText(QCoreApplication.translate("MainPage", u"Cart\u00f5es e Contas ", None))
#if QT_CONFIG(tooltip)
        self.btnConfig.setToolTip(QCoreApplication.translate("MainPage", u"Configura\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
        self.btnConfig.setText(QCoreApplication.translate("MainPage", u"Configura\u00e7\u00f5es     ", None))
#if QT_CONFIG(tooltip)
        self.btnSair.setToolTip(QCoreApplication.translate("MainPage", u"Sair", None))
#endif // QT_CONFIG(tooltip)
        self.btnSair.setText(QCoreApplication.translate("MainPage", u"Sair                      ", None))
    # retranslateUi

