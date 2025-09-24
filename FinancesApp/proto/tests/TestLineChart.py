from PySide6.QtWidgets import QApplication
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PySide6.QtCore import QDateTime, QPointF, Qt
from PySide6.QtGui import QPainter, QPalette

app = QApplication([])
color = app.palette().color(QPalette.ColorRole.Text)

# Criar série de linha com datas
serie = QLineSeries()
serie.append(QDateTime.fromString("2025-01-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 10)
serie.append(QDateTime.fromString("2025-02-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 20)
serie.append(QDateTime.fromString("2025-03-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 15)
serie.setPointsVisible(True)

# Criar gráfico
chart = QChart()
chart.addSeries(serie)
chart.setTitle("Dados por Data")
chart.legend().hide()
chart.setBackgroundVisible(False)
chart.setTitleBrush(color)

# Eixo X com datas
eixo_x = QDateTimeAxis()
eixo_x.setFormat("dd/MM/yy")#("MMM yyyy")
eixo_x.setTitleText("Data")
eixo_x.setLabelsColor(color)
eixo_x.setTitleBrush(color)
# chart.setAxisX(eixo_x, serie)
chart.addAxis(eixo_x, Qt.AlignBottom)
serie.attachAxis(eixo_x)

# Eixo Y com valores
eixo_y = QValueAxis()
eixo_y.setTitleText("Valor")
eixo_y.setLabelsColor(color)
eixo_y.setTitleBrush(color)
# chart.setAxisY(eixo_y, serie)
chart.addAxis(eixo_y, Qt.AlignLeft)
serie.attachAxis(eixo_y)


# Visualização
chart_view = QChartView(chart)
chart_view.setRenderHint(QPainter.Antialiasing)
chart_view.resize(600, 300)
chart_view.show()

app.exec()