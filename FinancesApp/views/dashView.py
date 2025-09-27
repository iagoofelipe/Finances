from PySide6.QtWidgets import QWidget, QDialog, QApplication
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QLineSeries, QDateTimeAxis, QValueAxis
from PySide6.QtCore import Qt, QMargins, QDateTime, Signal
from PySide6.QtGui import QPainter, QPalette, QIcon
from typing import Sequence

from ..src.ui.auto.ui_DashForm import Ui_DashForm
from .dialog.dashParamsDialog import DashParamsDialog
from .components.HBarTwoValues import HBarTwoValues
from ..models.structs import RegType, DashParams
from ..models.tools import isDark
from ..models.consts import DASH_DATE_START, DASH_DATE_END

class DashView(QWidget):
    paramsChanged = Signal(DashParams)

    def __init__(self, parent:QWidget = None):
        super().__init__(parent)
        palette = QApplication.instance().palette()
        self.__textColor = palette.color(QPalette.ColorRole.Text)
        self.__ui = Ui_DashForm()
        self.__params = None

        self.__ui.setupUi(self)
        self.setParams(DashParams(DASH_DATE_START, DASH_DATE_END, RegType.IN))
        self.setRegValues(110, 50.5)
        self.setCardValues(10, 90)
        self.setRegDateValues({
            (QDateTime(2025, 9, 1, 0, 0, 0), 100),
            (QDateTime(2025, 9, 13, 0, 0, 0), 10),
            (QDateTime(2025, 9, 20, 0, 0, 0), 50.5),
        }, 160.5)

        self.setCategories({
            ('Jacob', 1), 
            ('Juddy', 2), 
            ('Andy', 3), 
            ('Barbara', 4), 
            ('Arrow', 5),
        })


        self.__ui.btnParams.clicked.connect(self.on_btnParams_clicked)

        # updating icons
        if isDark(): self.__ui.btnParams.setIcon(QIcon(u":/root/imgs/dark-params.svg"))

    def setParams(self, params:DashParams):
        regType = "Entradas" if params.regType == RegType.IN else "Saídas"
        self.__params = params

        self.__ui.lbRegType.setText(regType)
        self.__ui.lbDesc.setText(f"{params.start.toString("dd/MM/yyyy")} - {params.end.toString("dd/MM/yyyy")}")
        self.paramsChanged.emit(params)

    def getParams(self) -> DashParams:
        return self.__params

    def on_btnParams_clicked(self):
        view = DashParamsDialog(self.getParams(), self)

        if QDialog.DialogCode.Accepted == view.exec():
            self.setParams(view.getParams())

    def setCategories(self, values:set[tuple[str, float]]):
        series = QPieSeries()
        for v in values: series.append(*v)

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

    def setRegValues(self, accounted:float, pending:float):
        widOld = self.__ui.widRegsPercent
        widNew = self.__ui.widRegsPercent = HBarTwoValues(accounted, pending, 'Contabilizado', 'Pendente', self.__ui.frameRegs)
        self.__ui.layoutRegs.replaceWidget(widOld, widNew)
        widOld.deleteLater()

    def setCardValues(self, used:float, available:float):
        widOld = self.__ui.widCardChart
        widNew = self.__ui.widCardChart = HBarTwoValues(used, available, 'Utilizado', 'Disponível', self.__ui.frameCard)
        self.__ui.cardLayout.replaceWidget(widOld, widNew)
        widOld.deleteLater()

    def setRegDateValues(self, dates:Sequence[tuple[QDateTime, float]], total:float): 
        self.__ui.lbValue.setText(f"R$ {total:.2f}")

        # Criar série de linha com datas
        serie = QLineSeries()
        serie.setPointsVisible(True)
        for dt, val in dates: serie.append(dt.toMSecsSinceEpoch(), val)

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
        self.__ui.layoutRegs.replaceWidget(widOld, chartView)