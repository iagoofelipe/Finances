from PySide6.QtWidgets import QApplication
from ...views.components.table import TableWidget

def tableForm():
    app = QApplication()
    view = TableWidget(
        ['Título', 'Valor'],
        'Histórico',
        TableWidget.BtnAdd | TableWidget.BtnEdit | TableWidget.ShowNavAsNeeded,
    )

    view.setData([
        ['Origem', 134],
        ['Destino', 3221],
        ['Destino', 3221],
        ['Destino', 3221],
        ['Destino', 3221],
        ['Destino', 3221],
        ['Destino', 3221],
    ])

    view.show()
    app.exec()
