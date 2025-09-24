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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . import resource_rc

class Ui_DashForm(object):
    def setupUi(self, DashForm):
        if not DashForm.objectName():
            DashForm.setObjectName(u"DashForm")
        DashForm.resize(700, 456)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        DashForm.setFont(font)
        self.verticalLayout = QVBoxLayout(DashForm)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(DashForm)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(494, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lbDesc = QLabel(self.widget)
        self.lbDesc.setObjectName(u"lbDesc")
        font2 = QFont()
        font2.setPointSize(11)
        self.lbDesc.setFont(font2)

        self.horizontalLayout.addWidget(self.lbDesc)

        self.btnParams = QPushButton(self.widget)
        self.btnParams.setObjectName(u"btnParams")
        self.btnParams.setStyleSheet(u"background-color: transparent; padding: 5")
        icon = QIcon()
        icon.addFile(u":/root/imgs/light-params.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnParams.setIcon(icon)
        self.btnParams.setIconSize(QSize(25, 25))
        self.btnParams.setFlat(True)

        self.horizontalLayout.addWidget(self.btnParams)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(DashForm)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameRegs = QFrame(self.widget_2)
        self.frameRegs.setObjectName(u"frameRegs")
        self.frameRegs.setFrameShape(QFrame.StyledPanel)
        self.frameRegs.setFrameShadow(QFrame.Raised)
        self.layoutRegs = QVBoxLayout(self.frameRegs)
        self.layoutRegs.setObjectName(u"layoutRegs")
        self.widget_4 = QWidget(self.frameRegs)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbRegType = QLabel(self.widget_4)
        self.lbRegType.setObjectName(u"lbRegType")
        self.lbRegType.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lbRegType)

        self.lbValue = QLabel(self.widget_4)
        self.lbValue.setObjectName(u"lbValue")
        self.lbValue.setFont(font1)
        self.lbValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbValue)


        self.layoutRegs.addWidget(self.widget_4)

        self.widChartDate = QFrame(self.frameRegs)
        self.widChartDate.setObjectName(u"widChartDate")
        self.widChartDate.setFrameShape(QFrame.StyledPanel)
        self.widChartDate.setFrameShadow(QFrame.Raised)

        self.layoutRegs.addWidget(self.widChartDate)

        self.widRegsPercent = QWidget(self.frameRegs)
        self.widRegsPercent.setObjectName(u"widRegsPercent")

        self.layoutRegs.addWidget(self.widRegsPercent)

        self.layoutRegs.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.frameRegs)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameCategory = QFrame(self.widget_3)
        self.frameCategory.setObjectName(u"frameCategory")
        self.frameCategory.setFrameShape(QFrame.StyledPanel)
        self.frameCategory.setFrameShadow(QFrame.Raised)
        self.layoutCategory = QVBoxLayout(self.frameCategory)
        self.layoutCategory.setObjectName(u"layoutCategory")
        self.label_6 = QLabel(self.frameCategory)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font1)

        self.layoutCategory.addWidget(self.label_6)

        self.widChartCategory = QWidget(self.frameCategory)
        self.widChartCategory.setObjectName(u"widChartCategory")

        self.layoutCategory.addWidget(self.widChartCategory)


        self.verticalLayout_2.addWidget(self.frameCategory)

        self.frameCard = QFrame(self.widget_3)
        self.frameCard.setObjectName(u"frameCard")
        self.frameCard.setFrameShape(QFrame.StyledPanel)
        self.frameCard.setFrameShadow(QFrame.Raised)
        self.cardLayout = QVBoxLayout(self.frameCard)
        self.cardLayout.setObjectName(u"cardLayout")
        self.widget_5 = QWidget(self.frameCard)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.cbCard = QComboBox(self.widget_5)
        self.cbCard.addItem("")
        self.cbCard.addItem("")
        self.cbCard.addItem("")
        self.cbCard.setObjectName(u"cbCard")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbCard.sizePolicy().hasHeightForWidth())
        self.cbCard.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.cbCard)


        self.cardLayout.addWidget(self.widget_5)

        self.widCardChart = QWidget(self.frameCard)
        self.widCardChart.setObjectName(u"widCardChart")

        self.cardLayout.addWidget(self.widCardChart)

        self.lbCardLimit = QLabel(self.frameCard)
        self.lbCardLimit.setObjectName(u"lbCardLimit")
        font3 = QFont()
        font3.setPointSize(9)
        self.lbCardLimit.setFont(font3)

        self.cardLayout.addWidget(self.lbCardLimit)

        self.lbCurrentInvoice = QLabel(self.frameCard)
        self.lbCurrentInvoice.setObjectName(u"lbCurrentInvoice")
        self.lbCurrentInvoice.setFont(font3)

        self.cardLayout.addWidget(self.lbCurrentInvoice)

        self.lbInvoiceExpected = QLabel(self.frameCard)
        self.lbInvoiceExpected.setObjectName(u"lbInvoiceExpected")
        self.lbInvoiceExpected.setFont(font3)

        self.cardLayout.addWidget(self.lbInvoiceExpected)

        self.cardLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.frameCard)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(DashForm)

        QMetaObject.connectSlotsByName(DashForm)
    # setupUi

    def retranslateUi(self, DashForm):
        DashForm.setWindowTitle(QCoreApplication.translate("DashForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("DashForm", u"Dashboard", None))
        self.lbDesc.setText(QCoreApplication.translate("DashForm", u"<DT_START> - <DT_END>", None))
#if QT_CONFIG(tooltip)
        self.btnParams.setToolTip(QCoreApplication.translate("DashForm", u"par\u00e2metros", None))
#endif // QT_CONFIG(tooltip)
        self.lbRegType.setText(QCoreApplication.translate("DashForm", u"<REG_TYPE>", None))
        self.lbValue.setText(QCoreApplication.translate("DashForm", u"R$ 0,00", None))
        self.label_6.setText(QCoreApplication.translate("DashForm", u"Categorias", None))
        self.label_2.setText(QCoreApplication.translate("DashForm", u"Cart\u00f5es", None))
        self.cbCard.setItemText(0, QCoreApplication.translate("DashForm", u"Nubank", None))
        self.cbCard.setItemText(1, QCoreApplication.translate("DashForm", u"Will", None))
        self.cbCard.setItemText(2, QCoreApplication.translate("DashForm", u"Santander", None))

        self.lbCardLimit.setText(QCoreApplication.translate("DashForm", u"Limite Total R$ 0,00", None))
        self.lbCurrentInvoice.setText(QCoreApplication.translate("DashForm", u"Fatura Atual R$ 0,00", None))
        self.lbInvoiceExpected.setText(QCoreApplication.translate("DashForm", u"Fatura Prevista R$0,00", None))
    # retranslateUi

