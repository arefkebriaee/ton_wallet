# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tw_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 30))
        self.widget_4.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.create_wallet_button = QPushButton(self.widget_4)
        self.create_wallet_button.setObjectName(u"create_wallet_button")
        self.create_wallet_button.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(True)
        self.create_wallet_button.setFont(font)
        self.create_wallet_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.create_wallet_button.setStyleSheet(u"#create_wallet_button{\n"
"border-radius: 5px;\n"
"background-color: rgb(206, 206, 206);\n"
"	color: rgb(35, 166, 171);\n"
"}\n"
"\n"
"#create_wallet_button::hover{\n"
"border-radius: 5px;\n"
"background-color: rgb(35, 166, 171);\n"
"	color: rgb(234, 234, 234);\n"
"}")

        self.gridLayout_5.addWidget(self.create_wallet_button, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.widget_5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"#listWidget{\n"
"	background-color: rgb(232, 232, 232);\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"#listWidget:item{\n"
"color: rgb(31, 31, 31);\n"
"height: 40px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding-left: 0;\n"
"}\n"
"\n"
"#listWidget::item::selected{\n"
"	background-color: rgb(35, 166, 171);\n"
"	color: rgb(229, 229, 229);\n"
"	padding-left: 20px;\n"
"	font: 75 15pt \"MS Sans Serif\";\n"
"}\n"
"\n"
"#listWidget:item:hover{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(72, 72, 72);\n"
"	padding-left: 20px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.listWidget, 1, 0, 1, 1)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_5, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 30))
        self.gridLayout_10 = QGridLayout(self.widget_10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)

        self.state_label = QLabel(self.widget_10)
        self.state_label.setObjectName(u"state_label")

        self.gridLayout_10.addWidget(self.state_label, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_10, 2, 0, 1, 1)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 30))
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)

        self.wallet_address_label = QLabel(self.widget_8)
        self.wallet_address_label.setObjectName(u"wallet_address_label")
        self.wallet_address_label.setFont(font)

        self.gridLayout_8.addWidget(self.wallet_address_label, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 30))
        self.gridLayout_9 = QGridLayout(self.widget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 1)

        self.balance_label = QLabel(self.widget_9)
        self.balance_label.setObjectName(u"balance_label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.balance_label.setFont(font1)

        self.gridLayout_9.addWidget(self.balance_label, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_9, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 30))
        self.gridLayout_11 = QGridLayout(self.widget_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)

        self.last_activity_label = QLabel(self.widget_11)
        self.last_activity_label.setObjectName(u"last_activity_label")

        self.gridLayout_11.addWidget(self.last_activity_label, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_11, 3, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_6, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_12 = QGridLayout(self.widget_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget_7)
        self.tabWidget.setObjectName(u"tabWidget")
        self.withdraw_tab = QWidget()
        self.withdraw_tab.setObjectName(u"withdraw_tab")
        self.gridLayout_13 = QGridLayout(self.withdraw_tab)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.widget_12 = QWidget(self.withdraw_tab)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_14 = QGridLayout(self.widget_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_16 = QGridLayout(self.widget_14)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_7 = QLabel(self.widget_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(150, 0))

        self.gridLayout_16.addWidget(self.label_7, 0, 0, 1, 1)

        self.withdraw_amount_line_edit = QLineEdit(self.widget_14)
        self.withdraw_amount_line_edit.setObjectName(u"withdraw_amount_line_edit")

        self.gridLayout_16.addWidget(self.withdraw_amount_line_edit, 0, 1, 1, 1)


        self.gridLayout_14.addWidget(self.widget_14, 1, 0, 1, 1)

        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_15 = QGridLayout(self.widget_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_6 = QLabel(self.widget_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 0))

        self.gridLayout_15.addWidget(self.label_6, 0, 0, 1, 1)

        self.withdraw_destination_address_line_edit = QLineEdit(self.widget_13)
        self.withdraw_destination_address_line_edit.setObjectName(u"withdraw_destination_address_line_edit")

        self.gridLayout_15.addWidget(self.withdraw_destination_address_line_edit, 0, 1, 1, 1)


        self.gridLayout_14.addWidget(self.widget_13, 0, 0, 1, 1)

        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_17 = QGridLayout(self.widget_15)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.withdraw_send_button = QPushButton(self.widget_15)
        self.withdraw_send_button.setObjectName(u"withdraw_send_button")
        self.withdraw_send_button.setMinimumSize(QSize(150, 30))
        self.withdraw_send_button.setStyleSheet(u"#withdraw_send_button{\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(35, 166, 171);\n"
"background-color: rgb(35, 166, 171);\n"
"	color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"#withdraw_send_button::hover{\n"
"border-radius: 5px;\n"
"\n"
"border: 2px solid  rgb(206, 206, 206);\n"
"}")

        self.gridLayout_17.addWidget(self.withdraw_send_button, 0, 1, 1, 1)


        self.gridLayout_14.addWidget(self.widget_15, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.withdraw_tab, "")
        self.history_tab = QWidget()
        self.history_tab.setObjectName(u"history_tab")
        self.gridLayout_18 = QGridLayout(self.history_tab)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.widget_16 = QWidget(self.history_tab)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_19 = QGridLayout(self.widget_16)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.histoy_widget = QWidget(self.widget_16)
        self.histoy_widget.setObjectName(u"histoy_widget")
        self.histoy_widget.setMinimumSize(QSize(0, 30))
        self.gridLayout_20 = QGridLayout(self.histoy_widget)
        self.gridLayout_20.setObjectName(u"gridLayout_20")

        self.gridLayout_19.addWidget(self.histoy_widget, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.widget_16, 0, 0, 1, 1)

        self.tabWidget.addTab(self.history_tab, "")

        self.gridLayout_12.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_7, 2, 0, 1, 1)

        self.widget_17 = QWidget(self.widget_3)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 30))
        self.gridLayout_21 = QGridLayout(self.widget_17)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_21.addWidget(self.label_8, 0, 0, 1, 1)

        self.public_key_label = QLabel(self.widget_17)
        self.public_key_label.setObjectName(u"public_key_label")

        self.gridLayout_21.addWidget(self.public_key_label, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_17, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.listWidget.setCurrentRow(-1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.create_wallet_button.setText(QCoreApplication.translate("MainWindow", u"Create New Wallet", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wallet List", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.state_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wallet Adress", None))
        self.wallet_address_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.balance_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Last Activity", None))
        self.last_activity_label.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Destination Adress", None))
        self.withdraw_send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.withdraw_tab), QCoreApplication.translate("MainWindow", u"Withdraw", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history_tab), QCoreApplication.translate("MainWindow", u"History", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Public key", None))
        self.public_key_label.setText("")
    # retranslateUi

