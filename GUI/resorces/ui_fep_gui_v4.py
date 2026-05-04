# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FEP_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(959, 794)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setPointSize(9)
        self.stackedWidget.setFont(font)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.gridLayout_2 = QGridLayout(self.login_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.v_space1 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_2.addItem(self.v_space1, 0, 1, 1, 1)

        self.h_space2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.h_space2, 1, 2, 1, 1)

        self.v_box1 = QVBoxLayout()
        self.v_box1.setObjectName(u"v_box1")
        self.f_box = QFormLayout()
        self.f_box.setObjectName(u"f_box")
        self.f_box.setVerticalSpacing(26)
        self.login_text = QLabel(self.login_page)
        self.login_text.setObjectName(u"login_text")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_text.sizePolicy().hasHeightForWidth())
        self.login_text.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.login_text.setFont(font1)
        self.login_text.setFocusPolicy(Qt.NoFocus)
        self.login_text.setAlignment(Qt.AlignCenter)

        self.f_box.setWidget(0, QFormLayout.ItemRole.FieldRole, self.login_text)

        self.password_edit = QLineEdit(self.login_page)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.f_box.setWidget(2, QFormLayout.ItemRole.FieldRole, self.password_edit)

        self.username_edit = QLineEdit(self.login_page)
        self.username_edit.setObjectName(u"username_edit")

        self.f_box.setWidget(1, QFormLayout.ItemRole.FieldRole, self.username_edit)

        self.login_button = QPushButton(self.login_page)
        self.login_button.setObjectName(u"login_button")

        self.f_box.setWidget(3, QFormLayout.ItemRole.FieldRole, self.login_button)

        self.register_button = QPushButton(self.login_page)
        self.register_button.setObjectName(u"register_button")

        self.f_box.setWidget(4, QFormLayout.ItemRole.FieldRole, self.register_button)


        self.v_box1.addLayout(self.f_box)


        self.gridLayout_2.addLayout(self.v_box1, 1, 1, 1, 1)

        self.v_space2 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_2.addItem(self.v_space2, 2, 1, 1, 1)

        self.h_space1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.h_space1, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.register_page.sizePolicy().hasHeightForWidth())
        self.register_page.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.register_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.h_space_r2 = QSpacerItem(290, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.h_space_r2, 1, 2, 1, 1)

        self.v_space_r1 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.v_space_r1, 2, 1, 1, 1)

        self.v_box_re = QVBoxLayout()
        self.v_box_re.setObjectName(u"v_box_re")
        self.f_box_re = QFormLayout()
        self.f_box_re.setObjectName(u"f_box_re")
        self.f_box_re.setVerticalSpacing(26)
        self.register_text = QLabel(self.register_page)
        self.register_text.setObjectName(u"register_text")
        sizePolicy.setHeightForWidth(self.register_text.sizePolicy().hasHeightForWidth())
        self.register_text.setSizePolicy(sizePolicy)
        self.register_text.setFont(font1)
        self.register_text.setAlignment(Qt.AlignCenter)

        self.f_box_re.setWidget(0, QFormLayout.ItemRole.FieldRole, self.register_text)

        self.conpassword_edit = QLineEdit(self.register_page)
        self.conpassword_edit.setObjectName(u"conpassword_edit")
        self.conpassword_edit.setEchoMode(QLineEdit.Password)

        self.f_box_re.setWidget(3, QFormLayout.ItemRole.FieldRole, self.conpassword_edit)

        self.registerpassword_edit = QLineEdit(self.register_page)
        self.registerpassword_edit.setObjectName(u"registerpassword_edit")
        self.registerpassword_edit.setEchoMode(QLineEdit.Password)

        self.f_box_re.setWidget(2, QFormLayout.ItemRole.FieldRole, self.registerpassword_edit)

        self.registerusername_edit = QLineEdit(self.register_page)
        self.registerusername_edit.setObjectName(u"registerusername_edit")

        self.f_box_re.setWidget(1, QFormLayout.ItemRole.FieldRole, self.registerusername_edit)

        self.backtologin_button = QPushButton(self.register_page)
        self.backtologin_button.setObjectName(u"backtologin_button")

        self.f_box_re.setWidget(5, QFormLayout.ItemRole.FieldRole, self.backtologin_button)

        self.register_button_2 = QPushButton(self.register_page)
        self.register_button_2.setObjectName(u"register_button_2")

        self.f_box_re.setWidget(4, QFormLayout.ItemRole.FieldRole, self.register_button_2)


        self.v_box_re.addLayout(self.f_box_re)


        self.gridLayout_3.addLayout(self.v_box_re, 1, 1, 1, 1)

        self.h_space_r1 = QSpacerItem(290, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.h_space_r1, 1, 0, 1, 1)

        self.v_space_r2 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.v_space_r2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.register_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.gridLayout_4 = QGridLayout(self.home_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget_2 = QStackedWidget(self.home_page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.rate_page = QWidget()
        self.rate_page.setObjectName(u"rate_page")
        self.verticalLayout_53 = QVBoxLayout(self.rate_page)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.header_frame = QFrame(self.rate_page)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 70))
        self.header_frame.setMaximumSize(QSize(16777215, 100))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lbl_base_rate = QLabel(self.header_frame)
        self.lbl_base_rate.setObjectName(u"lbl_base_rate")

        self.horizontalLayout_24.addWidget(self.lbl_base_rate)

        self.cb_base_currency = QComboBox(self.header_frame)
        self.cb_base_currency.setObjectName(u"cb_base_currency")

        self.horizontalLayout_24.addWidget(self.cb_base_currency)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_24)

        self.user_lbl_frame = QFrame(self.header_frame)
        self.user_lbl_frame.setObjectName(u"user_lbl_frame")
        sizePolicy1.setHeightForWidth(self.user_lbl_frame.sizePolicy().hasHeightForWidth())
        self.user_lbl_frame.setSizePolicy(sizePolicy1)
        self.user_lbl_frame.setFrameShape(QFrame.StyledPanel)
        self.user_lbl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.user_lbl_frame)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.v_spacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.v_spacer_3)

        self.user_info_lbl = QLabel(self.user_lbl_frame)
        self.user_info_lbl.setObjectName(u"user_info_lbl")

        self.verticalLayout_52.addWidget(self.user_info_lbl)

        self.portfoilo_lbl = QLabel(self.user_lbl_frame)
        self.portfoilo_lbl.setObjectName(u"portfoilo_lbl")

        self.verticalLayout_52.addWidget(self.portfoilo_lbl)

        self.v_spacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.v_spacer_4)


        self.horizontalLayout_24.addWidget(self.user_lbl_frame)

        self.profile_button = QToolButton(self.header_frame)
        self.profile_button.setObjectName(u"profile_button")
        sizePolicy1.setHeightForWidth(self.profile_button.sizePolicy().hasHeightForWidth())
        self.profile_button.setSizePolicy(sizePolicy1)
        self.profile_button.setMinimumSize(QSize(70, 70))
        self.profile_button.setMaximumSize(QSize(70, 70))

        self.horizontalLayout_24.addWidget(self.profile_button)


        self.verticalLayout_51.addWidget(self.header_frame)


        self.verticalLayout_53.addLayout(self.verticalLayout_51)

        self.scroll_area_currencies = QScrollArea(self.rate_page)
        self.scroll_area_currencies.setObjectName(u"scroll_area_currencies")
        self.scroll_area_currencies.setWidgetResizable(True)
        self.scroll_content_currencies = QWidget()
        self.scroll_content_currencies.setObjectName(u"scroll_content_currencies")
        self.scroll_content_currencies.setGeometry(QRect(0, 0, 870, 1192))
        self.verticalLayout_16 = QVBoxLayout(self.scroll_content_currencies)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.card_eur = QFrame(self.scroll_content_currencies)
        self.card_eur.setObjectName(u"card_eur")
        self.card_eur.setMinimumSize(QSize(0, 100))
        self.card_eur.setMaximumSize(QSize(16777215, 120))
        self.card_eur.setFrameShape(QFrame.StyledPanel)
        self.card_eur.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.card_eur)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lbl_icon_eur = QLabel(self.card_eur)
        self.lbl_icon_eur.setObjectName(u"lbl_icon_eur")
        self.lbl_icon_eur.setMinimumSize(QSize(70, 70))
        font2 = QFont()
        font2.setPointSize(15)
        self.lbl_icon_eur.setFont(font2)
        self.lbl_icon_eur.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lbl_icon_eur)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.lbl_name_eur = QLabel(self.card_eur)
        self.lbl_name_eur.setObjectName(u"lbl_name_eur")
        self.lbl_name_eur.setMinimumSize(QSize(0, 0))

        self.verticalLayout_18.addWidget(self.lbl_name_eur)

        self.lbl_rate_eur = QLabel(self.card_eur)
        self.lbl_rate_eur.setObjectName(u"lbl_rate_eur")
        self.lbl_rate_eur.setMinimumSize(QSize(0, 0))

        self.verticalLayout_18.addWidget(self.lbl_rate_eur)


        self.horizontalLayout_13.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_13 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.buy_eur_button = QPushButton(self.card_eur)
        self.buy_eur_button.setObjectName(u"buy_eur_button")

        self.verticalLayout_21.addWidget(self.buy_eur_button)

        self.dsb_amount_eur = QDoubleSpinBox(self.card_eur)
        self.dsb_amount_eur.setObjectName(u"dsb_amount_eur")
        self.dsb_amount_eur.setMinimum(1.000000000000000)

        self.verticalLayout_21.addWidget(self.dsb_amount_eur)


        self.horizontalLayout_13.addLayout(self.verticalLayout_21)


        self.verticalLayout_16.addWidget(self.card_eur)

        self.card_usd = QFrame(self.scroll_content_currencies)
        self.card_usd.setObjectName(u"card_usd")
        self.card_usd.setMinimumSize(QSize(0, 100))
        self.card_usd.setMaximumSize(QSize(16777215, 120))
        self.card_usd.setFrameShape(QFrame.StyledPanel)
        self.card_usd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.card_usd)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lbl_icon_usd = QLabel(self.card_usd)
        self.lbl_icon_usd.setObjectName(u"lbl_icon_usd")
        self.lbl_icon_usd.setMinimumSize(QSize(70, 70))
        self.lbl_icon_usd.setFont(font2)
        self.lbl_icon_usd.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lbl_icon_usd)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.lbl_name_usd = QLabel(self.card_usd)
        self.lbl_name_usd.setObjectName(u"lbl_name_usd")
        self.lbl_name_usd.setMinimumSize(QSize(0, 0))

        self.verticalLayout_19.addWidget(self.lbl_name_usd)

        self.lbl_rate_usd = QLabel(self.card_usd)
        self.lbl_rate_usd.setObjectName(u"lbl_rate_usd")
        self.lbl_rate_usd.setMinimumSize(QSize(0, 0))

        self.verticalLayout_19.addWidget(self.lbl_rate_usd)


        self.horizontalLayout_14.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_14 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.buy_usd_button = QPushButton(self.card_usd)
        self.buy_usd_button.setObjectName(u"buy_usd_button")

        self.verticalLayout_32.addWidget(self.buy_usd_button)

        self.dsb_amount_usd = QDoubleSpinBox(self.card_usd)
        self.dsb_amount_usd.setObjectName(u"dsb_amount_usd")
        self.dsb_amount_usd.setMinimum(1.000000000000000)

        self.verticalLayout_32.addWidget(self.dsb_amount_usd)


        self.horizontalLayout_14.addLayout(self.verticalLayout_32)


        self.verticalLayout_16.addWidget(self.card_usd)

        self.card_gbp = QFrame(self.scroll_content_currencies)
        self.card_gbp.setObjectName(u"card_gbp")
        self.card_gbp.setMinimumSize(QSize(0, 100))
        self.card_gbp.setMaximumSize(QSize(16777215, 120))
        self.card_gbp.setFrameShape(QFrame.StyledPanel)
        self.card_gbp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.card_gbp)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lbl_icon_gbp = QLabel(self.card_gbp)
        self.lbl_icon_gbp.setObjectName(u"lbl_icon_gbp")
        self.lbl_icon_gbp.setMinimumSize(QSize(70, 70))
        self.lbl_icon_gbp.setFont(font2)
        self.lbl_icon_gbp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lbl_icon_gbp)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.lbl_name_gbp = QLabel(self.card_gbp)
        self.lbl_name_gbp.setObjectName(u"lbl_name_gbp")
        self.lbl_name_gbp.setMinimumSize(QSize(0, 0))

        self.verticalLayout_33.addWidget(self.lbl_name_gbp)

        self.lbl_rate_gbp = QLabel(self.card_gbp)
        self.lbl_rate_gbp.setObjectName(u"lbl_rate_gbp")
        self.lbl_rate_gbp.setMinimumSize(QSize(0, 0))

        self.verticalLayout_33.addWidget(self.lbl_rate_gbp)


        self.horizontalLayout_15.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_15 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.buy_gbp_button = QPushButton(self.card_gbp)
        self.buy_gbp_button.setObjectName(u"buy_gbp_button")

        self.verticalLayout_34.addWidget(self.buy_gbp_button)

        self.dsb_amount_gbp = QDoubleSpinBox(self.card_gbp)
        self.dsb_amount_gbp.setObjectName(u"dsb_amount_gbp")
        self.dsb_amount_gbp.setMinimum(1.000000000000000)

        self.verticalLayout_34.addWidget(self.dsb_amount_gbp)


        self.horizontalLayout_15.addLayout(self.verticalLayout_34)


        self.verticalLayout_16.addWidget(self.card_gbp)

        self.card_jpy = QFrame(self.scroll_content_currencies)
        self.card_jpy.setObjectName(u"card_jpy")
        self.card_jpy.setMinimumSize(QSize(0, 100))
        self.card_jpy.setMaximumSize(QSize(16777215, 120))
        self.card_jpy.setFrameShape(QFrame.StyledPanel)
        self.card_jpy.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.card_jpy)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lbl_icon_jpy = QLabel(self.card_jpy)
        self.lbl_icon_jpy.setObjectName(u"lbl_icon_jpy")
        self.lbl_icon_jpy.setMinimumSize(QSize(70, 70))
        self.lbl_icon_jpy.setFont(font2)
        self.lbl_icon_jpy.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lbl_icon_jpy)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.lbl_name_jpy = QLabel(self.card_jpy)
        self.lbl_name_jpy.setObjectName(u"lbl_name_jpy")
        self.lbl_name_jpy.setMinimumSize(QSize(0, 0))

        self.verticalLayout_35.addWidget(self.lbl_name_jpy)

        self.lbl_rate_jpy = QLabel(self.card_jpy)
        self.lbl_rate_jpy.setObjectName(u"lbl_rate_jpy")
        self.lbl_rate_jpy.setMinimumSize(QSize(0, 0))

        self.verticalLayout_35.addWidget(self.lbl_rate_jpy)


        self.horizontalLayout_16.addLayout(self.verticalLayout_35)

        self.horizontalSpacer_16 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.buy_jpy_button = QPushButton(self.card_jpy)
        self.buy_jpy_button.setObjectName(u"buy_jpy_button")

        self.verticalLayout_36.addWidget(self.buy_jpy_button)

        self.dsb_amount_jpy = QDoubleSpinBox(self.card_jpy)
        self.dsb_amount_jpy.setObjectName(u"dsb_amount_jpy")
        self.dsb_amount_jpy.setMinimum(1.000000000000000)

        self.verticalLayout_36.addWidget(self.dsb_amount_jpy)


        self.horizontalLayout_16.addLayout(self.verticalLayout_36)


        self.verticalLayout_16.addWidget(self.card_jpy)

        self.card_chf = QFrame(self.scroll_content_currencies)
        self.card_chf.setObjectName(u"card_chf")
        self.card_chf.setMinimumSize(QSize(0, 100))
        self.card_chf.setMaximumSize(QSize(16777215, 120))
        self.card_chf.setFrameShape(QFrame.StyledPanel)
        self.card_chf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.card_chf)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lbl_icon_chf = QLabel(self.card_chf)
        self.lbl_icon_chf.setObjectName(u"lbl_icon_chf")
        self.lbl_icon_chf.setMinimumSize(QSize(70, 70))
        self.lbl_icon_chf.setFont(font2)
        self.lbl_icon_chf.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.lbl_icon_chf)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.lbl_name_chf = QLabel(self.card_chf)
        self.lbl_name_chf.setObjectName(u"lbl_name_chf")
        self.lbl_name_chf.setMinimumSize(QSize(0, 0))

        self.verticalLayout_37.addWidget(self.lbl_name_chf)

        self.lbl_rate_chf = QLabel(self.card_chf)
        self.lbl_rate_chf.setObjectName(u"lbl_rate_chf")
        self.lbl_rate_chf.setMinimumSize(QSize(0, 0))

        self.verticalLayout_37.addWidget(self.lbl_rate_chf)


        self.horizontalLayout_17.addLayout(self.verticalLayout_37)

        self.horizontalSpacer_17 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.buy_chf_button = QPushButton(self.card_chf)
        self.buy_chf_button.setObjectName(u"buy_chf_button")

        self.verticalLayout_38.addWidget(self.buy_chf_button)

        self.dsb_amount_chf = QDoubleSpinBox(self.card_chf)
        self.dsb_amount_chf.setObjectName(u"dsb_amount_chf")
        self.dsb_amount_chf.setMinimum(1.000000000000000)

        self.verticalLayout_38.addWidget(self.dsb_amount_chf)


        self.horizontalLayout_17.addLayout(self.verticalLayout_38)


        self.verticalLayout_16.addWidget(self.card_chf)

        self.card_cad = QFrame(self.scroll_content_currencies)
        self.card_cad.setObjectName(u"card_cad")
        self.card_cad.setMinimumSize(QSize(0, 100))
        self.card_cad.setMaximumSize(QSize(16777215, 120))
        self.card_cad.setFrameShape(QFrame.StyledPanel)
        self.card_cad.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.card_cad)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lbl_icon_cad = QLabel(self.card_cad)
        self.lbl_icon_cad.setObjectName(u"lbl_icon_cad")
        self.lbl_icon_cad.setMinimumSize(QSize(70, 70))
        font3 = QFont()
        font3.setPointSize(12)
        self.lbl_icon_cad.setFont(font3)
        self.lbl_icon_cad.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.lbl_icon_cad)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.lbl_name_cad = QLabel(self.card_cad)
        self.lbl_name_cad.setObjectName(u"lbl_name_cad")
        self.lbl_name_cad.setMinimumSize(QSize(0, 0))

        self.verticalLayout_39.addWidget(self.lbl_name_cad)

        self.lbl_rate_cad = QLabel(self.card_cad)
        self.lbl_rate_cad.setObjectName(u"lbl_rate_cad")
        self.lbl_rate_cad.setMinimumSize(QSize(0, 0))

        self.verticalLayout_39.addWidget(self.lbl_rate_cad)


        self.horizontalLayout_18.addLayout(self.verticalLayout_39)

        self.horizontalSpacer_18 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.buy_cad_button = QPushButton(self.card_cad)
        self.buy_cad_button.setObjectName(u"buy_cad_button")

        self.verticalLayout_40.addWidget(self.buy_cad_button)

        self.dsb_amount_cad = QDoubleSpinBox(self.card_cad)
        self.dsb_amount_cad.setObjectName(u"dsb_amount_cad")
        self.dsb_amount_cad.setMinimum(1.000000000000000)

        self.verticalLayout_40.addWidget(self.dsb_amount_cad)


        self.horizontalLayout_18.addLayout(self.verticalLayout_40)


        self.verticalLayout_16.addWidget(self.card_cad)

        self.card_aud = QFrame(self.scroll_content_currencies)
        self.card_aud.setObjectName(u"card_aud")
        self.card_aud.setMinimumSize(QSize(0, 100))
        self.card_aud.setMaximumSize(QSize(16777215, 120))
        self.card_aud.setAutoFillBackground(False)
        self.card_aud.setFrameShape(QFrame.StyledPanel)
        self.card_aud.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.card_aud)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lbl_icon_aud = QLabel(self.card_aud)
        self.lbl_icon_aud.setObjectName(u"lbl_icon_aud")
        self.lbl_icon_aud.setMinimumSize(QSize(70, 70))
        self.lbl_icon_aud.setFont(font3)
        self.lbl_icon_aud.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.lbl_icon_aud)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.lbl_name_aud = QLabel(self.card_aud)
        self.lbl_name_aud.setObjectName(u"lbl_name_aud")
        self.lbl_name_aud.setMinimumSize(QSize(0, 0))

        self.verticalLayout_41.addWidget(self.lbl_name_aud)

        self.lbl_rate_aud = QLabel(self.card_aud)
        self.lbl_rate_aud.setObjectName(u"lbl_rate_aud")
        self.lbl_rate_aud.setMinimumSize(QSize(0, 0))

        self.verticalLayout_41.addWidget(self.lbl_rate_aud)


        self.horizontalLayout_19.addLayout(self.verticalLayout_41)

        self.horizontalSpacer_19 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.buy_aud_button = QPushButton(self.card_aud)
        self.buy_aud_button.setObjectName(u"buy_aud_button")

        self.verticalLayout_42.addWidget(self.buy_aud_button)

        self.dsb_amount_aud = QDoubleSpinBox(self.card_aud)
        self.dsb_amount_aud.setObjectName(u"dsb_amount_aud")
        self.dsb_amount_aud.setMinimum(1.000000000000000)

        self.verticalLayout_42.addWidget(self.dsb_amount_aud)


        self.horizontalLayout_19.addLayout(self.verticalLayout_42)


        self.verticalLayout_16.addWidget(self.card_aud)

        self.card_cny = QFrame(self.scroll_content_currencies)
        self.card_cny.setObjectName(u"card_cny")
        self.card_cny.setMinimumSize(QSize(0, 100))
        self.card_cny.setMaximumSize(QSize(16777215, 120))
        self.card_cny.setFrameShape(QFrame.StyledPanel)
        self.card_cny.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.card_cny)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lbl_icon_cny = QLabel(self.card_cny)
        self.lbl_icon_cny.setObjectName(u"lbl_icon_cny")
        self.lbl_icon_cny.setMinimumSize(QSize(70, 70))
        self.lbl_icon_cny.setFont(font3)
        self.lbl_icon_cny.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lbl_icon_cny)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.lbl_name_cny = QLabel(self.card_cny)
        self.lbl_name_cny.setObjectName(u"lbl_name_cny")
        self.lbl_name_cny.setMinimumSize(QSize(0, 0))

        self.verticalLayout_43.addWidget(self.lbl_name_cny)

        self.lbl_rate_cny = QLabel(self.card_cny)
        self.lbl_rate_cny.setObjectName(u"lbl_rate_cny")
        self.lbl_rate_cny.setMinimumSize(QSize(0, 0))

        self.verticalLayout_43.addWidget(self.lbl_rate_cny)


        self.horizontalLayout_20.addLayout(self.verticalLayout_43)

        self.horizontalSpacer_20 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.buy_cny_button = QPushButton(self.card_cny)
        self.buy_cny_button.setObjectName(u"buy_cny_button")

        self.verticalLayout_44.addWidget(self.buy_cny_button)

        self.dsb_amount_cny = QDoubleSpinBox(self.card_cny)
        self.dsb_amount_cny.setObjectName(u"dsb_amount_cny")
        self.dsb_amount_cny.setMinimum(1.000000000000000)

        self.verticalLayout_44.addWidget(self.dsb_amount_cny)


        self.horizontalLayout_20.addLayout(self.verticalLayout_44)


        self.verticalLayout_16.addWidget(self.card_cny)

        self.card_try = QFrame(self.scroll_content_currencies)
        self.card_try.setObjectName(u"card_try")
        self.card_try.setMinimumSize(QSize(0, 100))
        self.card_try.setMaximumSize(QSize(16777215, 120))
        self.card_try.setFrameShape(QFrame.StyledPanel)
        self.card_try.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.card_try)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lbl_icon_try = QLabel(self.card_try)
        self.lbl_icon_try.setObjectName(u"lbl_icon_try")
        self.lbl_icon_try.setMinimumSize(QSize(70, 70))
        self.lbl_icon_try.setFont(font2)
        self.lbl_icon_try.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lbl_icon_try)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.lbl_name_try = QLabel(self.card_try)
        self.lbl_name_try.setObjectName(u"lbl_name_try")
        self.lbl_name_try.setMinimumSize(QSize(0, 0))

        self.verticalLayout_45.addWidget(self.lbl_name_try)

        self.lbl_rate_try = QLabel(self.card_try)
        self.lbl_rate_try.setObjectName(u"lbl_rate_try")
        self.lbl_rate_try.setMinimumSize(QSize(0, 0))

        self.verticalLayout_45.addWidget(self.lbl_rate_try)


        self.horizontalLayout_21.addLayout(self.verticalLayout_45)

        self.horizontalSpacer_21 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.buy_try_button = QPushButton(self.card_try)
        self.buy_try_button.setObjectName(u"buy_try_button")

        self.verticalLayout_46.addWidget(self.buy_try_button)

        self.dsb_amount_try = QDoubleSpinBox(self.card_try)
        self.dsb_amount_try.setObjectName(u"dsb_amount_try")
        self.dsb_amount_try.setMinimum(1.000000000000000)

        self.verticalLayout_46.addWidget(self.dsb_amount_try)


        self.horizontalLayout_21.addLayout(self.verticalLayout_46)


        self.verticalLayout_16.addWidget(self.card_try)

        self.card_sar = QFrame(self.scroll_content_currencies)
        self.card_sar.setObjectName(u"card_sar")
        self.card_sar.setMinimumSize(QSize(0, 100))
        self.card_sar.setMaximumSize(QSize(16777215, 120))
        self.card_sar.setFrameShape(QFrame.StyledPanel)
        self.card_sar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.card_sar)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lbl_icon_sar = QLabel(self.card_sar)
        self.lbl_icon_sar.setObjectName(u"lbl_icon_sar")
        self.lbl_icon_sar.setMinimumSize(QSize(70, 70))
        self.lbl_icon_sar.setFont(font2)
        self.lbl_icon_sar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.lbl_icon_sar)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.lbl_name_sar = QLabel(self.card_sar)
        self.lbl_name_sar.setObjectName(u"lbl_name_sar")
        self.lbl_name_sar.setMinimumSize(QSize(0, 0))

        self.verticalLayout_47.addWidget(self.lbl_name_sar)

        self.lbl_rate_sar = QLabel(self.card_sar)
        self.lbl_rate_sar.setObjectName(u"lbl_rate_sar")
        self.lbl_rate_sar.setMinimumSize(QSize(0, 0))

        self.verticalLayout_47.addWidget(self.lbl_rate_sar)


        self.horizontalLayout_22.addLayout(self.verticalLayout_47)

        self.horizontalSpacer_22 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_22)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.buy_sar_button = QPushButton(self.card_sar)
        self.buy_sar_button.setObjectName(u"buy_sar_button")

        self.verticalLayout_48.addWidget(self.buy_sar_button)

        self.dsb_amount_sar = QDoubleSpinBox(self.card_sar)
        self.dsb_amount_sar.setObjectName(u"dsb_amount_sar")
        self.dsb_amount_sar.setMinimum(1.000000000000000)

        self.verticalLayout_48.addWidget(self.dsb_amount_sar)


        self.horizontalLayout_22.addLayout(self.verticalLayout_48)


        self.verticalLayout_16.addWidget(self.card_sar)

        self.card_nzd = QFrame(self.scroll_content_currencies)
        self.card_nzd.setObjectName(u"card_nzd")
        self.card_nzd.setMinimumSize(QSize(0, 100))
        self.card_nzd.setMaximumSize(QSize(16777215, 120))
        self.card_nzd.setFrameShape(QFrame.StyledPanel)
        self.card_nzd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.card_nzd)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lbl_icon_nzd = QLabel(self.card_nzd)
        self.lbl_icon_nzd.setObjectName(u"lbl_icon_nzd")
        self.lbl_icon_nzd.setMinimumSize(QSize(70, 70))
        self.lbl_icon_nzd.setFont(font3)
        self.lbl_icon_nzd.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.lbl_icon_nzd)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.lbl_name_nzd = QLabel(self.card_nzd)
        self.lbl_name_nzd.setObjectName(u"lbl_name_nzd")
        self.lbl_name_nzd.setMinimumSize(QSize(0, 0))

        self.verticalLayout_49.addWidget(self.lbl_name_nzd)

        self.lbl_rate_nzd = QLabel(self.card_nzd)
        self.lbl_rate_nzd.setObjectName(u"lbl_rate_nzd")
        self.lbl_rate_nzd.setMinimumSize(QSize(0, 0))

        self.verticalLayout_49.addWidget(self.lbl_rate_nzd)


        self.horizontalLayout_23.addLayout(self.verticalLayout_49)

        self.horizontalSpacer_23 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_23)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.buy_nzd_button = QPushButton(self.card_nzd)
        self.buy_nzd_button.setObjectName(u"buy_nzd_button")

        self.verticalLayout_50.addWidget(self.buy_nzd_button)

        self.dsb_amount_nzd = QDoubleSpinBox(self.card_nzd)
        self.dsb_amount_nzd.setObjectName(u"dsb_amount_nzd")
        self.dsb_amount_nzd.setMinimum(1.000000000000000)

        self.verticalLayout_50.addWidget(self.dsb_amount_nzd)


        self.horizontalLayout_23.addLayout(self.verticalLayout_50)


        self.verticalLayout_16.addWidget(self.card_nzd)

        self.scroll_area_currencies.setWidget(self.scroll_content_currencies)

        self.verticalLayout_53.addWidget(self.scroll_area_currencies)

        self.verticalLayout_53.setStretch(1, 6)
        self.stackedWidget_2.addWidget(self.rate_page)
        self.loading_page = QWidget()
        self.loading_page.setObjectName(u"loading_page")
        self.gridLayout_7 = QGridLayout(self.loading_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.lbl_loading_rates_2 = QLabel(self.loading_page)
        self.lbl_loading_rates_2.setObjectName(u"lbl_loading_rates_2")
        font4 = QFont()
        font4.setPointSize(11)
        self.lbl_loading_rates_2.setFont(font4)
        self.lbl_loading_rates_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_loading_rates_2)

        self.loading_bar_2 = QProgressBar(self.loading_page)
        self.loading_bar_2.setObjectName(u"loading_bar_2")
        self.loading_bar_2.setMaximum(0)
        self.loading_bar_2.setValue(-1)
        self.loading_bar_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.loading_bar_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.gridLayout_7.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.loading_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.gridLayout_5 = QGridLayout(self.profile_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.h_box = QHBoxLayout()
        self.h_box.setObjectName(u"h_box")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.back_home_button = QPushButton(self.profile_page)
        self.back_home_button.setObjectName(u"back_home_button")

        self.verticalLayout_2.addWidget(self.back_home_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.h_box.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.h_box.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.username_prof_lbl = QLabel(self.profile_page)
        self.username_prof_lbl.setObjectName(u"username_prof_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.username_prof_lbl.sizePolicy().hasHeightForWidth())
        self.username_prof_lbl.setSizePolicy(sizePolicy2)
        self.username_prof_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.username_prof_lbl)

        self.change_foto_button = QPushButton(self.profile_page)
        self.change_foto_button.setObjectName(u"change_foto_button")
        sizePolicy2.setHeightForWidth(self.change_foto_button.sizePolicy().hasHeightForWidth())
        self.change_foto_button.setSizePolicy(sizePolicy2)
        self.change_foto_button.setMinimumSize(QSize(150, 0))

        self.verticalLayout.addWidget(self.change_foto_button)

        self.logout_button = QPushButton(self.profile_page)
        self.logout_button.setObjectName(u"logout_button")

        self.verticalLayout.addWidget(self.logout_button)


        self.h_box.addLayout(self.verticalLayout)

        self.profile_foto_button = QLabel(self.profile_page)
        self.profile_foto_button.setObjectName(u"profile_foto_button")
        self.profile_foto_button.setMinimumSize(QSize(150, 150))
        self.profile_foto_button.setMaximumSize(QSize(150, 150))
        self.profile_foto_button.setAlignment(Qt.AlignCenter)

        self.h_box.addWidget(self.profile_foto_button)


        self.gridLayout_5.addLayout(self.h_box, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.profile_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 870, 657))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.card_eur_usd = QFrame(self.scrollAreaWidgetContents)
        self.card_eur_usd.setObjectName(u"card_eur_usd")
        self.card_eur_usd.setMinimumSize(QSize(0, 100))
        self.card_eur_usd.setMaximumSize(QSize(16777215, 120))
        self.card_eur_usd.setFrameShape(QFrame.StyledPanel)
        self.card_eur_usd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.card_eur_usd)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lbl_icon_eur_2 = QLabel(self.card_eur_usd)
        self.lbl_icon_eur_2.setObjectName(u"lbl_icon_eur_2")
        self.lbl_icon_eur_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_eur_2.setFont(font2)
        self.lbl_icon_eur_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.lbl_icon_eur_2)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.lbl_name_eur_2 = QLabel(self.card_eur_usd)
        self.lbl_name_eur_2.setObjectName(u"lbl_name_eur_2")
        self.lbl_name_eur_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_20.addWidget(self.lbl_name_eur_2)

        self.lbl_rate_eur_2 = QLabel(self.card_eur_usd)
        self.lbl_rate_eur_2.setObjectName(u"lbl_rate_eur_2")
        self.lbl_rate_eur_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_20.addWidget(self.lbl_rate_eur_2)


        self.horizontalLayout_26.addLayout(self.verticalLayout_20)

        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_4)

        self.lbl_icon_usd_2 = QLabel(self.card_eur_usd)
        self.lbl_icon_usd_2.setObjectName(u"lbl_icon_usd_2")
        self.lbl_icon_usd_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_usd_2.setFont(font2)
        self.lbl_icon_usd_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.lbl_icon_usd_2)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.lbl_name_usd_2 = QLabel(self.card_eur_usd)
        self.lbl_name_usd_2.setObjectName(u"lbl_name_usd_2")
        self.lbl_name_usd_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_23.addWidget(self.lbl_name_usd_2)

        self.lbl_rate_usd_2 = QLabel(self.card_eur_usd)
        self.lbl_rate_usd_2.setObjectName(u"lbl_rate_usd_2")
        self.lbl_rate_usd_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_23.addWidget(self.lbl_rate_usd_2)


        self.horizontalLayout_26.addLayout(self.verticalLayout_23)


        self.verticalLayout_3.addWidget(self.card_eur_usd)

        self.card_gbp_2 = QFrame(self.scrollAreaWidgetContents)
        self.card_gbp_2.setObjectName(u"card_gbp_2")
        self.card_gbp_2.setMinimumSize(QSize(0, 100))
        self.card_gbp_2.setMaximumSize(QSize(16777215, 120))
        self.card_gbp_2.setFrameShape(QFrame.StyledPanel)
        self.card_gbp_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.card_gbp_2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lbl_icon_gbp_2 = QLabel(self.card_gbp_2)
        self.lbl_icon_gbp_2.setObjectName(u"lbl_icon_gbp_2")
        self.lbl_icon_gbp_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_gbp_2.setFont(font2)
        self.lbl_icon_gbp_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.lbl_icon_gbp_2)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.lbl_name_gbp_2 = QLabel(self.card_gbp_2)
        self.lbl_name_gbp_2.setObjectName(u"lbl_name_gbp_2")
        self.lbl_name_gbp_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_64.addWidget(self.lbl_name_gbp_2)

        self.lbl_rate_gbp_2 = QLabel(self.card_gbp_2)
        self.lbl_rate_gbp_2.setObjectName(u"lbl_rate_gbp_2")
        self.lbl_rate_gbp_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_64.addWidget(self.lbl_rate_gbp_2)


        self.horizontalLayout_31.addLayout(self.verticalLayout_64)

        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_5)

        self.lbl_icon_jpy_2 = QLabel(self.card_gbp_2)
        self.lbl_icon_jpy_2.setObjectName(u"lbl_icon_jpy_2")
        self.lbl_icon_jpy_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_jpy_2.setFont(font2)
        self.lbl_icon_jpy_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.lbl_icon_jpy_2)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.lbl_name_jpy_2 = QLabel(self.card_gbp_2)
        self.lbl_name_jpy_2.setObjectName(u"lbl_name_jpy_2")
        self.lbl_name_jpy_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_55.addWidget(self.lbl_name_jpy_2)

        self.lbl_rate_jpy_2 = QLabel(self.card_gbp_2)
        self.lbl_rate_jpy_2.setObjectName(u"lbl_rate_jpy_2")
        self.lbl_rate_jpy_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_55.addWidget(self.lbl_rate_jpy_2)


        self.horizontalLayout_31.addLayout(self.verticalLayout_55)


        self.verticalLayout_3.addWidget(self.card_gbp_2)

        self.card_chf_2 = QFrame(self.scrollAreaWidgetContents)
        self.card_chf_2.setObjectName(u"card_chf_2")
        self.card_chf_2.setMinimumSize(QSize(0, 100))
        self.card_chf_2.setMaximumSize(QSize(16777215, 120))
        self.card_chf_2.setFrameShape(QFrame.StyledPanel)
        self.card_chf_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.card_chf_2)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lbl_icon_chf_2 = QLabel(self.card_chf_2)
        self.lbl_icon_chf_2.setObjectName(u"lbl_icon_chf_2")
        self.lbl_icon_chf_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_chf_2.setFont(font2)
        self.lbl_icon_chf_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.lbl_icon_chf_2)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.lbl_name_chf_2 = QLabel(self.card_chf_2)
        self.lbl_name_chf_2.setObjectName(u"lbl_name_chf_2")
        self.lbl_name_chf_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_59.addWidget(self.lbl_name_chf_2)

        self.lbl_rate_chf_2 = QLabel(self.card_chf_2)
        self.lbl_rate_chf_2.setObjectName(u"lbl_rate_chf_2")
        self.lbl_rate_chf_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_59.addWidget(self.lbl_rate_chf_2)


        self.horizontalLayout_28.addLayout(self.verticalLayout_59)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_6)

        self.lbl_icon_cad_2 = QLabel(self.card_chf_2)
        self.lbl_icon_cad_2.setObjectName(u"lbl_icon_cad_2")
        self.lbl_icon_cad_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_cad_2.setFont(font3)
        self.lbl_icon_cad_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.lbl_icon_cad_2)

        self.verticalLayout_70 = QVBoxLayout()
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.lbl_name_cad_2 = QLabel(self.card_chf_2)
        self.lbl_name_cad_2.setObjectName(u"lbl_name_cad_2")
        self.lbl_name_cad_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_70.addWidget(self.lbl_name_cad_2)

        self.lbl_rate_cad_2 = QLabel(self.card_chf_2)
        self.lbl_rate_cad_2.setObjectName(u"lbl_rate_cad_2")
        self.lbl_rate_cad_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_70.addWidget(self.lbl_rate_cad_2)


        self.horizontalLayout_28.addLayout(self.verticalLayout_70)


        self.verticalLayout_3.addWidget(self.card_chf_2)

        self.card_aud_2 = QFrame(self.scrollAreaWidgetContents)
        self.card_aud_2.setObjectName(u"card_aud_2")
        self.card_aud_2.setMinimumSize(QSize(0, 100))
        self.card_aud_2.setMaximumSize(QSize(16777215, 120))
        self.card_aud_2.setAutoFillBackground(False)
        self.card_aud_2.setFrameShape(QFrame.StyledPanel)
        self.card_aud_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.card_aud_2)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lbl_icon_aud_2 = QLabel(self.card_aud_2)
        self.lbl_icon_aud_2.setObjectName(u"lbl_icon_aud_2")
        self.lbl_icon_aud_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_aud_2.setFont(font3)
        self.lbl_icon_aud_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.lbl_icon_aud_2)

        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.lbl_name_aud_2 = QLabel(self.card_aud_2)
        self.lbl_name_aud_2.setObjectName(u"lbl_name_aud_2")
        self.lbl_name_aud_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_66.addWidget(self.lbl_name_aud_2)

        self.lbl_rate_aud_2 = QLabel(self.card_aud_2)
        self.lbl_rate_aud_2.setObjectName(u"lbl_rate_aud_2")
        self.lbl_rate_aud_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_66.addWidget(self.lbl_rate_aud_2)


        self.horizontalLayout_32.addLayout(self.verticalLayout_66)

        self.horizontalSpacer_33 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_33)

        self.lbl_icon_cny_2 = QLabel(self.card_aud_2)
        self.lbl_icon_cny_2.setObjectName(u"lbl_icon_cny_2")
        self.lbl_icon_cny_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_cny_2.setFont(font3)
        self.lbl_icon_cny_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.lbl_icon_cny_2)

        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.lbl_name_cny_2 = QLabel(self.card_aud_2)
        self.lbl_name_cny_2.setObjectName(u"lbl_name_cny_2")
        self.lbl_name_cny_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_68.addWidget(self.lbl_name_cny_2)

        self.lbl_rate_cny_2 = QLabel(self.card_aud_2)
        self.lbl_rate_cny_2.setObjectName(u"lbl_rate_cny_2")
        self.lbl_rate_cny_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_68.addWidget(self.lbl_rate_cny_2)


        self.horizontalLayout_32.addLayout(self.verticalLayout_68)


        self.verticalLayout_3.addWidget(self.card_aud_2)

        self.card_try_2 = QFrame(self.scrollAreaWidgetContents)
        self.card_try_2.setObjectName(u"card_try_2")
        self.card_try_2.setMinimumSize(QSize(0, 100))
        self.card_try_2.setMaximumSize(QSize(16777215, 120))
        self.card_try_2.setFrameShape(QFrame.StyledPanel)
        self.card_try_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.card_try_2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lbl_icon_try_2 = QLabel(self.card_try_2)
        self.lbl_icon_try_2.setObjectName(u"lbl_icon_try_2")
        self.lbl_icon_try_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_try_2.setFont(font2)
        self.lbl_icon_try_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.lbl_icon_try_2)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.lbl_name_try_2 = QLabel(self.card_try_2)
        self.lbl_name_try_2.setObjectName(u"lbl_name_try_2")
        self.lbl_name_try_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_57.addWidget(self.lbl_name_try_2)

        self.lbl_rate_try_2 = QLabel(self.card_try_2)
        self.lbl_rate_try_2.setObjectName(u"lbl_rate_try_2")
        self.lbl_rate_try_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_57.addWidget(self.lbl_rate_try_2)


        self.horizontalLayout_27.addLayout(self.verticalLayout_57)

        self.horizontalSpacer_35 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_35)

        self.lbl_icon_sar_2 = QLabel(self.card_try_2)
        self.lbl_icon_sar_2.setObjectName(u"lbl_icon_sar_2")
        self.lbl_icon_sar_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_sar_2.setFont(font2)
        self.lbl_icon_sar_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.lbl_icon_sar_2)

        self.verticalLayout_72 = QVBoxLayout()
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.lbl_name_sar_2 = QLabel(self.card_try_2)
        self.lbl_name_sar_2.setObjectName(u"lbl_name_sar_2")
        self.lbl_name_sar_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_72.addWidget(self.lbl_name_sar_2)

        self.lbl_rate_sar_2 = QLabel(self.card_try_2)
        self.lbl_rate_sar_2.setObjectName(u"lbl_rate_sar_2")
        self.lbl_rate_sar_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_72.addWidget(self.lbl_rate_sar_2)


        self.horizontalLayout_27.addLayout(self.verticalLayout_72)


        self.verticalLayout_3.addWidget(self.card_try_2)

        self.card_nzd_2 = QFrame(self.scrollAreaWidgetContents)
        self.card_nzd_2.setObjectName(u"card_nzd_2")
        self.card_nzd_2.setMinimumSize(QSize(0, 100))
        self.card_nzd_2.setMaximumSize(QSize(16777215, 120))
        self.card_nzd_2.setFrameShape(QFrame.StyledPanel)
        self.card_nzd_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.card_nzd_2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lbl_icon_nzd_2 = QLabel(self.card_nzd_2)
        self.lbl_icon_nzd_2.setObjectName(u"lbl_icon_nzd_2")
        self.lbl_icon_nzd_2.setMinimumSize(QSize(70, 70))
        self.lbl_icon_nzd_2.setFont(font3)
        self.lbl_icon_nzd_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.lbl_icon_nzd_2)

        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.lbl_name_nzd_2 = QLabel(self.card_nzd_2)
        self.lbl_name_nzd_2.setObjectName(u"lbl_name_nzd_2")
        self.lbl_name_nzd_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_62.addWidget(self.lbl_name_nzd_2)

        self.lbl_rate_nzd_2 = QLabel(self.card_nzd_2)
        self.lbl_rate_nzd_2.setObjectName(u"lbl_rate_nzd_2")
        self.lbl_rate_nzd_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_62.addWidget(self.lbl_rate_nzd_2)


        self.horizontalLayout_30.addLayout(self.verticalLayout_62)

        self.horizontalSpacer_7 = QSpacerItem(480, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addWidget(self.card_nzd_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 4)
        self.stackedWidget_2.addWidget(self.profile_page)

        self.gridLayout_4.addWidget(self.stackedWidget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_text.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.password_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.username_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.register_text.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.conpassword_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password ", None))
        self.registerpassword_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.registerusername_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.backtologin_button.setText(QCoreApplication.translate("MainWindow", u"Back To Login", None))
        self.register_button_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.lbl_base_rate.setText(QCoreApplication.translate("MainWindow", u"Base Rate", None))
        self.user_info_lbl.setText(QCoreApplication.translate("MainWindow", u"User: Test", None))
        self.portfoilo_lbl.setText(QCoreApplication.translate("MainWindow", u"Portfoilo: 100 USD", None))
        self.profile_button.setText("")
        self.lbl_icon_eur.setText(QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.lbl_name_eur.setText(QCoreApplication.translate("MainWindow", u"Euro", None))
        self.lbl_rate_eur.setText(QCoreApplication.translate("MainWindow", u"1 EUR = ? Base", None))
        self.buy_eur_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_usd.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.lbl_name_usd.setText(QCoreApplication.translate("MainWindow", u"American Dollar", None))
        self.lbl_rate_usd.setText(QCoreApplication.translate("MainWindow", u"1 USD = ? Base", None))
        self.buy_usd_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_gbp.setText(QCoreApplication.translate("MainWindow", u"\u00a3", None))
        self.lbl_name_gbp.setText(QCoreApplication.translate("MainWindow", u"Great British Pound", None))
        self.lbl_rate_gbp.setText(QCoreApplication.translate("MainWindow", u"1 GBP = ? Base", None))
        self.buy_gbp_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_jpy.setText(QCoreApplication.translate("MainWindow", u"\u00a5", None))
        self.lbl_name_jpy.setText(QCoreApplication.translate("MainWindow", u"Japanese Yen", None))
        self.lbl_rate_jpy.setText(QCoreApplication.translate("MainWindow", u"1 JPY = ? Base", None))
        self.buy_jpy_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_chf.setText(QCoreApplication.translate("MainWindow", u"\u20a3", None))
        self.lbl_name_chf.setText(QCoreApplication.translate("MainWindow", u"Swiss franc", None))
        self.lbl_rate_chf.setText(QCoreApplication.translate("MainWindow", u"1 CHF = ? Base", None))
        self.buy_chf_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_cad.setText(QCoreApplication.translate("MainWindow", u"CA$", None))
        self.lbl_name_cad.setText(QCoreApplication.translate("MainWindow", u"Canadian Dollar", None))
        self.lbl_rate_cad.setText(QCoreApplication.translate("MainWindow", u"1 CAD = ? Base", None))
        self.buy_cad_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_aud.setText(QCoreApplication.translate("MainWindow", u"AU$", None))
        self.lbl_name_aud.setText(QCoreApplication.translate("MainWindow", u"Australian Dollar", None))
        self.lbl_rate_aud.setText(QCoreApplication.translate("MainWindow", u"1 AUD = ? Base", None))
        self.buy_aud_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_cny.setText(QCoreApplication.translate("MainWindow", u"CN\u00a5", None))
        self.lbl_name_cny.setText(QCoreApplication.translate("MainWindow", u"Chinese Yuan Renminbi", None))
        self.lbl_rate_cny.setText(QCoreApplication.translate("MainWindow", u"1 CNY = ? Base", None))
        self.buy_cny_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_try.setText(QCoreApplication.translate("MainWindow", u"\u20ba", None))
        self.lbl_name_try.setText(QCoreApplication.translate("MainWindow", u"Turkish Lira", None))
        self.lbl_rate_try.setText(QCoreApplication.translate("MainWindow", u"1 TRY = ? Base", None))
        self.buy_try_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_sar.setText(QCoreApplication.translate("MainWindow", u"\u20c1", None))
        self.lbl_name_sar.setText(QCoreApplication.translate("MainWindow", u"Saudi Riyal", None))
        self.lbl_rate_sar.setText(QCoreApplication.translate("MainWindow", u"1 SAR = ? Base", None))
        self.buy_sar_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_icon_nzd.setText(QCoreApplication.translate("MainWindow", u"NZ$", None))
        self.lbl_name_nzd.setText(QCoreApplication.translate("MainWindow", u"New Zealand Dollar", None))
        self.lbl_rate_nzd.setText(QCoreApplication.translate("MainWindow", u"1 NZD = ? Base", None))
        self.buy_nzd_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.lbl_loading_rates_2.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))
        self.back_home_button.setText(QCoreApplication.translate("MainWindow", u"Back To Home Page", None))
        self.username_prof_lbl.setText(QCoreApplication.translate("MainWindow", u"User: tester", None))
        self.change_foto_button.setText(QCoreApplication.translate("MainWindow", u"Change Profile Photo", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.profile_foto_button.setText(QCoreApplication.translate("MainWindow", u"No Image", None))
        self.lbl_icon_eur_2.setText(QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.lbl_name_eur_2.setText(QCoreApplication.translate("MainWindow", u"Euro", None))
        self.lbl_rate_eur_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? EUR", None))
        self.lbl_icon_usd_2.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.lbl_name_usd_2.setText(QCoreApplication.translate("MainWindow", u"American Dollar", None))
        self.lbl_rate_usd_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? USD", None))
        self.lbl_icon_gbp_2.setText(QCoreApplication.translate("MainWindow", u"\u00a3", None))
        self.lbl_name_gbp_2.setText(QCoreApplication.translate("MainWindow", u"Great British Pound", None))
        self.lbl_rate_gbp_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? GBP", None))
        self.lbl_icon_jpy_2.setText(QCoreApplication.translate("MainWindow", u"\u00a5", None))
        self.lbl_name_jpy_2.setText(QCoreApplication.translate("MainWindow", u"Japanese Yen", None))
        self.lbl_rate_jpy_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? JPY", None))
        self.lbl_icon_chf_2.setText(QCoreApplication.translate("MainWindow", u"\u20a3", None))
        self.lbl_name_chf_2.setText(QCoreApplication.translate("MainWindow", u"Swiss franc", None))
        self.lbl_rate_chf_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? CHF", None))
        self.lbl_icon_cad_2.setText(QCoreApplication.translate("MainWindow", u"CA$", None))
        self.lbl_name_cad_2.setText(QCoreApplication.translate("MainWindow", u"Canadian Dollar", None))
        self.lbl_rate_cad_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? CAD", None))
        self.lbl_icon_aud_2.setText(QCoreApplication.translate("MainWindow", u"AU$", None))
        self.lbl_name_aud_2.setText(QCoreApplication.translate("MainWindow", u"Australian Dollar", None))
        self.lbl_rate_aud_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? AUD", None))
        self.lbl_icon_cny_2.setText(QCoreApplication.translate("MainWindow", u"CN\u00a5", None))
        self.lbl_name_cny_2.setText(QCoreApplication.translate("MainWindow", u"Chinese Yuan Renminbi", None))
        self.lbl_rate_cny_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? CNY", None))
        self.lbl_icon_try_2.setText(QCoreApplication.translate("MainWindow", u"\u20ba", None))
        self.lbl_name_try_2.setText(QCoreApplication.translate("MainWindow", u"Turkish Lira", None))
        self.lbl_rate_try_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? TRY", None))
        self.lbl_icon_sar_2.setText(QCoreApplication.translate("MainWindow", u"\u20c1", None))
        self.lbl_name_sar_2.setText(QCoreApplication.translate("MainWindow", u"Saudi Riyal", None))
        self.lbl_rate_sar_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? SAR", None))
        self.lbl_icon_nzd_2.setText(QCoreApplication.translate("MainWindow", u"NZ$", None))
        self.lbl_name_nzd_2.setText(QCoreApplication.translate("MainWindow", u"New Zealand Dollar", None))
        self.lbl_rate_nzd_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio: ? NZD", None))
    # retranslateUi

