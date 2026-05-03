import sys
from API.api import get_rates
from Exchange.exchange import get_exchange_rates
from GUI.resorces.ui_fep_gui_v3 import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QObject, Signal, QThread
from DataBase.DB import DataBase
from Classes.User import User

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.currencies = [
            "USD",
            "EUR",
            "TRY",
            "GBP",
            "JPY",
            "CHF",
            "CAD",
            "AUD",
            "SAR",
            "CNY",
            "NZD"
        ]

        self.cb_base_currency.addItems(self.currencies)
        self.cb_base_currency.setCurrentText("EUR")
        self.setWindowTitle("FEP")

        self.stackedWidget.setCurrentWidget(self.login_page)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.show_register_page)
        self.register_button_2.clicked.connect(self.register)
        self.backtologin_button.clicked.connect(self.show_login_page)

        self.cb_base_currency.currentTextChanged.connect(self.update_rates)


    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        logged_user = User(username, password)
        logged_user_id = DataBase.login(logged_user)

        if not logged_user_id:
            self.username_edit.clear()
            self.password_edit.clear()

            QMessageBox.information(self,"Login Unsuccessful","Username or Password Incorrect.\nPlease try again.")

        else:
            self.show_home_page(logged_user_id)


    def register(self):
        pass

    def show_home_page(self, logged_user_id):
        self.stackedWidget.setCurrentWidget(self.home_page)
        self.load_rates()


    def show_register_page(self):
        self.stackedWidget.setCurrentWidget(self.register_page)

    def show_login_page(self):
        self.stackedWidget.setCurrentWidget(self.login_page)

    def closeEvent(self, event):
        if DataBase.con is not None:
            try:
                DataBase.close_connection()
                print("DB connection closed.")
            except Exception as e:
                print(f"DB close error: {e}")
            finally:
                DataBase.con = None
        event.accept()

    def load_rates(self):
        self.stackedWidget_2.setCurrentWidget(self.loading_page)

        self.rate_thread = QThread()
        self.rate_worker = RateWorker()

        self.rate_worker.moveToThread(self.rate_thread)

        self.rate_thread.started.connect(self.rate_worker.run)

        self.rate_worker.finished.connect(self.on_rates_loaded)
        self.rate_worker.error.connect(self.on_rates_error)

        self.rate_worker.finished.connect(self.rate_thread.quit)
        self.rate_worker.error.connect(self.rate_thread.quit)

        self.rate_worker.finished.connect(self.rate_worker.deleteLater)
        self.rate_worker.error.connect(self.rate_worker.deleteLater)
        self.rate_thread.finished.connect(self.rate_thread.deleteLater)

        self.rate_thread.start()

    def on_rates_loaded(self, rates):
        self.rates = rates

        self.update_rates()

        self.stackedWidget_2.setCurrentWidget(self.rate_page)


    def on_rates_error(self, error_message):
        self.loading_frame.hide()

        QMessageBox.warning(
            self,
            "Rate Loading Error",
            f"Rates couldn't loaded.\n\n{error_message}"
        )
        sys.exit()

    def update_rates(self):
        base_rate = self.cb_base_currency.currentText()

        rates = get_exchange_rates(self.rates,base_rate)

        eur_text = f"1 EUR = {rates['EUR']} {base_rate}"
        usd_text = f"1 USD = {rates['USD']} {base_rate}"
        gbp_text = f"1 GBP = {rates['GBP']} {base_rate}"
        jpy_text = f"1 JPY = {rates['JPY']} {base_rate}"
        chf_text = f"1 CHF = {rates['CHF']} {base_rate}"
        cad_text = f"1 CAD = {rates['CAD']} {base_rate}"
        aud_text = f"1 AUD = {rates['AUD']} {base_rate}"
        cny_text = f"1 CNY = {rates['CNY']} {base_rate}"
        try_text = f"1 TRY = {rates['TRY']} {base_rate}"
        sar_text = f"1 SAR = {rates['SAR']} {base_rate}"
        nzd_text = f"1 NZD = {rates['NZD']} {base_rate}"

        self.lbl_rate_eur.setText(eur_text)
        self.lbl_rate_usd.setText(usd_text)
        self.lbl_rate_gbp.setText(gbp_text)
        self.lbl_rate_jpy.setText(jpy_text)
        self.lbl_rate_chf.setText(chf_text)
        self.lbl_rate_cad.setText(cad_text)
        self.lbl_rate_aud.setText(aud_text)
        self.lbl_rate_cny.setText(cny_text)
        self.lbl_rate_try.setText(try_text)
        self.lbl_rate_sar.setText(sar_text)
        self.lbl_rate_nzd.setText(nzd_text)


class RateWorker(QObject):
    finished = Signal(dict)
    error = Signal(str)

    def run(self):
        try:
            rates = get_rates()
            self.finished.emit(rates)
        except Exception as e:
            self.error.emit(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())







