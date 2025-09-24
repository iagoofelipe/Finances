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

class Ui_HomeForm(object):
    def setupUi(self, HomeForm):
        if not HomeForm.objectName():
            HomeForm.setObjectName(u"HomeForm")
        HomeForm.resize(704, 398)
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
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 141, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnDash = QPushButton(self.frame)
        self.btnDash.setObjectName(u"btnDash")

        self.verticalLayout.addWidget(self.btnDash)

        self.btnReg = QPushButton(self.frame)
        self.btnReg.setObjectName(u"btnReg")

        self.verticalLayout.addWidget(self.btnReg)

        self.verticalSpacer_2 = QSpacerItem(20, 141, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


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
        self.btnDash.setText(QCoreApplication.translate("HomeForm", u"Dashboard", None))
        self.btnReg.setText(QCoreApplication.translate("HomeForm", u"Registros", None))
    # retranslateUi

