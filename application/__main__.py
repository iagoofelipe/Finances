import sys

from .views.app import FinancesApp

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = sys.argv[1]

        if mode == 'test.createAccountForm':
            from .tests.createAccountForm import crerateAccountForm
            crerateAccountForm()

        if mode == 'test.loginForm':
            from .tests.loginForm import loginForm
            loginForm()

        if mode == 'test.loginPage':
            from .tests.loginPage import loginPage
            loginPage()

    else:
        app = FinancesApp()
        sys.exit(app.exec())