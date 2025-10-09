import sys

from .views.app import FinancesApp

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = sys.argv[1]

        if mode == 'test.createAccountForm':
            from .src.tests.createAccountForm import crerateAccountForm
            crerateAccountForm()

        elif mode == 'test.loginForm':
            from .src.tests.loginForm import loginForm
            loginForm()

        elif mode == 'test.loginPage':
            from .src.tests.loginPage import loginPage
            loginPage()

        elif mode == 'test.mainPage':
            from .src.tests.mainPage import mainPage
            mainPage()

        elif mode == 'test.configForm':
            from .src.tests.configForm import configForm
            configForm()

        elif mode == 'test.tableForm':
            from .src.tests.tableForm import tableForm
            tableForm()

    else:
        app = FinancesApp()
        sys.exit(app.exec())