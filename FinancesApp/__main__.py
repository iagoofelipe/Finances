from .views.app import FinancesApp, FinancesAppConsole
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'console':
        app = FinancesAppConsole()

    else:
        app = FinancesApp()
        
    app.exec()