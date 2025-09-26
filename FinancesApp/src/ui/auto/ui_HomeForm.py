# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_HomeForm(object):
    def setupUi(self, HomeForm):
        if not HomeForm.objectName():
            HomeForm.setObjectName(u"HomeForm")
        HomeForm.resize(700, 398)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        HomeForm.setFont(font)
        self.mainLayout = QHBoxLayout(HomeForm)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(HomeForm)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QPushButton { background-color: transparent }")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnDash = QPushButton(self.frame)
        self.btnDash.setObjectName(u"btnDash")
        self.btnDash.setFont(font)
        icon = QIcon()
        icon.addFile(u":/root/imgs/light-pie.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDash.setIcon(icon)
        self.btnDash.setIconSize(QSize(25, 25))
        self.btnDash.setFlat(True)

        self.verticalLayout.addWidget(self.btnDash)

        self.btnReg = QPushButton(self.frame)
        self.btnReg.setObjectName(u"btnReg")
        self.btnReg.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/root/imgs/light-table.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnReg.setIcon(icon1)
        self.btnReg.setIconSize(QSize(25, 25))
        self.btnReg.setFlat(True)

        self.verticalLayout.addWidget(self.btnReg)

        self.btnCard = QPushButton(self.frame)
        self.btnCard.setObjectName(u"btnCard")
        self.btnCard.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/root/imgs/light-card.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCard.setIcon(icon2)
        self.btnCard.setIconSize(QSize(25, 25))
        self.btnCard.setFlat(True)

        self.verticalLayout.addWidget(self.btnCard)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.verticalSpacer_2 = QSpacerItem(20, 141, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btnUser = QPushButton(self.frame)
        self.btnUser.setObjectName(u"btnUser")
        self.btnUser.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/root/imgs/light-user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUser.setIcon(icon3)
        self.btnUser.setIconSize(QSize(25, 25))
        self.btnUser.setFlat(True)

        self.verticalLayout.addWidget(self.btnUser)

        self.btnConfig = QPushButton(self.frame)
        self.btnConfig.setObjectName(u"btnConfig")
        self.btnConfig.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/root/imgs/light-gear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConfig.setIcon(icon4)
        self.btnConfig.setIconSize(QSize(25, 25))
        self.btnConfig.setFlat(True)

        self.verticalLayout.addWidget(self.btnConfig)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btnLogout = QPushButton(self.frame)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/root/imgs/light-logout.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLogout.setIcon(icon5)
        self.btnLogout.setIconSize(QSize(25, 25))
        self.btnLogout.setFlat(True)

        self.verticalLayout.addWidget(self.btnLogout)


        self.mainLayout.addWidget(self.frame)

        self.widContent = QWidget(HomeForm)
        self.widContent.setObjectName(u"widContent")

        self.mainLayout.addWidget(self.widContent)

        self.mainLayout.setStretch(1, 1)

        self.retranslateUi(HomeForm)

        QMetaObject.connectSlotsByName(HomeForm)
    # setupUi

    def retranslateUi(self, HomeForm):
        HomeForm.setWindowTitle(QCoreApplication.translate("HomeForm", u"Form", None))
        self.btnDash.setText(QCoreApplication.translate("HomeForm", u"Dashboard        ", None))
        self.btnReg.setText(QCoreApplication.translate("HomeForm", u"Registros           ", None))
        self.btnCard.setText(QCoreApplication.translate("HomeForm", u"Banco e Cart\u00f5es", None))
        self.btnUser.setText(QCoreApplication.translate("HomeForm", u"Usu\u00e1rio              ", None))
        self.btnConfig.setText(QCoreApplication.translate("HomeForm", u"Configura\u00e7\u00f5es   ", None))
        self.btnLogout.setText(QCoreApplication.translate("HomeForm", u"Sair                    ", None))
    # retranslateUi

