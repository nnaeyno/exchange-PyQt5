import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QLineEdit
from PyQt5.QtWidgets import QMainWindow

from currency_calculator import CurrencyAPI, CurrencyConverter, CurrencyService, handle_error
from login import AdminLogin
from ui_main import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.auth)
        self.ui.password.setEchoMode(QLineEdit.Password)

        self.loginService = AdminLogin()
        self.exchange_calculator = CurrencyConverter(CurrencyAPI())
        self.currency_service = CurrencyService(CurrencyAPI())

        self.init_buttons()

    def show(self):
        self.main_win.show()

    def clear(self):
        self.ui.amount_input.clear()
        self.ui.result.clear()

    def convert(self):
        result = self.exchange_calculator.convert(self.ui.from_box.currentText(), self.ui.to_box.currentText(),
                                                  self.ui.amount_input.text())
        self.ui.result.setText(f"Calculated amount: {result}")

    def log_out(self):
        self.ui.username.clear()
        self.ui.password.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.auth)

    def redirect(self):
        if self.loginService.authenticate(self.ui.username.text(), self.ui.password.text()):
            self.ui.stackedWidget.setCurrentWidget(self.ui.exchnage)
        else:
            handle_error("Credentials are invalid.", "Wrong username or password.")

    def populate_currency_combo_box(self):
        currencies = self.currency_service.get_currency_codes()

        if currencies:
            for code in currencies:
                self.ui.from_box.addItem(code)
                self.ui.to_box.addItem(code)

    def init_buttons(self):
        self.ui.login_button.clicked.connect(self.redirect)
        self.ui.logout_button.clicked.connect(self.log_out)

        self.ui.convert.clicked.connect(self.convert)
        self.ui.clear.clicked.connect(self.clear)

        self.populate_currency_combo_box()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
