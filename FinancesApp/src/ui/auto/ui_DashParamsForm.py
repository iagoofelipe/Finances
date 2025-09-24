# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashParamsForm.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDateEdit,
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DashParamsForm(object):
    def setupUi(self, DashParamsForm):
        if not DashParamsForm.objectName():
            DashParamsForm.setObjectName(u"DashParamsForm")
        DashParamsForm.resize(458, 412)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        DashParamsForm.setFont(font)
        self.gridLayout = QGridLayout(DashParamsForm)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.groupBox = QGroupBox(DashParamsForm)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.cbCatAll = QCheckBox(self.groupBox)
        self.cbCatAll.setObjectName(u"cbCatAll")
        self.cbCatAll.setTristate(False)

        self.verticalLayout.addWidget(self.cbCatAll)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.widCategories = QWidget()
        self.widCategories.setObjectName(u"widCategories")
        self.widCategories.setGeometry(QRect(0, 0, 414, 140))
        self.scrollArea.setWidget(self.widCategories)

        self.verticalLayout.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 2)

        self.widget_3 = QWidget(DashParamsForm)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rbIn = QRadioButton(self.widget_3)
        self.rbIn.setObjectName(u"rbIn")

        self.horizontalLayout_2.addWidget(self.rbIn)

        self.rbOut = QRadioButton(self.widget_3)
        self.rbOut.setObjectName(u"rbOut")

        self.horizontalLayout_2.addWidget(self.rbOut)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 2)

        self.dtEnd = QDateEdit(DashParamsForm)
        self.dtEnd.setObjectName(u"dtEnd")

        self.gridLayout.addWidget(self.dtEnd, 2, 1, 1, 1)

        self.dtStart = QDateEdit(DashParamsForm)
        self.dtStart.setObjectName(u"dtStart")

        self.gridLayout.addWidget(self.dtStart, 1, 1, 1, 1)

        self.label_2 = QLabel(DashParamsForm)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(DashParamsForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 2)

        self.label = QLabel(DashParamsForm)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(DashParamsForm)
        self.buttonBox.accepted.connect(DashParamsForm.accept)
        self.buttonBox.rejected.connect(DashParamsForm.reject)

        QMetaObject.connectSlotsByName(DashParamsForm)
    # setupUi

    def retranslateUi(self, DashParamsForm):
        DashParamsForm.setWindowTitle(QCoreApplication.translate("DashParamsForm", u"Par\u00e2metros do Dashboard", None))
        self.groupBox.setTitle(QCoreApplication.translate("DashParamsForm", u"Categorias", None))
        self.cbCatAll.setText(QCoreApplication.translate("DashParamsForm", u"incluir todas as categorias", None))
        self.label_3.setText(QCoreApplication.translate("DashParamsForm", u"Categorias selecionadas", None))
        self.rbIn.setText(QCoreApplication.translate("DashParamsForm", u"Entrada", None))
        self.rbOut.setText(QCoreApplication.translate("DashParamsForm", u"Sa\u00edda", None))
        self.label_2.setText(QCoreApplication.translate("DashParamsForm", u"Fim", None))
        self.label.setText(QCoreApplication.translate("DashParamsForm", u"In\u00edcio", None))
    # retranslateUi

