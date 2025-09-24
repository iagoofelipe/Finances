# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegForm.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_RegForm(object):
    def setupUi(self, RegForm):
        if not RegForm.objectName():
            RegForm.setObjectName(u"RegForm")
        RegForm.resize(758, 478)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        RegForm.setFont(font)
        self.verticalLayout = QVBoxLayout(RegForm)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(RegForm)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QPushButton { background-color: transparent; padding: 5 }")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(499, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.btnFilter = QPushButton(self.widget_2)
        self.btnFilter.setObjectName(u"btnFilter")
        icon = QIcon()
        icon.addFile(u":/root/imgs/light-filter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFilter.setIcon(icon)
        self.btnFilter.setIconSize(QSize(25, 25))
        self.btnFilter.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnFilter)

        self.btnDelete = QPushButton(self.widget_2)
        self.btnDelete.setObjectName(u"btnDelete")
        icon1 = QIcon()
        icon1.addFile(u":/root/imgs/light-trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon1)
        self.btnDelete.setIconSize(QSize(25, 25))
        self.btnDelete.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.btnEdit = QPushButton(self.widget_2)
        self.btnEdit.setObjectName(u"btnEdit")
        icon2 = QIcon()
        icon2.addFile(u":/root/imgs/light-pen.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdit.setIcon(icon2)
        self.btnEdit.setIconSize(QSize(25, 25))
        self.btnEdit.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnAdd = QPushButton(self.widget_2)
        self.btnAdd.setObjectName(u"btnAdd")
        icon3 = QIcon()
        icon3.addFile(u":/root/imgs/light-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAdd.setIcon(icon3)
        self.btnAdd.setIconSize(QSize(25, 25))
        self.btnAdd.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnAdd)


        self.verticalLayout.addWidget(self.widget_2)

        self.tableWidget = QTableWidget(RegForm)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.widget = QWidget(RegForm)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton { background-color: transparent; padding: 5 }")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnPrev = QPushButton(self.widget)
        self.btnPrev.setObjectName(u"btnPrev")
        icon4 = QIcon()
        icon4.addFile(u":/root/imgs/light-left-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrev.setIcon(icon4)
        self.btnPrev.setIconSize(QSize(25, 25))
        self.btnPrev.setFlat(True)

        self.horizontalLayout.addWidget(self.btnPrev)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.btnNext = QPushButton(self.widget)
        self.btnNext.setObjectName(u"btnNext")
        icon5 = QIcon()
        icon5.addFile(u":/root/imgs/light-right-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNext.setIcon(icon5)
        self.btnNext.setIconSize(QSize(25, 25))
        self.btnNext.setFlat(True)

        self.horizontalLayout.addWidget(self.btnNext)

        self.horizontalSpacer_2 = QSpacerItem(277, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(RegForm)

        QMetaObject.connectSlotsByName(RegForm)
    # setupUi

    def retranslateUi(self, RegForm):
        RegForm.setWindowTitle(QCoreApplication.translate("RegForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("RegForm", u"Registros", None))
#if QT_CONFIG(tooltip)
        self.btnFilter.setToolTip(QCoreApplication.translate("RegForm", u"filtrar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnDelete.setToolTip(QCoreApplication.translate("RegForm", u"deletar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnEdit.setToolTip(QCoreApplication.translate("RegForm", u"editar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnAdd.setToolTip(QCoreApplication.translate("RegForm", u"adicionar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnPrev.setToolTip(QCoreApplication.translate("RegForm", u"voltar", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("RegForm", u"0 a 0 de 0", None))
#if QT_CONFIG(tooltip)
        self.btnNext.setToolTip(QCoreApplication.translate("RegForm", u"avan\u00e7ar", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

