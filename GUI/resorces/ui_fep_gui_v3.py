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
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(948, 749)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_14 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
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
        self.verticalLayout_17 = QVBoxLayout(self.home_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.home_page)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 70))
        self.header_frame.setMaximumSize(QSize(16777215, 100))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_base_rate = QLabel(self.header_frame)
        self.lbl_base_rate.setObjectName(u"lbl_base_rate")

        self.horizontalLayout_2.addWidget(self.lbl_base_rate)

        self.cb_base_currency = QComboBox(self.header_frame)
        self.cb_base_currency.setObjectName(u"cb_base_currency")

        self.horizontalLayout_2.addWidget(self.cb_base_currency)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.user_lbl_frame = QFrame(self.header_frame)
        self.user_lbl_frame.setObjectName(u"user_lbl_frame")
        sizePolicy1.setHeightForWidth(self.user_lbl_frame.sizePolicy().hasHeightForWidth())
        self.user_lbl_frame.setSizePolicy(sizePolicy1)
        self.user_lbl_frame.setFrameShape(QFrame.StyledPanel)
        self.user_lbl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.user_lbl_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.v_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.v_spacer)

        self.user_info_lbl = QLabel(self.user_lbl_frame)
        self.user_info_lbl.setObjectName(u"user_info_lbl")

        self.verticalLayout_2.addWidget(self.user_info_lbl)

        self.portfoilo_lbl = QLabel(self.user_lbl_frame)
        self.portfoilo_lbl.setObjectName(u"portfoilo_lbl")

        self.verticalLayout_2.addWidget(self.portfoilo_lbl)

        self.v_spacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.v_spacer_2)


        self.horizontalLayout_2.addWidget(self.user_lbl_frame)

        self.profile_button = QPushButton(self.header_frame)
        self.profile_button.setObjectName(u"profile_button")

        self.horizontalLayout_2.addWidget(self.profile_button)


        self.verticalLayout.addWidget(self.header_frame)


        self.verticalLayout_17.addLayout(self.verticalLayout)

        self.stackedWidget_2 = QStackedWidget(self.home_page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy2)
        self.rate_page = QWidget()
        self.rate_page.setObjectName(u"rate_page")
        self.verticalLayout_16 = QVBoxLayout(self.rate_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.scroll_area_currencies = QScrollArea(self.rate_page)
        self.scroll_area_currencies.setObjectName(u"scroll_area_currencies")
        self.scroll_area_currencies.setWidgetResizable(True)
        self.scroll_content_currencies = QWidget()
        self.scroll_content_currencies.setObjectName(u"scroll_content_currencies")
        self.scroll_content_currencies.setGeometry(QRect(0, 0, 859, 1192))
        self.verticalLayout_4 = QVBoxLayout(self.scroll_content_currencies)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.card_eur = QFrame(self.scroll_content_currencies)
        self.card_eur.setObjectName(u"card_eur")
        self.card_eur.setMinimumSize(QSize(0, 100))
        self.card_eur.setMaximumSize(QSize(16777215, 120))
        self.card_eur.setFrameShape(QFrame.StyledPanel)
        self.card_eur.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.card_eur)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_icon_eur = QLabel(self.card_eur)
        self.lbl_icon_eur.setObjectName(u"lbl_icon_eur")
        self.lbl_icon_eur.setMinimumSize(QSize(70, 70))
        self.lbl_icon_eur.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_icon_eur)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_name_eur = QLabel(self.card_eur)
        self.lbl_name_eur.setObjectName(u"lbl_name_eur")
        self.lbl_name_eur.setMinimumSize(QSize(0, 0))

        self.verticalLayout_5.addWidget(self.lbl_name_eur)

        self.lbl_rate_eur = QLabel(self.card_eur)
        self.lbl_rate_eur.setObjectName(u"lbl_rate_eur")
        self.lbl_rate_eur.setMinimumSize(QSize(0, 0))

        self.verticalLayout_5.addWidget(self.lbl_rate_eur)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.buy_eur_button = QPushButton(self.card_eur)
        self.buy_eur_button.setObjectName(u"buy_eur_button")

        self.verticalLayout_20.addWidget(self.buy_eur_button)

        self.dsb_amount_eur = QDoubleSpinBox(self.card_eur)
        self.dsb_amount_eur.setObjectName(u"dsb_amount_eur")
        self.dsb_amount_eur.setMinimum(1.000000000000000)

        self.verticalLayout_20.addWidget(self.dsb_amount_eur)


        self.horizontalLayout.addLayout(self.verticalLayout_20)


        self.verticalLayout_4.addWidget(self.card_eur)

        self.card_usd = QFrame(self.scroll_content_currencies)
        self.card_usd.setObjectName(u"card_usd")
        self.card_usd.setMinimumSize(QSize(0, 100))
        self.card_usd.setMaximumSize(QSize(16777215, 120))
        self.card_usd.setFrameShape(QFrame.StyledPanel)
        self.card_usd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.card_usd)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_icon_usd = QLabel(self.card_usd)
        self.lbl_icon_usd.setObjectName(u"lbl_icon_usd")
        self.lbl_icon_usd.setMinimumSize(QSize(70, 70))
        self.lbl_icon_usd.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_icon_usd)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_name_usd = QLabel(self.card_usd)
        self.lbl_name_usd.setObjectName(u"lbl_name_usd")
        self.lbl_name_usd.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.lbl_name_usd)

        self.lbl_rate_usd = QLabel(self.card_usd)
        self.lbl_rate_usd.setObjectName(u"lbl_rate_usd")
        self.lbl_rate_usd.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.lbl_rate_usd)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_3 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.buy_usd_button = QPushButton(self.card_usd)
        self.buy_usd_button.setObjectName(u"buy_usd_button")

        self.verticalLayout_22.addWidget(self.buy_usd_button)

        self.dsb_amount_usd = QDoubleSpinBox(self.card_usd)
        self.dsb_amount_usd.setObjectName(u"dsb_amount_usd")
        self.dsb_amount_usd.setMinimum(1.000000000000000)

        self.verticalLayout_22.addWidget(self.dsb_amount_usd)


        self.horizontalLayout_3.addLayout(self.verticalLayout_22)


        self.verticalLayout_4.addWidget(self.card_usd)

        self.card_gbp = QFrame(self.scroll_content_currencies)
        self.card_gbp.setObjectName(u"card_gbp")
        self.card_gbp.setMinimumSize(QSize(0, 100))
        self.card_gbp.setMaximumSize(QSize(16777215, 120))
        self.card_gbp.setFrameShape(QFrame.StyledPanel)
        self.card_gbp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.card_gbp)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_icon_gbp = QLabel(self.card_gbp)
        self.lbl_icon_gbp.setObjectName(u"lbl_icon_gbp")
        self.lbl_icon_gbp.setMinimumSize(QSize(70, 70))
        self.lbl_icon_gbp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbl_icon_gbp)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_name_gbp = QLabel(self.card_gbp)
        self.lbl_name_gbp.setObjectName(u"lbl_name_gbp")
        self.lbl_name_gbp.setMinimumSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.lbl_name_gbp)

        self.lbl_rate_gbp = QLabel(self.card_gbp)
        self.lbl_rate_gbp.setObjectName(u"lbl_rate_gbp")
        self.lbl_rate_gbp.setMinimumSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.lbl_rate_gbp)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.buy_gbp_button = QPushButton(self.card_gbp)
        self.buy_gbp_button.setObjectName(u"buy_gbp_button")

        self.verticalLayout_23.addWidget(self.buy_gbp_button)

        self.dsb_amount_gbp = QDoubleSpinBox(self.card_gbp)
        self.dsb_amount_gbp.setObjectName(u"dsb_amount_gbp")
        self.dsb_amount_gbp.setMinimum(1.000000000000000)

        self.verticalLayout_23.addWidget(self.dsb_amount_gbp)


        self.horizontalLayout_4.addLayout(self.verticalLayout_23)


        self.verticalLayout_4.addWidget(self.card_gbp)

        self.card_jpy = QFrame(self.scroll_content_currencies)
        self.card_jpy.setObjectName(u"card_jpy")
        self.card_jpy.setMinimumSize(QSize(0, 100))
        self.card_jpy.setMaximumSize(QSize(16777215, 120))
        self.card_jpy.setFrameShape(QFrame.StyledPanel)
        self.card_jpy.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.card_jpy)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_icon_jpy = QLabel(self.card_jpy)
        self.lbl_icon_jpy.setObjectName(u"lbl_icon_jpy")
        self.lbl_icon_jpy.setMinimumSize(QSize(70, 70))
        self.lbl_icon_jpy.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lbl_icon_jpy)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_name_jpy = QLabel(self.card_jpy)
        self.lbl_name_jpy.setObjectName(u"lbl_name_jpy")
        self.lbl_name_jpy.setMinimumSize(QSize(0, 0))

        self.verticalLayout_8.addWidget(self.lbl_name_jpy)

        self.lbl_rate_jpy = QLabel(self.card_jpy)
        self.lbl_rate_jpy.setObjectName(u"lbl_rate_jpy")
        self.lbl_rate_jpy.setMinimumSize(QSize(0, 0))

        self.verticalLayout_8.addWidget(self.lbl_rate_jpy)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_5 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.buy_jpy_button = QPushButton(self.card_jpy)
        self.buy_jpy_button.setObjectName(u"buy_jpy_button")

        self.verticalLayout_24.addWidget(self.buy_jpy_button)

        self.dsb_amount_jpy = QDoubleSpinBox(self.card_jpy)
        self.dsb_amount_jpy.setObjectName(u"dsb_amount_jpy")
        self.dsb_amount_jpy.setMinimum(1.000000000000000)

        self.verticalLayout_24.addWidget(self.dsb_amount_jpy)


        self.horizontalLayout_5.addLayout(self.verticalLayout_24)


        self.verticalLayout_4.addWidget(self.card_jpy)

        self.card_chf = QFrame(self.scroll_content_currencies)
        self.card_chf.setObjectName(u"card_chf")
        self.card_chf.setMinimumSize(QSize(0, 100))
        self.card_chf.setMaximumSize(QSize(16777215, 120))
        self.card_chf.setFrameShape(QFrame.StyledPanel)
        self.card_chf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.card_chf)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_icon_chf = QLabel(self.card_chf)
        self.lbl_icon_chf.setObjectName(u"lbl_icon_chf")
        self.lbl_icon_chf.setMinimumSize(QSize(70, 70))
        self.lbl_icon_chf.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lbl_icon_chf)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_name_chf = QLabel(self.card_chf)
        self.lbl_name_chf.setObjectName(u"lbl_name_chf")
        self.lbl_name_chf.setMinimumSize(QSize(0, 0))

        self.verticalLayout_9.addWidget(self.lbl_name_chf)

        self.lbl_rate_chf = QLabel(self.card_chf)
        self.lbl_rate_chf.setObjectName(u"lbl_rate_chf")
        self.lbl_rate_chf.setMinimumSize(QSize(0, 0))

        self.verticalLayout_9.addWidget(self.lbl_rate_chf)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_6 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.buy_chf_button = QPushButton(self.card_chf)
        self.buy_chf_button.setObjectName(u"buy_chf_button")

        self.verticalLayout_25.addWidget(self.buy_chf_button)

        self.dsb_amount_chf = QDoubleSpinBox(self.card_chf)
        self.dsb_amount_chf.setObjectName(u"dsb_amount_chf")
        self.dsb_amount_chf.setMinimum(1.000000000000000)

        self.verticalLayout_25.addWidget(self.dsb_amount_chf)


        self.horizontalLayout_6.addLayout(self.verticalLayout_25)


        self.verticalLayout_4.addWidget(self.card_chf)

        self.card_cad = QFrame(self.scroll_content_currencies)
        self.card_cad.setObjectName(u"card_cad")
        self.card_cad.setMinimumSize(QSize(0, 100))
        self.card_cad.setMaximumSize(QSize(16777215, 120))
        self.card_cad.setFrameShape(QFrame.StyledPanel)
        self.card_cad.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.card_cad)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_icon_cad = QLabel(self.card_cad)
        self.lbl_icon_cad.setObjectName(u"lbl_icon_cad")
        self.lbl_icon_cad.setMinimumSize(QSize(70, 70))
        self.lbl_icon_cad.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbl_icon_cad)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lbl_name_cad = QLabel(self.card_cad)
        self.lbl_name_cad.setObjectName(u"lbl_name_cad")
        self.lbl_name_cad.setMinimumSize(QSize(0, 0))

        self.verticalLayout_10.addWidget(self.lbl_name_cad)

        self.lbl_rate_cad = QLabel(self.card_cad)
        self.lbl_rate_cad.setObjectName(u"lbl_rate_cad")
        self.lbl_rate_cad.setMinimumSize(QSize(0, 0))

        self.verticalLayout_10.addWidget(self.lbl_rate_cad)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_7 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.buy_cad_button = QPushButton(self.card_cad)
        self.buy_cad_button.setObjectName(u"buy_cad_button")

        self.verticalLayout_26.addWidget(self.buy_cad_button)

        self.dsb_amount_cad = QDoubleSpinBox(self.card_cad)
        self.dsb_amount_cad.setObjectName(u"dsb_amount_cad")
        self.dsb_amount_cad.setMinimum(1.000000000000000)

        self.verticalLayout_26.addWidget(self.dsb_amount_cad)


        self.horizontalLayout_7.addLayout(self.verticalLayout_26)


        self.verticalLayout_4.addWidget(self.card_cad)

        self.card_aud = QFrame(self.scroll_content_currencies)
        self.card_aud.setObjectName(u"card_aud")
        self.card_aud.setMinimumSize(QSize(0, 100))
        self.card_aud.setMaximumSize(QSize(16777215, 120))
        self.card_aud.setAutoFillBackground(False)
        self.card_aud.setFrameShape(QFrame.StyledPanel)
        self.card_aud.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.card_aud)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_icon_aud = QLabel(self.card_aud)
        self.lbl_icon_aud.setObjectName(u"lbl_icon_aud")
        self.lbl_icon_aud.setMinimumSize(QSize(70, 70))
        self.lbl_icon_aud.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lbl_icon_aud)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lbl_name_aud = QLabel(self.card_aud)
        self.lbl_name_aud.setObjectName(u"lbl_name_aud")
        self.lbl_name_aud.setMinimumSize(QSize(0, 0))

        self.verticalLayout_11.addWidget(self.lbl_name_aud)

        self.lbl_rate_aud = QLabel(self.card_aud)
        self.lbl_rate_aud.setObjectName(u"lbl_rate_aud")
        self.lbl_rate_aud.setMinimumSize(QSize(0, 0))

        self.verticalLayout_11.addWidget(self.lbl_rate_aud)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_8 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.buy_aud_button = QPushButton(self.card_aud)
        self.buy_aud_button.setObjectName(u"buy_aud_button")

        self.verticalLayout_27.addWidget(self.buy_aud_button)

        self.dsb_amount_aud = QDoubleSpinBox(self.card_aud)
        self.dsb_amount_aud.setObjectName(u"dsb_amount_aud")
        self.dsb_amount_aud.setMinimum(1.000000000000000)

        self.verticalLayout_27.addWidget(self.dsb_amount_aud)


        self.horizontalLayout_8.addLayout(self.verticalLayout_27)


        self.verticalLayout_4.addWidget(self.card_aud)

        self.card_cny = QFrame(self.scroll_content_currencies)
        self.card_cny.setObjectName(u"card_cny")
        self.card_cny.setMinimumSize(QSize(0, 100))
        self.card_cny.setMaximumSize(QSize(16777215, 120))
        self.card_cny.setFrameShape(QFrame.StyledPanel)
        self.card_cny.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.card_cny)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_icon_cny = QLabel(self.card_cny)
        self.lbl_icon_cny.setObjectName(u"lbl_icon_cny")
        self.lbl_icon_cny.setMinimumSize(QSize(70, 70))
        self.lbl_icon_cny.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lbl_icon_cny)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lbl_name_cny = QLabel(self.card_cny)
        self.lbl_name_cny.setObjectName(u"lbl_name_cny")
        self.lbl_name_cny.setMinimumSize(QSize(0, 0))

        self.verticalLayout_12.addWidget(self.lbl_name_cny)

        self.lbl_rate_cny = QLabel(self.card_cny)
        self.lbl_rate_cny.setObjectName(u"lbl_rate_cny")
        self.lbl_rate_cny.setMinimumSize(QSize(0, 0))

        self.verticalLayout_12.addWidget(self.lbl_rate_cny)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_9 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.buy_cny_button = QPushButton(self.card_cny)
        self.buy_cny_button.setObjectName(u"buy_cny_button")

        self.verticalLayout_28.addWidget(self.buy_cny_button)

        self.dsb_amount_cny = QDoubleSpinBox(self.card_cny)
        self.dsb_amount_cny.setObjectName(u"dsb_amount_cny")
        self.dsb_amount_cny.setMinimum(1.000000000000000)

        self.verticalLayout_28.addWidget(self.dsb_amount_cny)


        self.horizontalLayout_9.addLayout(self.verticalLayout_28)


        self.verticalLayout_4.addWidget(self.card_cny)

        self.card_try = QFrame(self.scroll_content_currencies)
        self.card_try.setObjectName(u"card_try")
        self.card_try.setMinimumSize(QSize(0, 100))
        self.card_try.setMaximumSize(QSize(16777215, 120))
        self.card_try.setFrameShape(QFrame.StyledPanel)
        self.card_try.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.card_try)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_icon_try = QLabel(self.card_try)
        self.lbl_icon_try.setObjectName(u"lbl_icon_try")
        self.lbl_icon_try.setMinimumSize(QSize(70, 70))
        self.lbl_icon_try.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lbl_icon_try)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lbl_name_try = QLabel(self.card_try)
        self.lbl_name_try.setObjectName(u"lbl_name_try")
        self.lbl_name_try.setMinimumSize(QSize(0, 0))

        self.verticalLayout_13.addWidget(self.lbl_name_try)

        self.lbl_rate_try = QLabel(self.card_try)
        self.lbl_rate_try.setObjectName(u"lbl_rate_try")
        self.lbl_rate_try.setMinimumSize(QSize(0, 0))

        self.verticalLayout_13.addWidget(self.lbl_rate_try)


        self.horizontalLayout_10.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_10 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.buy_try_button = QPushButton(self.card_try)
        self.buy_try_button.setObjectName(u"buy_try_button")

        self.verticalLayout_29.addWidget(self.buy_try_button)

        self.dsb_amount_try = QDoubleSpinBox(self.card_try)
        self.dsb_amount_try.setObjectName(u"dsb_amount_try")
        self.dsb_amount_try.setMinimum(1.000000000000000)

        self.verticalLayout_29.addWidget(self.dsb_amount_try)


        self.horizontalLayout_10.addLayout(self.verticalLayout_29)


        self.verticalLayout_4.addWidget(self.card_try)

        self.card_sar = QFrame(self.scroll_content_currencies)
        self.card_sar.setObjectName(u"card_sar")
        self.card_sar.setMinimumSize(QSize(0, 100))
        self.card_sar.setMaximumSize(QSize(16777215, 120))
        self.card_sar.setFrameShape(QFrame.StyledPanel)
        self.card_sar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.card_sar)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_icon_sar = QLabel(self.card_sar)
        self.lbl_icon_sar.setObjectName(u"lbl_icon_sar")
        self.lbl_icon_sar.setMinimumSize(QSize(70, 70))
        self.lbl_icon_sar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lbl_icon_sar)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lbl_name_sar = QLabel(self.card_sar)
        self.lbl_name_sar.setObjectName(u"lbl_name_sar")
        self.lbl_name_sar.setMinimumSize(QSize(0, 0))

        self.verticalLayout_14.addWidget(self.lbl_name_sar)

        self.lbl_rate_sar = QLabel(self.card_sar)
        self.lbl_rate_sar.setObjectName(u"lbl_rate_sar")
        self.lbl_rate_sar.setMinimumSize(QSize(0, 0))

        self.verticalLayout_14.addWidget(self.lbl_rate_sar)


        self.horizontalLayout_11.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_11 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.buy_sar_button = QPushButton(self.card_sar)
        self.buy_sar_button.setObjectName(u"buy_sar_button")

        self.verticalLayout_30.addWidget(self.buy_sar_button)

        self.dsb_amount_sar = QDoubleSpinBox(self.card_sar)
        self.dsb_amount_sar.setObjectName(u"dsb_amount_sar")
        self.dsb_amount_sar.setMinimum(1.000000000000000)

        self.verticalLayout_30.addWidget(self.dsb_amount_sar)


        self.horizontalLayout_11.addLayout(self.verticalLayout_30)


        self.verticalLayout_4.addWidget(self.card_sar)

        self.card_nzd = QFrame(self.scroll_content_currencies)
        self.card_nzd.setObjectName(u"card_nzd")
        self.card_nzd.setMinimumSize(QSize(0, 100))
        self.card_nzd.setMaximumSize(QSize(16777215, 120))
        self.card_nzd.setFrameShape(QFrame.StyledPanel)
        self.card_nzd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.card_nzd)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lbl_icon_nzd = QLabel(self.card_nzd)
        self.lbl_icon_nzd.setObjectName(u"lbl_icon_nzd")
        self.lbl_icon_nzd.setMinimumSize(QSize(70, 70))
        self.lbl_icon_nzd.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lbl_icon_nzd)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lbl_name_nzd = QLabel(self.card_nzd)
        self.lbl_name_nzd.setObjectName(u"lbl_name_nzd")
        self.lbl_name_nzd.setMinimumSize(QSize(0, 0))

        self.verticalLayout_15.addWidget(self.lbl_name_nzd)

        self.lbl_rate_nzd = QLabel(self.card_nzd)
        self.lbl_rate_nzd.setObjectName(u"lbl_rate_nzd")
        self.lbl_rate_nzd.setMinimumSize(QSize(0, 0))

        self.verticalLayout_15.addWidget(self.lbl_rate_nzd)


        self.horizontalLayout_12.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_12 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.buy_nzd_button = QPushButton(self.card_nzd)
        self.buy_nzd_button.setObjectName(u"buy_nzd_button")

        self.verticalLayout_31.addWidget(self.buy_nzd_button)

        self.dsb_amount_nzd = QDoubleSpinBox(self.card_nzd)
        self.dsb_amount_nzd.setObjectName(u"dsb_amount_nzd")
        self.dsb_amount_nzd.setMinimum(1.000000000000000)

        self.verticalLayout_31.addWidget(self.dsb_amount_nzd)


        self.horizontalLayout_12.addLayout(self.verticalLayout_31)


        self.verticalLayout_4.addWidget(self.card_nzd)

        self.scroll_area_currencies.setWidget(self.scroll_content_currencies)

        self.verticalLayout_16.addWidget(self.scroll_area_currencies)

        self.stackedWidget_2.addWidget(self.rate_page)
        self.loading_page = QWidget()
        self.loading_page.setObjectName(u"loading_page")
        self.horizontalLayout_15 = QHBoxLayout(self.loading_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.loading_frame = QFrame(self.loading_page)
        self.loading_frame.setObjectName(u"loading_frame")
        self.loading_frame.setFrameShape(QFrame.StyledPanel)
        self.loading_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.loading_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.lbl_loading_rates = QLabel(self.loading_frame)
        self.lbl_loading_rates.setObjectName(u"lbl_loading_rates")
        self.lbl_loading_rates.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_loading_rates)

        self.loading_bar = QProgressBar(self.loading_frame)
        self.loading_bar.setObjectName(u"loading_bar")
        self.loading_bar.setMaximum(0)
        self.loading_bar.setValue(-1)
        self.loading_bar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.loading_bar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.loading_frame)

        self.stackedWidget_2.addWidget(self.loading_page)

        self.verticalLayout_17.addWidget(self.stackedWidget_2)

        self.verticalLayout_17.setStretch(0, 1)
        self.verticalLayout_17.setStretch(1, 6)
        self.stackedWidget.addWidget(self.home_page)

        self.horizontalLayout_14.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)


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
        self.profile_button.setText(QCoreApplication.translate("MainWindow", u"profile", None))
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
        self.lbl_loading_rates.setText(QCoreApplication.translate("MainWindow", u"Loading exchange rates...", None))
    # retranslateUi

