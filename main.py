import sys
import os
import shutil
from API.api import get_rates
from Exchange.exchange import get_exchange_rates, main_exn, calculate_exchange_value
from Classes.Token import Token
from GUI.resorces.ui_fep_gui_v5 import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import QObject, Signal, QThread, Qt, QSize
from PySide6.QtGui import QIcon, QPixmap
from DataBase.DB import DataBase
from Classes.User import User

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.symbols = {
            "EUR": "€",
            "USD": "$",
            "GBP": "£",
            "JPY": "¥",
            "CHF": "₣",
            "CAD": "CA$",
            "AUD": "AU$",
            "SAR": "⃁",
            "TRY": "₺",
            "CNY": "CN¥",
            "NZD": "NZ$"
        }

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
        self.profile_button.clicked.connect(self.show_profile_page)
        self.back_home_button.clicked.connect(self.show_home_page)
        self.logout_button.clicked.connect(self.show_login_page)
        self.change_foto_button.clicked.connect(self.change_profile_photo)

        self.buy_buttons = {
            "EUR": self.buy_eur_button,
            "USD": self.buy_usd_button,
            "GBP": self.buy_gbp_button,
            "JPY": self.buy_jpy_button,
            "CHF": self.buy_chf_button,
            "CAD": self.buy_cad_button,
            "AUD": self.buy_aud_button,
            "TRY": self.buy_try_button,
            "CNY": self.buy_cny_button,
            "NZD": self.buy_nzd_button,
            "SAR": self.buy_sar_button,
        }

        self.amount_spinboxes = {
            "EUR": self.dsb_amount_eur,
            "USD": self.dsb_amount_usd,
            "GBP": self.dsb_amount_gbp,
            "JPY": self.dsb_amount_jpy,
            "CHF": self.dsb_amount_chf,
            "CAD": self.dsb_amount_cad,
            "AUD": self.dsb_amount_aud,
            "TRY": self.dsb_amount_try,
            "CNY": self.dsb_amount_cny,
            "NZD": self.dsb_amount_nzd,
            "SAR": self.dsb_amount_sar,
        }

        for currency, button in self.buy_buttons.items():
            button.clicked.connect(lambda checked=False, to_rate=currency: self.buy(to_rate))

        self.cb_base_currency.currentTextChanged.connect(self.update_page)


    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        logged_user = User(username, password)
        self.user_id = DataBase.login(logged_user)

        if not self.user_id:
            self.username_edit.clear()
            self.password_edit.clear()

            QMessageBox.information(self,"Login Unsuccessful","Username or Password Incorrect.\nPlease try again.")

        else:
            self.username_prof_lbl.setText(f"User: {logged_user.user_name}")
            self.show_home_page()
            self.username_edit.clear()
            self.password_edit.clear()


    def register(self):
        username = self.registerusername_edit.text()
        password = self.registerpassword_edit.text()
        conpassword = self.conpassword_edit.text()

        if conpassword != password:
            self.registerusername_edit.clear()
            self.registerpassword_edit.clear()
            self.conpassword_edit.clear()
            QMessageBox.warning(self,"Register Unsuccessful","Password is not confirmed correctly.\nPlease try again.")
            return

        user = User(username, password)
        try:
            register = DataBase.register(user)
        except Exception as e:
            register = e
            print(register)
        finally:
            self.registerusername_edit.clear()
            self.registerpassword_edit.clear()
            self.conpassword_edit.clear()

        if register == "AlreadyRegistered":
            QMessageBox.information(self,"Register Unsuccessful","This username already exists.\nPlease try again.")
        elif register == "Registered":
            QMessageBox.information(self,"Registered","Registration Successful.\nPlease login.")
            start_token = Token("EUR",500,user.user_id)
            try:
                DataBase.add_default_pp(user.user_id)
                DataBase.add_token(start_token.token)
            except Exception as e:
                self.registerusername_edit.clear()
                self.registerpassword_edit.clear()
                self.conpassword_edit.clear()
                QMessageBox.warning(self,"Register Unsuccessful","Something went wrong.\nPlease try again.")
                print(e)
        else:
            QMessageBox.information(self,"Register Unsuccessful","Something went wrong.\nPlease try again.")
            self.stackedWidget.setCurrentWidget(self.login_page)

    def change_profile_photo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Profile Photo",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_path:
            return

        file_name = os.path.basename(file_path)

        target_base_dir = os.path.dirname(os.path.abspath(__file__))
        target_dir = os.path.join(target_base_dir,"GUI" ,"profile_photos", file_name)

        shutil.copy2(file_path, target_dir)

        DataBase.change_profile_photo(self.user_id,target_dir)
        self.set_profile_photo()


    def set_profile_photo(self):
        try:
            pp_info = DataBase.get_pp(self.user_id)
        except Exception as e:
            QMessageBox.information(self,"Profile Photo Error","Something went wrong.\nPlease try again.")
            self.stackedWidget.setCurrentWidget(self.login_page)
            print(e)
            return

        if pp_info["state"] == "Default":
            base_dir = os.path.dirname(os.path.abspath(__file__))
            pp_dir = os.path.join(base_dir, "GUI","profile_photos")
            pp_path = os.path.join(pp_dir, "Default.png")
            pixmap = QPixmap(pp_path)
        else:
            pp_path = pp_info["pp_path"]
            pixmap = QPixmap(pp_path)

        if pixmap.isNull():
            QMessageBox.warning(self,"Image Error","Image cannot found.")
            self.stackedWidget.setCurrentWidget(self.login_page)
            return

        scaled_pixmap = pixmap.scaled(
            self.profile_foto_button.width(),
            self.profile_foto_button.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.profile_foto_button.setPixmap(scaled_pixmap)
        self.profile_foto_button.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.profile_button.setText("")
        self.profile_button.setIcon(QIcon(pp_path))
        self.profile_button.setIconSize(QSize(70, 70))

    def show_home_page(self):
        self.stackedWidget.setCurrentWidget(self.home_page)
        self.load_profile(self.user_id)
        self.load_rates()

    def show_profile_page(self):
        self.stackedWidget_2.setCurrentWidget(self.profile_page)
        try:
            wallet_keys = self.wallet.keys()
        except Exception as e:
            print(e)
            return
        finally:
            text_eur = f"Portfolio: 0 EUR"
            text_usd = f"Portfolio: 0 USD"
            text_gbp = f"Portfolio: 0 GBP"
            text_jpy = f"Portfolio: 0 JPY"
            text_chf = f"Portfolio: 0 CHF"
            text_cad = f"Portfolio: 0 CAD"
            text_aud = f"Portfolio: 0 AUD"
            text_cny = f"Portfolio: 0 CNY"
            text_try = f"Portfolio: 0 TRY"
            text_sar = f"Portfolio: 0 SAR"
            text_nzd = f"Portfolio: 0 NZD"

        for i in wallet_keys:
            if i == "EUR":
                text_eur = f"Portfolio: {self.wallet[i]} EUR"
            elif i == "USD":
                text_usd = f"Portfolio: {self.wallet[i]} USD"
            elif i == "GBP":
                text_gbp = f"Portfolio: {self.wallet[i]} GBP"
            elif i == "JPY":
                text_jpy = f"Portfolio: {self.wallet[i]} JPY"
            elif i == "CHF":
                text_chf = f"Portfolio: {self.wallet[i]} CHF"
            elif i == "CAD":
                text_cad = f"Portfolio: {self.wallet[i]} CAD"
            elif i == "AUD":
                text_aud = f"Portfolio: {self.wallet[i]} AUD"
            elif i == "CNY":
                text_cny = f"Portfolio: {self.wallet[i]} CNY"
            elif i == "TRY":
                text_try = f"Portfolio: {self.wallet[i]} TRY"
            elif i == "SAR":
                text_sar = f"Portfolio: {self.wallet[i]} SAR"
            elif i == "NZD":
                text_nzd = f"Portfolio: {self.wallet[i]} NZD"

            self.lbl_rate_eur_2.setText(text_eur)
            self.lbl_rate_usd_2.setText(text_usd)
            self.lbl_rate_gbp_2.setText(text_gbp)
            self.lbl_rate_jpy_2.setText(text_jpy)
            self.lbl_rate_chf_2.setText(text_chf)
            self.lbl_rate_cad_2.setText(text_cad)
            self.lbl_rate_aud_2.setText(text_aud)
            self.lbl_rate_cny_2.setText(text_cny)
            self.lbl_rate_try_2.setText(text_try)
            self.lbl_rate_sar_2.setText(text_sar)
            self.lbl_rate_nzd_2.setText(text_nzd)


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

    def load_profile(self,user_id):
        try:
            info = DataBase.get_user_info(user_id)
        except Exception as e:
            QMessageBox.information(self,"Load Profile Error","Something went wrong while loading profile.\nPlease try again.")
            print(e)
            self.stackedWidget.setCurrentWidget(self.login_page)
            return

        username = info["user_info"][0][1]
        self.wallet = info["wallet_info"]

        self.user_info_lbl.setText(f"User: {username}")
        self.load_portfolio()
        self.set_profile_photo()

    def load_portfolio(self):
        base_rate = self.cb_base_currency.currentText()

        for i in self.wallet.keys():
            if i == base_rate:
                self.portfoilo_lbl.setText(f"Portfolio : {self.wallet[i]} {base_rate}")
                return
        self.portfoilo_lbl.setText(f"Portfolio : 0 {base_rate}")

    def on_rates_loaded(self, rates):
        self.rates = rates

        self.update_rates()

        self.stackedWidget_2.setCurrentWidget(self.rate_page)


    def on_rates_error(self, error_message):
        self.loading_page.hide()

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

    def update_page(self):
        self.update_rates()
        self.load_portfolio()

    def buy(self,to_rate):
        from_rate = self.cb_base_currency.currentText()
        value = self.amount_spinboxes[to_rate].value()

        self.exchange_info = \
            {
                "user_id": self.user_id,
                "from": from_rate,
                "to": to_rate,
                "value": value
            }

        payment_value = value * (self.rates[from_rate] / self.rates[to_rate])

        self.from_rate_lbl.setText(self.symbols[from_rate])
        self.from_rate_amount_lbl.setText(f"{payment_value} {from_rate}")

        self.to_rate_lbl.setText(self.symbols[to_rate])
        self.to_rate_amount_lbl.setText(f"{value} {to_rate}")

        self.stackedWidget_2.setCurrentWidget(self.buying_page)

        self.con_button.clicked.connect(self.exchange)
        self.dec_button.clicked.connect(self.decline)

    def exchange(self):
        self.stackedWidget_2.setCurrentWidget(self.loading_page)

        self.buy_thread = QThread()
        self.buyworker = ExchangeWorker(self.exchange_info)

        self.buyworker.moveToThread(self.buy_thread)

        self.buy_thread.started.connect(self.buyworker.run)

        self.buyworker.finished.connect(self.on_buy_success)
        self.buyworker.error.connect(self.on_buy_error)

        self.buyworker.finished.connect(self.buy_thread.quit)
        self.buyworker.error.connect(self.buy_thread.quit)

        self.buyworker.finished.connect(self.buyworker.deleteLater)
        self.buyworker.error.connect(self.buyworker.deleteLater)
        self.buy_thread.finished.connect(self.buy_thread.deleteLater)

        self.buy_thread.start()

    def on_buy_success(self,values):
        try:
            main_exn(self.exchange_info,values)
            QMessageBox.information(self, "Purchase Successful", "Purchase Completed Successfully")
            self.update_page()
            self.load_profile(self.user_id)
            self.stackedWidget_2.setCurrentWidget(self.rate_page)
        except Exception as e:
            QMessageBox.information(self, "Purchase Unsuccessful", f"Purchase Failed\n\n{e}")

    def on_buy_error(self,error):
        QMessageBox.warning(self,"Purchase Error",f"Purchase failed\n\n{error}")
        self.stackedWidget_2.setCurrentWidget(self.rate_page)

    def decline(self):
        self.stackedWidget_2.setCurrentWidget(self.rate_page)

class ExchangeWorker(QObject):
    finished = Signal(list)
    error = Signal(str)

    def __init__(self,exchange_info):
        super().__init__()

        self.exchange_info = exchange_info

    def run(self):
        try:
            values = calculate_exchange_value(self.exchange_info)
            self.finished.emit(values)
        except Exception as e:
            self.error.emit(str(e))


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

