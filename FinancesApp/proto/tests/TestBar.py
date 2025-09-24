from PySide6.QtWidgets import QApplication
from PySide6.QtCharts import QChart, QChartView, QBarSet, QStackedBarSeries, QBarCategoryAxis
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt

app = QApplication([])

# Criar conjuntos empilhados
parte1 = QBarSet("Parte A")
parte2 = QBarSet("Parte B")
parte3 = QBarSet("Parte C")

# Cada conjunto representa uma parte da barra empilhada
parte1 << 30
parte2 << 20
parte3 << 50

# Criar série empilhada
serie = QStackedBarSeries()
serie.append(parte1)
serie.append(parte2)
serie.append(parte3)

# Criar gráfico
chart = QChart()
chart.addSeries(serie)
chart.setTitle("Barra empilhada única")
chart.setAnimationOptions(QChart.SeriesAnimations)

# Definir categorias (eixo X)
categorias = ["Item Único"]
eixo_x = QBarCategoryAxis()
eixo_x.append(categorias)
chart.setAxisX(eixo_x, serie)

# Eixo Y automático
chart.createDefaultAxes()

# Criar visualização
chart_view = QChartView(chart)
chart_view.setRenderHint(QPainter.Antialiasing)
chart_view.resize(400, 300)
chart_view.show()

app.exec()