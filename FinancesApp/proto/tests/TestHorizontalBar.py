from PySide6.QtWidgets import QApplication
from PySide6.QtCharts import QChart, QChartView, QBarSet, QHorizontalStackedBarSeries, QBarCategoryAxis
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QMargins

app = QApplication([])

# Criar os dois segmentos da barra
laranja = QBarSet("Laranja")
azul = QBarSet("Azul")

# Definir os valores proporcionais (ex: 90 e 10)
laranja << 90
azul << 10

# Definir cores
# laranja.setColor(QColor("#FFA500"))  # Laranja
# azul.setColor(QColor("#1E90FF"))     # Azul

# Criar série empilhada horizontal
serie = QHorizontalStackedBarSeries()
serie.append(laranja)
serie.append(azul)

# Criar gráfico
chart = QChart()
chart.addSeries(serie)
# chart.setTitle("")  # Sem título
chart.legend().hide()  # Ocultar legenda

# Definir categoria única
# categorias = [""]  # Sem rótulo
# eixo_y = QBarCategoryAxis()
# eixo_y.append(categorias)
# chart.setAxisY(eixo_y, serie)

# Eixo X automático
# chart.createDefaultAxes()

# Remover margens e fundo
# chart.setMargins(QMargins(0, 0, 0, 0))
chart.setBackgroundVisible(False)

# Criar visualização
chart_view = QChartView(chart)
chart_view.setRenderHint(QPainter.Antialiasing)
chart_view.resize(400, 100)
chart_view.show()

app.exec()