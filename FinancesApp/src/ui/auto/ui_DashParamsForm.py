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
    QDialog, QDialogButtonBox, QFormLayout, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_DashParamsForm(object):
    def setupUi(self, DashParamsForm):
        if not DashParamsForm.objectName():
            DashParamsForm.setObjectName(u"DashParamsForm")
        DashParamsForm.resize(450, 186)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        DashParamsForm.setFont(font)
        self.formLayout = QFormLayout(DashParamsForm)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.label = QLabel(DashParamsForm)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.dtStart = QDateEdit(DashParamsForm)
        self.dtStart.setObjectName(u"dtStart")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dtStart)

        self.label_2 = QLabel(DashParamsForm)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.dtEnd = QDateEdit(DashParamsForm)
        self.dtEnd.setObjectName(u"dtEnd")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dtEnd)

        self.buttonBox = QDialogButtonBox(DashParamsForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.buttonBox)

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


        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.widget_3)

        self.cbThird = QCheckBox(DashParamsForm)
        self.cbThird.setObjectName(u"cbThird")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.cbThird)


        self.retranslateUi(DashParamsForm)
        self.buttonBox.accepted.connect(DashParamsForm.accept)
        self.buttonBox.rejected.connect(DashParamsForm.reject)

        QMetaObject.connectSlotsByName(DashParamsForm)
    # setupUi

    def retranslateUi(self, DashParamsForm):
        DashParamsForm.setWindowTitle(QCoreApplication.translate("DashParamsForm", u"Par\u00e2metros do Dashboard", None))
        self.label.setText(QCoreApplication.translate("DashParamsForm", u"In\u00edcio", None))
        self.label_2.setText(QCoreApplication.translate("DashParamsForm", u"Fim", None))
        self.rbIn.setText(QCoreApplication.translate("DashParamsForm", u"Entrada", None))
        self.rbOut.setText(QCoreApplication.translate("DashParamsForm", u"Sa\u00edda", None))
        self.cbThird.setText(QCoreApplication.translate("DashParamsForm", u"Incluir terceiros", None))
    # retranslateUi

