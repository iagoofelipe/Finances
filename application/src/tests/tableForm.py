from PySide6.QtWidgets import QApplication
from ...views.components.table import TableWidget

def tableForm():
    app = QApplication()
    view = TableWidget(
        ['Título', 'Valor'],
        'Histórico',
        TableWidget.BtnAdd | TableWidget.BtnEdit | TableWidget.ShowNavAsNeeded,
    )

    view.setData({
        'O001': ['Origem', 134],
        'O002': ['Origem', 143],
        'O003': ['Origem', 166],
        'D001': ['Destino', 3221],
        'D002': ['Destino', 2245],
    })

    view.addRequired.connect(view.getSelectedKeys)

    view.show()
    app.exec()
