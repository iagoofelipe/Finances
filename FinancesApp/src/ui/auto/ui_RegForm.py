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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateTimeEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_RegForm(object):
    def setupUi(self, RegForm):
        if not RegForm.objectName():
            RegForm.setObjectName(u"RegForm")
        RegForm.resize(849, 542)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        RegForm.setFont(font)
        RegForm.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(RegForm)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(RegForm)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QPushButton { background-color: transparent; padding: 5 }")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(15)
        font1.setKerning(True)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(113, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.btnParams = QPushButton(self.widget_2)
        self.btnParams.setObjectName(u"btnParams")
        icon = QIcon()
        icon.addFile(u":/root/imgs/light-params.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnParams.setIcon(icon)
        self.btnParams.setIconSize(QSize(25, 25))
        self.btnParams.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnParams)

        self.btnDelete = QPushButton(self.widget_2)
        self.btnDelete.setObjectName(u"btnDelete")
        icon1 = QIcon()
        icon1.addFile(u":/root/imgs/light-trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon1)
        self.btnDelete.setIconSize(QSize(25, 25))
        self.btnDelete.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.btnAdd = QPushButton(self.widget_2)
        self.btnAdd.setObjectName(u"btnAdd")
        icon2 = QIcon()
        icon2.addFile(u":/root/imgs/light-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAdd.setIcon(icon2)
        self.btnAdd.setIconSize(QSize(25, 25))
        self.btnAdd.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnAdd)


        self.verticalLayout.addWidget(self.widget_2)

        self.widTable = QTableWidget(self.widget_3)
        self.widTable.setObjectName(u"widTable")
        self.widTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.widTable.setAlternatingRowColors(True)
        self.widTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.widTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.widTable)

        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnPrev = QPushButton(self.widget)
        self.btnPrev.setObjectName(u"btnPrev")
        icon3 = QIcon()
        icon3.addFile(u":/root/imgs/light-left-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrev.setIcon(icon3)
        self.btnPrev.setIconSize(QSize(25, 25))
        self.btnPrev.setFlat(False)

        self.horizontalLayout.addWidget(self.btnPrev)

        self.lbTableNav = QLabel(self.widget)
        self.lbTableNav.setObjectName(u"lbTableNav")
        self.lbTableNav.setFont(font)

        self.horizontalLayout.addWidget(self.lbTableNav)

        self.btnNext = QPushButton(self.widget)
        self.btnNext.setObjectName(u"btnNext")
        icon4 = QIcon()
        icon4.addFile(u":/root/imgs/light-right-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNext.setIcon(icon4)
        self.btnNext.setIconSize(QSize(25, 25))
        self.btnNext.setFlat(False)

        self.horizontalLayout.addWidget(self.btnNext)

        self.horizontalSpacer_2 = QSpacerItem(126, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.widDetails = QWidget(RegForm)
        self.widDetails.setObjectName(u"widDetails")
        self.verticalLayout_2 = QVBoxLayout(self.widDetails)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widDetails)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QPushButton { background-color: transparent; padding: 5 }")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(15)
        self.label_3.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.btnClear = QPushButton(self.widget_6)
        self.btnClear.setObjectName(u"btnClear")
        icon5 = QIcon()
        icon5.addFile(u":/root/imgs/light-eraser.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClear.setIcon(icon5)
        self.btnClear.setIconSize(QSize(25, 25))
        self.btnClear.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnClear)

        self.btnSave = QPushButton(self.widget_6)
        self.btnSave.setObjectName(u"btnSave")
        icon6 = QIcon()
        icon6.addFile(u":/root/imgs/light-save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSave.setIcon(icon6)
        self.btnSave.setIconSize(QSize(25, 25))
        self.btnSave.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnSave)

        self.btnEdit = QPushButton(self.widget_6)
        self.btnEdit.setObjectName(u"btnEdit")
        icon7 = QIcon()
        icon7.addFile(u":/root/imgs/light-pen.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdit.setIcon(icon7)
        self.btnEdit.setIconSize(QSize(25, 25))
        self.btnEdit.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnEdit)

        self.btnDeleteDetails = QPushButton(self.widget_6)
        self.btnDeleteDetails.setObjectName(u"btnDeleteDetails")
        self.btnDeleteDetails.setIcon(icon1)
        self.btnDeleteDetails.setIconSize(QSize(25, 25))
        self.btnDeleteDetails.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnDeleteDetails)

        self.btnHide = QPushButton(self.widget_6)
        self.btnHide.setObjectName(u"btnHide")
        self.btnHide.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/root/imgs/light-eye-slash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHide.setIcon(icon8)
        self.btnHide.setIconSize(QSize(25, 25))
        self.btnHide.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btnHide)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.frameDetails = QFrame(self.widDetails)
        self.frameDetails.setObjectName(u"frameDetails")
        self.frameDetails.setFrameShape(QFrame.StyledPanel)
        self.frameDetails.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameDetails)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.frameDetails)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbType = QComboBox(self.frameDetails)
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.setObjectName(u"cbType")

        self.gridLayout.addWidget(self.cbType, 0, 1, 1, 3)

        self.btnAddCat = QPushButton(self.frameDetails)
        self.btnAddCat.setObjectName(u"btnAddCat")
        self.btnAddCat.setFont(font)
        self.btnAddCat.setStyleSheet(u"background-color: transparent")
        self.btnAddCat.setIcon(icon2)
        self.btnAddCat.setIconSize(QSize(25, 25))
        self.btnAddCat.setFlat(True)

        self.gridLayout.addWidget(self.btnAddCat, 5, 1, 1, 1)

        self.btnAddCard = QPushButton(self.frameDetails)
        self.btnAddCard.setObjectName(u"btnAddCard")
        self.btnAddCard.setFont(font)
        self.btnAddCard.setStyleSheet(u"background-color: transparent")
        self.btnAddCard.setIcon(icon2)
        self.btnAddCard.setIconSize(QSize(25, 25))
        self.btnAddCard.setFlat(True)

        self.gridLayout.addWidget(self.btnAddCard, 4, 1, 1, 1)

        self.cbCard = QComboBox(self.frameDetails)
        self.cbCard.setObjectName(u"cbCard")
        self.cbCard.setEnabled(True)
        self.cbCard.setFont(font)
        self.cbCard.setEditable(False)

        self.gridLayout.addWidget(self.cbCard, 4, 3, 1, 1)

        self.label_7 = QLabel(self.frameDetails)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.cbCat = QComboBox(self.frameDetails)
        self.cbCat.setObjectName(u"cbCat")
        self.cbCat.setFont(font)

        self.gridLayout.addWidget(self.cbCat, 5, 3, 1, 1)

        self.dtDatetime = QDateTimeEdit(self.frameDetails)
        self.dtDatetime.setObjectName(u"dtDatetime")
        self.dtDatetime.setFont(font)
        self.dtDatetime.setReadOnly(False)

        self.gridLayout.addWidget(self.dtDatetime, 3, 1, 1, 3)

        self.leTitle = QLineEdit(self.frameDetails)
        self.leTitle.setObjectName(u"leTitle")
        self.leTitle.setFont(font)

        self.gridLayout.addWidget(self.leTitle, 1, 1, 1, 3)

        self.label_9 = QLabel(self.frameDetails)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_6 = QLabel(self.frameDetails)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_8 = QLabel(self.frameDetails)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.dsVal = QDoubleSpinBox(self.frameDetails)
        self.dsVal.setObjectName(u"dsVal")
        self.dsVal.setFont(font)
        self.dsVal.setMaximum(999999999999.000000000000000)

        self.gridLayout.addWidget(self.dsVal, 2, 1, 1, 3)

        self.label_5 = QLabel(self.frameDetails)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.ptDesc = QPlainTextEdit(self.frameDetails)
        self.ptDesc.setObjectName(u"ptDesc")
        self.ptDesc.setFont(font)

        self.gridLayout.addWidget(self.ptDesc, 6, 1, 2, 3)

        self.btnEraseCard = QPushButton(self.frameDetails)
        self.btnEraseCard.setObjectName(u"btnEraseCard")
        self.btnEraseCard.setStyleSheet(u"background-color: transparent")
        self.btnEraseCard.setIcon(icon5)
        self.btnEraseCard.setIconSize(QSize(25, 25))
        self.btnEraseCard.setFlat(True)

        self.gridLayout.addWidget(self.btnEraseCard, 4, 2, 1, 1)

        self.label_4 = QLabel(self.frameDetails)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.btnEraseCat = QPushButton(self.frameDetails)
        self.btnEraseCat.setObjectName(u"btnEraseCat")
        self.btnEraseCat.setStyleSheet(u"background-color: transparent")
        self.btnEraseCat.setIcon(icon5)
        self.btnEraseCat.setIconSize(QSize(25, 25))
        self.btnEraseCat.setFlat(True)

        self.gridLayout.addWidget(self.btnEraseCat, 5, 2, 1, 1)

        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout_2.addWidget(self.frameDetails)

        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_4.addWidget(self.widDetails)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)

        self.retranslateUi(RegForm)

        QMetaObject.connectSlotsByName(RegForm)
    # setupUi

    def retranslateUi(self, RegForm):
        RegForm.setWindowTitle(QCoreApplication.translate("RegForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("RegForm", u"Registros", None))
#if QT_CONFIG(tooltip)
        self.btnParams.setToolTip(QCoreApplication.translate("RegForm", u"par\u00e2metros", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnDelete.setToolTip(QCoreApplication.translate("RegForm", u"excluir registros selecionados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnAdd.setToolTip(QCoreApplication.translate("RegForm", u"adicionar novos registros", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnPrev.setToolTip(QCoreApplication.translate("RegForm", u"voltar", None))
#endif // QT_CONFIG(tooltip)
        self.lbTableNav.setText(QCoreApplication.translate("RegForm", u"0 a 0 de 0", None))
#if QT_CONFIG(tooltip)
        self.btnNext.setToolTip(QCoreApplication.translate("RegForm", u"avan\u00e7ar", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("RegForm", u"Detalhamento", None))
#if QT_CONFIG(tooltip)
        self.btnClear.setToolTip(QCoreApplication.translate("RegForm", u"retornar valores iniciais", None))
#endif // QT_CONFIG(tooltip)
        self.btnEdit.setText("")
#if QT_CONFIG(tooltip)
        self.btnDeleteDetails.setToolTip(QCoreApplication.translate("RegForm", u"excluir registro", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnHide.setToolTip(QCoreApplication.translate("RegForm", u"ocultar", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("RegForm", u"Tipo", None))
        self.cbType.setItemText(0, QCoreApplication.translate("RegForm", u"Entrada", None))
        self.cbType.setItemText(1, QCoreApplication.translate("RegForm", u"Sa\u00edda", None))

#if QT_CONFIG(tooltip)
        self.btnAddCat.setToolTip(QCoreApplication.translate("RegForm", u"adicionar nova categoria", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnAddCard.setToolTip(QCoreApplication.translate("RegForm", u"adicionar novo cart\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("RegForm", u"Descri\u00e7\u00e3o", None))
        self.label_9.setText(QCoreApplication.translate("RegForm", u"Categoria", None))
        self.label_6.setText(QCoreApplication.translate("RegForm", u"Data Hora", None))
        self.label_8.setText(QCoreApplication.translate("RegForm", u"Cart\u00e3o", None))
        self.label_5.setText(QCoreApplication.translate("RegForm", u"T\u00edtulo", None))
#if QT_CONFIG(tooltip)
        self.btnEraseCard.setToolTip(QCoreApplication.translate("RegForm", u"remover sele\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("RegForm", u"Valor", None))
#if QT_CONFIG(tooltip)
        self.btnEraseCat.setToolTip(QCoreApplication.translate("RegForm", u"remover sele\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

