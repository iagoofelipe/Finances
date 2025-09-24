# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DashForm(object):
    def setupUi(self, DashForm):
        if not DashForm.objectName():
            DashForm.setObjectName(u"DashForm")
        DashForm.resize(700, 500)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        DashForm.setFont(font)
        self.verticalLayout = QVBoxLayout(DashForm)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(DashForm)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(DashForm)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbDesc = QLabel(self.widget)
        self.lbDesc.setObjectName(u"lbDesc")

        self.horizontalLayout.addWidget(self.lbDesc)

        self.horizontalSpacer = QSpacerItem(494, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnOptions = QPushButton(self.widget)
        self.btnOptions.setObjectName(u"btnOptions")

        self.horizontalLayout.addWidget(self.btnOptions)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(DashForm)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutValues = QVBoxLayout(self.frame)
        self.layoutValues.setObjectName(u"layoutValues")
        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lbValue = QLabel(self.widget_4)
        self.lbValue.setObjectName(u"lbValue")
        self.lbValue.setFont(font1)
        self.lbValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbValue)


        self.layoutValues.addWidget(self.widget_4)

        self.widChartDate = QFrame(self.frame)
        self.widChartDate.setObjectName(u"widChartDate")
        self.widChartDate.setFrameShape(QFrame.StyledPanel)
        self.widChartDate.setFrameShadow(QFrame.Raised)

        self.layoutValues.addWidget(self.widChartDate)

        self.widPercent = QWidget(self.frame)
        self.widPercent.setObjectName(u"widPercent")
        self.layoutPercent = QGridLayout(self.widPercent)
        self.layoutPercent.setObjectName(u"layoutPercent")
        self.layoutPercent.setHorizontalSpacing(0)
        self.layoutPercent.setVerticalSpacing(10)
        self.layoutPercent.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widPercent)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.layoutPercent.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widPercent)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.layoutPercent.addWidget(self.label_4, 0, 0, 1, 1)

        self.widChartPercent = QFrame(self.widPercent)
        self.widChartPercent.setObjectName(u"widChartPercent")
        self.widChartPercent.setFrameShape(QFrame.StyledPanel)
        self.widChartPercent.setFrameShadow(QFrame.Raised)

        self.layoutPercent.addWidget(self.widChartPercent, 1, 0, 1, 2)

        self.lbValRight = QLabel(self.widPercent)
        self.lbValRight.setObjectName(u"lbValRight")
        sizePolicy.setHeightForWidth(self.lbValRight.sizePolicy().hasHeightForWidth())
        self.lbValRight.setSizePolicy(sizePolicy)

        self.layoutPercent.addWidget(self.lbValRight, 2, 0, 1, 1)

        self.lbValLeft = QLabel(self.widPercent)
        self.lbValLeft.setObjectName(u"lbValLeft")
        sizePolicy.setHeightForWidth(self.lbValLeft.sizePolicy().hasHeightForWidth())
        self.lbValLeft.setSizePolicy(sizePolicy)
        self.lbValLeft.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.layoutPercent.addWidget(self.lbValLeft, 2, 1, 1, 1)


        self.layoutValues.addWidget(self.widPercent)

        self.layoutValues.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.frame)

        self.frameCategory = QFrame(self.widget_2)
        self.frameCategory.setObjectName(u"frameCategory")
        self.frameCategory.setFrameShape(QFrame.StyledPanel)
        self.frameCategory.setFrameShadow(QFrame.Raised)
        self.layoutCategory = QVBoxLayout(self.frameCategory)
        self.layoutCategory.setObjectName(u"layoutCategory")
        self.label_6 = QLabel(self.frameCategory)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font1)

        self.layoutCategory.addWidget(self.label_6)

        self.widChartCategory = QWidget(self.frameCategory)
        self.widChartCategory.setObjectName(u"widChartCategory")

        self.layoutCategory.addWidget(self.widChartCategory)


        self.horizontalLayout_2.addWidget(self.frameCategory)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(DashForm)

        QMetaObject.connectSlotsByName(DashForm)
    # setupUi

    def retranslateUi(self, DashForm):
        DashForm.setWindowTitle(QCoreApplication.translate("DashForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("DashForm", u"Dashboard", None))
        self.lbDesc.setText(QCoreApplication.translate("DashForm", u"<REG_TYPE> de <DT_START> at\u00e9 <DT_END>", None))
        self.btnOptions.setText(QCoreApplication.translate("DashForm", u"op\u00e7\u00f5es", None))
        self.label_2.setText(QCoreApplication.translate("DashForm", u"Registros", None))
        self.lbValue.setText(QCoreApplication.translate("DashForm", u"R$ 0,00", None))
        self.label_5.setText(QCoreApplication.translate("DashForm", u"Pendente", None))
        self.label_4.setText(QCoreApplication.translate("DashForm", u"Contabilizado", None))
        self.lbValRight.setText(QCoreApplication.translate("DashForm", u"R$ 0,00", None))
        self.lbValLeft.setText(QCoreApplication.translate("DashForm", u"R$ 0,00", None))
        self.label_6.setText(QCoreApplication.translate("DashForm", u"Categorias", None))
    # retranslateUi

