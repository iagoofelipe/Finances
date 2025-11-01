from finances import FinancesApp
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = sys.argv[1]

        if mode == 'test.createAccountForm':
            from finances.tests.createAccountForm import crerateAccountForm
            crerateAccountForm()

        elif mode == 'test.loginForm':
            from finances.tests.loginForm import loginForm
            loginForm()

        elif mode == 'test.loginPage':
            from finances.tests.loginPage import loginPage
            loginPage()

        elif mode == 'test.homePage':
            from finances.tests.homePage import homePage
            homePage()

        elif mode == 'test.configForm':
            from finances.tests.configForm import configForm
            configForm()

        elif mode == 'test.tableForm':
            from finances.tests.tableForm import tableForm
            tableForm()

        elif mode == 'test.shareProfileDialog':
            from finances.tests.shareProfileDialog import shareProfileDialog
            shareProfileDialog()

        elif mode == 'test.registryForm':
            from finances.tests.registryForm import registryForm
            registryForm()

        elif mode == 'test.cardAccountForm':
            from finances.tests.cardAccountForm import cardAccountForm
            cardAccountForm()

    else:
        app = FinancesApp()
        sys.exit(app.exec())