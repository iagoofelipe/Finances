from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QBarSet, QHorizontalStackedBarSeries, QLineSeries, QDateTimeAxis, QValueAxis
from PySide6.QtCore import Qt, QMargins, QDateTime, Signal, QDate
from PySide6.QtGui import QPainter, QPalette, QColor, QIcon

class HBarTwoValues(QWidget):
    def __init__(self, value1:float=0, value2:float=0, title1='', title2='', parent:QWidget=None):
        super().__init__(parent)
        self.__setup(title1, title2)
        self.setValues(value1, value2)

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def setValues(self, first:float, second:float):
        self.__lbFirst.setText(f"R$ {first:.2f}")
        self.__lbSecond.setText(f"R$ {second:.2f}")
        self.__generateChart(first, second)

    def __setup(self, t1, t2):
        self.__layout = layout = QGridLayout(self)
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(10)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setRowStretch(1, 1)

        lbTitleFirst = QLabel(t1, self)
        layout.addWidget(lbTitleFirst, 0, 0, 1, 1)

        lbTitleSecond = QLabel(t2, self)
        lbTitleSecond.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(lbTitleSecond, 0, 1, 1, 1)

        self.__chartView = QWidget(self)        
        layout.addWidget(self.__chartView, 1, 0, 1, 2)

        self.__lbFirst = QLabel("R$ 0,00", self)
        layout.addWidget(self.__lbFirst, 2, 0, 1, 1)

        self.__lbSecond = QLabel("R$ 0,00", self)
        self.__lbSecond.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(self.__lbSecond, 2, 1, 1, 1)

    def __generateChart(self, v1, v2):
        self.__setFirst = QBarSet('first', color=QColor("#125B7F"))
        self.__setSecond = QBarSet('second', color=QColor("#1B88BF"))

        self.__first = v1
        self.__second = v2
        self.__setFirst << v1
        self.__setSecond << v2

        self.__serie = QHorizontalStackedBarSeries()
        self.__serie.append(self.__setFirst)
        self.__serie.append(self.__setSecond)

        chart = QChart()
        chart.addSeries(self.__serie)
        chart.setMargins(QMargins(0, 0, 0, 0))
        chart.setBackgroundVisible(False)
        chart.legend().hide()

        widOld = self.__chartView
        widNew = self.__chartView = QChartView(chart, self)
        self.__chartView.setRenderHint(QPainter.Antialiasing)
        self.__chartView.setStyleSheet("background-color: transparent")

        self.__layout.replaceWidget(widOld, widNew)
        widOld.deleteLater()