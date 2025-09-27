# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableParamsForm.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QLabel, QSizePolicy, QWidget)

class Ui_TableParamsForm(object):
    def setupUi(self, TableParamsForm):
        if not TableParamsForm.objectName():
            TableParamsForm.setObjectName(u"TableParamsForm")
        TableParamsForm.resize(386, 134)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        TableParamsForm.setFont(font)
        self.formLayout = QFormLayout(TableParamsForm)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(TableParamsForm)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.cbOrder = QComboBox(TableParamsForm)
        self.cbOrder.setObjectName(u"cbOrder")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cbOrder)

        self.cbAlpha = QCheckBox(TableParamsForm)
        self.cbAlpha.setObjectName(u"cbAlpha")
        self.cbAlpha.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.cbAlpha)

        self.buttonBox = QDialogButtonBox(TableParamsForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.buttonBox)

        self.gbFilters = QGroupBox(TableParamsForm)
        self.gbFilters.setObjectName(u"gbFilters")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.gbFilters)


        self.retranslateUi(TableParamsForm)
        self.buttonBox.accepted.connect(TableParamsForm.accept)
        self.buttonBox.rejected.connect(TableParamsForm.reject)

        QMetaObject.connectSlotsByName(TableParamsForm)
    # setupUi

    def retranslateUi(self, TableParamsForm):
        TableParamsForm.setWindowTitle(QCoreApplication.translate("TableParamsForm", u"Par\u00e2metros da Tabela", None))
        self.label.setText(QCoreApplication.translate("TableParamsForm", u"Ordenar por", None))
        self.cbAlpha.setText(QCoreApplication.translate("TableParamsForm", u"Alfabeticamente (do menor para o maior)", None))
        self.gbFilters.setTitle(QCoreApplication.translate("TableParamsForm", u"Filtros", None))
    # retranslateUi

