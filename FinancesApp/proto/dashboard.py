from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QBarSet, QHorizontalStackedBarSeries, QLineSeries, QDateTimeAxis, QValueAxis
from PySide6.QtCore import Qt, QMargins, QDateTime, QDate, Signal
from PySide6.QtGui import QPainter, QPen, QPalette, QColor

from auto.ui_DashForm import Ui_DashForm
from auto.ui_DashParamsForm import Ui_DashParamsForm

REG_TYPE = int
REG_TYPE_IN = 0
REG_TYPE_OUT = 1
CURRENT_DATE = QDate.currentDate()
DASH_DATE_START = QDate(CURRENT_DATE.year(), CURRENT_DATE.month(), 1)
DASH_DATE_END = QDate(CURRENT_DATE.year(), CURRENT_DATE.month(), DASH_DATE_START.daysInMonth())

app = QApplication()

class DashParams(object):
    def __init__(self, thirdParties:bool=True, start:QDate=None, end:QDate=None, regType:REG_TYPE=None):
        self.thirdParties = thirdParties
        self.start = start
        self.end = end
        self.regType = regType

class DashParamsView(QDialog):
    def __init__(self, params:DashParams=None, parent:QWidget=None):
        super().__init__(parent, modal=True)
        self.__ui = Ui_DashParamsForm()

        self.__ui.setupUi(self)
        self.setFixedSize(450, 190)

        # setting params
        if params:
            self.__ui.cbThird.setChecked(params.thirdParties)
            self.__ui.dtStart.setDate(params.start)
            self.__ui.dtEnd.setDate(params.end)
            
            if params.regType == REG_TYPE_IN:
                self.__ui.rbIn.setChecked(True)
            else:
                self.__ui.rbOut.setChecked(True)

        else:
            self.__ui.cbThird.setChecked(True)
            self.__ui.rbIn.setChecked(True)

    def getParams(self) -> DashParams:
        return DashParams(
            self.__ui.cbThird.isChecked(),
            self.__ui.dtStart.date(),
            self.__ui.dtEnd.date(),
            REG_TYPE_IN if self.__ui.rbIn.isChecked() else REG_TYPE_OUT
        )


class DashView(QWidget):
    paramsChanged = Signal(DashParams)

    def __init__(self, parent:QWidget = None):
        super().__init__(parent)
        self.__textColor = app.palette().color(QPalette.ColorRole.Text)
        self.__ui = Ui_DashForm()
        self.__params = None

        self.__ui.setupUi(self)
        self.setParams(DashParams(start=DASH_DATE_START, end=DASH_DATE_END, regType=REG_TYPE_IN))
        self.__generateChartCateg()
        self.__generateValuesCharts()
        self.__generateDateChart()

        self.__ui.btnOptions.clicked.connect(self.on_btnOptions_clicked)

    def setParams(self, params:DashParams):
        regType = "Entradas" if params.regType == REG_TYPE_IN else "Saídas"
        self.__params = params
        self.__ui.lbDesc.setText(f"{regType} de {params.start.toString("dd/MM/yyyy")} até {params.end.toString("dd/MM/yyyy")}")

        self.paramsChanged.emit(params)

    def getParams(self) -> DashParams:
        return self.__params

    def on_btnOptions_clicked(self):
        view = DashParamsView(self.getParams(), self)

        if QDialog.DialogCode.Accepted == view.exec():
            self.setParams(view.getParams())

    def __generateChartCateg(self):
        series = QPieSeries()

        series.append('Jane', 1)
        series.append('Joe', 2)
        series.append('Andy', 3)
        series.append('Barbara', 4)
        series.append('Axel', 5)

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

def on_paramsChanged(params:DashParams):
    text = f"{"Entradas" if params.regType == REG_TYPE_IN else "Saídas"} | intervalo {params.start.toString("dd/MM/yyyy")} - {params.end.toString("dd/MM/yyyy")} | Terceiros={params.thirdParties}"
    QMessageBox(QMessageBox.Icon.Information, "Parâmetros Alterados", text).exec()

if __name__ == '__main__':
    view = DashView()
    window = QMainWindow()
    
    view.paramsChanged.connect(on_paramsChanged)
    # view.setDescription(QDate(2025, 1, 1), QDate(2025, 1, 20))
    window.setCentralWidget(view)
    window.setMinimumSize(800, 550)
    window.show()
    app.exec()