from PySide6.QtWidgets import QWidget, QDialog, QApplication
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QBarSet, QHorizontalStackedBarSeries, QLineSeries, QDateTimeAxis, QValueAxis
from PySide6.QtCore import Qt, QMargins, QDateTime, Signal
from PySide6.QtGui import QPainter, QPalette, QColor

from ..src.ui.auto.ui_DashForm import Ui_DashForm
from .dashParamsView import DashParamsView
from ..models.structs import RegType, DashParams
from ..models.consts import DASH_DATE_START, DASH_DATE_END

class DashView(QWidget):
    paramsChanged = Signal(DashParams)

    def __init__(self, parent:QWidget = None):
        super().__init__(parent)
        self.__textColor = QApplication.instance().palette().color(QPalette.ColorRole.Text)
        self.__ui = Ui_DashForm()
        self.__params = None

        self.__ui.setupUi(self)
        self.setParams(DashParams(True, DASH_DATE_START, DASH_DATE_END, RegType.IN))
        self.__generateValuesCharts()
        self.__generateDateChart()

        self.setCategories({
            ('Jacob', 1), 
            ('Juddy', 2), 
            ('Andy', 3), 
            ('Barbara', 4), 
            ('Arrow', 5),
        })

        self.__ui.btnParams.clicked.connect(self.on_btnParams_clicked)

    def setParams(self, params:DashParams):
        regType = "Entradas" if params.regType == RegType.IN else "Saídas"
        self.__params = params

        self.__ui.lbRegType.setText(regType)
        self.__ui.lbDesc.setText(f"{params.start.toString("dd/MM/yyyy")} - {params.end.toString("dd/MM/yyyy")}")
        self.paramsChanged.emit(params)

    def getParams(self) -> DashParams:
        return self.__params

    def on_btnParams_clicked(self):
        view = DashParamsView(self.getParams(), self)

        if QDialog.DialogCode.Accepted == view.exec():
            self.setParams(view.getParams())

    def setCategories(self, values:set[tuple[str, float]]):
        series = QPieSeries()

        for v in values:
            series.append(*v)

        chart = QChart()
        chart.addSeries(series)
        chart.setMargins(QMargins(0, 0, 0, 0))
        chart.setBackgroundVisible(False)

        legend = chart.legend()
        legend.setLabelColor(self.__textColor)
        legend.setAlignment(Qt.AlignBottom)

        widOld = self.__ui.widChartCategory
        chartView = self.__ui.widChartCategory = QChartView(chart)
        chartView.setRenderHint(QPainter.RenderHint.Antialiasing)
        chartView.setStyleSheet("background-color: transparent")

        widOld.deleteLater()
        self.__ui.layoutCategory.replaceWidget(widOld, chartView)

    def __generateValuesCharts(self):
        set1 = QBarSet("Contabilizado")
        set2 = QBarSet("Pendente")

        set1 << 90
        set2 << 10

        set1.setColor(QColor("#125B7F"))
        set2.setColor(QColor("#1B88BF"))
        self.__ui.lbValRight.setText("R$ 90,00")
        self.__ui.lbValLeft.setText("R$ 10,00")

        serie = QHorizontalStackedBarSeries()
        serie.append(set1)
        serie.append(set2)

        chart = QChart()
        chart.addSeries(serie)
        chart.setMargins(QMargins(0, 0, 0, 0))
        chart.setBackgroundVisible(False)
        chart.legend().hide()

        widOld = self.__ui.widChartPercent
        chartView = self.__ui.widChartPercent = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.setStyleSheet("background-color: transparent")

        widOld.deleteLater()
        self.__ui.layoutPercent.replaceWidget(widOld, chartView)

    def __generateDateChart(self):
        # Criar série de linha com datas
        serie = QLineSeries()
        serie.append(QDateTime.fromString("2025-01-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 10)
        serie.append(QDateTime.fromString("2025-02-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 20)
        serie.append(QDateTime.fromString("2025-03-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 15)
        serie.setPointsVisible(True)

        # Criar gráfico
        chart = QChart()
        chart.addSeries(serie)
        chart.legend().hide()
        chart.setBackgroundVisible(False)

        # Eixo X com datas
        eixo_x = QDateTimeAxis()
        eixo_x.setFormat("dd/MM/yy")
        eixo_x.setTitleText("Data")
        eixo_x.setLabelsColor(self.__textColor)
        eixo_x.setTitleBrush(self.__textColor)

        chart.addAxis(eixo_x, Qt.AlignBottom)
        serie.attachAxis(eixo_x)

        # Eixo Y com valores
        eixo_y = QValueAxis()
        eixo_y.setTitleText("Valor")
        eixo_y.setLabelsColor(self.__textColor)
        eixo_y.setTitleBrush(self.__textColor)

        chart.addAxis(eixo_y, Qt.AlignLeft)
        serie.attachAxis(eixo_y)

        # Visualização
        widOld = self.__ui.widChartDate
        chartView = self.__ui.widChartDate = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.setStyleSheet("background-color: transparent")

        widOld.deleteLater()
        self.__ui.layoutValues.replaceWidget(widOld, chartView)