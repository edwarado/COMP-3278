# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin/ui_files/admin_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Admin_Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 505)
        MainWindow.setMaximumSize(QtCore.QSize(561, 505))
        MainWindow.setStyleSheet("background-color: rgb(171, 171, 171);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(5000, 5000))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Logout.setGeometry(QtCore.QRect(420, 321, 111, 31))
        self.pushButton_Logout.setMaximumSize(QtCore.QSize(171, 16777215))
        self.pushButton_Logout.setObjectName("pushButton_Logout")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 90, 491, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_CheckAllAccount = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_CheckAllAccount.setMaximumSize(QtCore.QSize(481, 16777215))
        self.pushButton_CheckAllAccount.setObjectName("pushButton_CheckAllAccount")
        self.verticalLayout.addWidget(self.pushButton_CheckAllAccount)
        self.pushButton_Transfer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Transfer.setMaximumSize(QtCore.QSize(481, 16777215))
        self.pushButton_Transfer.setObjectName("pushButton_Transfer")
        self.verticalLayout.addWidget(self.pushButton_Transfer)
        self.pushButton_Profile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Profile.setMaximumSize(QtCore.QSize(481, 16777215))
        self.pushButton_Profile.setObjectName("pushButton_Profile")
        self.verticalLayout.addWidget(self.pushButton_Profile)
        self.pushButton_LoginHistory = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_LoginHistory.setMaximumSize(QtCore.QSize(481, 16777215))
        self.pushButton_LoginHistory.setObjectName("pushButton_LoginHistory")
        self.verticalLayout.addWidget(self.pushButton_LoginHistory)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 50, 271, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 269, 29))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Logout.setText(_translate("MainWindow", "Logout"))
        self.pushButton_CheckAllAccount.setText(_translate("MainWindow", "Accounts"))
        self.pushButton_Transfer.setText(_translate("MainWindow", "Transactions"))
        self.pushButton_Profile.setText(_translate("MainWindow", "User Profiles"))
        self.pushButton_LoginHistory.setText(_translate("MainWindow", "User Login History"))
        self.label.setText(_translate("MainWindow", "WELCOME TO YOUR BANK ACCOUNT!"))
        self.label_2.setText(_translate("MainWindow", "ADMIN"))
