# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableForm.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from . import resource_rc

class Ui_TableForm(object):
    def setupUi(self, TableForm):
        if not TableForm.objectName():
            TableForm.setObjectName(u"TableForm")
        TableForm.resize(572, 515)
        self.verticalLayout_2 = QVBoxLayout(TableForm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(TableForm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbTitle = QLabel(self.widget)
        self.lbTitle.setObjectName(u"lbTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        self.lbTitle.setFont(font)

        self.horizontalLayout.addWidget(self.lbTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnReject = QPushButton(self.widget)
        self.btnReject.setObjectName(u"btnReject")
        self.btnReject.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/root/icons/light_x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnReject.setIcon(icon)
        self.btnReject.setIconSize(QSize(20, 20))
        self.btnReject.setFlat(True)

        self.horizontalLayout.addWidget(self.btnReject)

        self.btnAccept = QPushButton(self.widget)
        self.btnAccept.setObjectName(u"btnAccept")
        self.btnAccept.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/root/icons/light_check.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAccept.setIcon(icon1)
        self.btnAccept.setIconSize(QSize(20, 20))
        self.btnAccept.setFlat(True)

        self.horizontalLayout.addWidget(self.btnAccept)

        self.btnDelete = QPushButton(self.widget)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setStyleSheet(u"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/root/icons/light_trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon2)
        self.btnDelete.setIconSize(QSize(20, 20))
        self.btnDelete.setFlat(True)

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnDetails = QPushButton(self.widget)
        self.btnDetails.setObjectName(u"btnDetails")
        self.btnDetails.setStyleSheet(u"background-color: transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/root/icons/light_detail.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetails.setIcon(icon3)
        self.btnDetails.setIconSize(QSize(20, 20))
        self.btnDetails.setFlat(True)

        self.horizontalLayout.addWidget(self.btnDetails)

        self.btnAdd = QPushButton(self.widget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setStyleSheet(u"background-color: transparent;")
        icon4 = QIcon()
        icon4.addFile(u":/root/icons/light_plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAdd.setIcon(icon4)
        self.btnAdd.setIconSize(QSize(20, 20))
        self.btnAdd.setFlat(True)

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnParams = QPushButton(self.widget)
        self.btnParams.setObjectName(u"btnParams")
        self.btnParams.setStyleSheet(u"background-color: transparent;")
        icon5 = QIcon()
        icon5.addFile(u":/root/icons/light_sliders.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnParams.setIcon(icon5)
        self.btnParams.setIconSize(QSize(20, 20))
        self.btnParams.setFlat(True)

        self.horizontalLayout.addWidget(self.btnParams)

        self.btnEdit = QPushButton(self.widget)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setStyleSheet(u"background-color: transparent;")
        icon6 = QIcon()
        icon6.addFile(u":/root/icons/light_edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdit.setIcon(icon6)
        self.btnEdit.setIconSize(QSize(20, 20))
        self.btnEdit.setFlat(True)

        self.horizontalLayout.addWidget(self.btnEdit)


        self.verticalLayout.addWidget(self.widget)

        self.frameTable = QFrame(self.frame)
        self.frameTable.setObjectName(u"frameTable")
        self.frameTable.setFrameShape(QFrame.StyledPanel)
        self.frameTable.setFrameShadow(QFrame.Raised)
        self.frameTableLayout = QVBoxLayout(self.frameTable)
        self.frameTableLayout.setSpacing(0)
        self.frameTableLayout.setObjectName(u"frameTableLayout")
        self.frameTableLayout.setContentsMargins(5, 5, 5, 5)
        self.tableWid = QTableWidget(self.frameTable)
        self.tableWid.setObjectName(u"tableWid")
        self.tableWid.setStyleSheet(u"QTableWidget::item:selected, QTableWidget::item::hover {\n"
"	color: white;\n"
"	background-color: rgb(68, 68, 68);\n"
"}")
        self.tableWid.setFrameShape(QFrame.NoFrame)
        self.tableWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWid.setAlternatingRowColors(True)
        self.tableWid.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableWid.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWid.setShowGrid(False)
        self.tableWid.setSortingEnabled(True)
        self.tableWid.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tableWid.horizontalHeader().setStretchLastSection(True)
        self.tableWid.verticalHeader().setVisible(False)
        self.tableWid.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWid.verticalHeader().setStretchLastSection(False)

        self.frameTableLayout.addWidget(self.tableWid)


        self.verticalLayout.addWidget(self.frameTable)

        self.widNav = QWidget(self.frame)
        self.widNav.setObjectName(u"widNav")
        self.horizontalLayout_2 = QHBoxLayout(self.widNav)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(172, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnPrev = QPushButton(self.widNav)
        self.btnPrev.setObjectName(u"btnPrev")
        self.btnPrev.setStyleSheet(u"background-color: transparent;")
        icon7 = QIcon()
        icon7.addFile(u":/root/icons/light_prev.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrev.setIcon(icon7)
        self.btnPrev.setIconSize(QSize(25, 25))
        self.btnPrev.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnPrev)

        self.lbNav = QLabel(self.widNav)
        self.lbNav.setObjectName(u"lbNav")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.lbNav.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lbNav)

        self.btnNext = QPushButton(self.widNav)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setStyleSheet(u"background-color: transparent;")
        icon8 = QIcon()
        icon8.addFile(u":/root/icons/light_next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNext.setIcon(icon8)
        self.btnNext.setIconSize(QSize(25, 25))
        self.btnNext.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnNext)

        self.horizontalSpacer_3 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widNav)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(TableForm)

        QMetaObject.connectSlotsByName(TableForm)
    # setupUi

    def retranslateUi(self, TableForm):
        TableForm.setWindowTitle(QCoreApplication.translate("TableForm", u"Form", None))
        self.lbTitle.setText(QCoreApplication.translate("TableForm", u"TITLE", None))
        self.lbNav.setText(QCoreApplication.translate("TableForm", u"0 a 0 de 0 itens", None))
    # retranslateUi

