# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWindow(object):

    def __init__(self, MenuEventHandler):
        self.MenuEventHandler = MenuEventHandler

    def handleUserClickEvent(self):
        self.MenuEventHandler('userMenu')

    def handleAdminClickEvent(self):
        self.MenuEventHandler('adminMenu')

    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(780, 390)
        MenuWindow.setStyleSheet("background-color : white;\n")
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 60, 521, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userMenuButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userMenuButton.sizePolicy().hasHeightForWidth())
        self.userMenuButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(18)
        self.userMenuButton.setFont(font)
        self.userMenuButton.clicked.connect(self.handleUserClickEvent)
        self.userMenuButton.setStyleSheet(
                "border-width : 3px;"
                "border-color : blue;"
                "border-style : solid;"
                "border-radius : 30%;"
                "background-color : white;")
        self.userMenuButton.setObjectName("userMenuButton")
        self.horizontalLayout.addWidget(self.userMenuButton)
        self.adminMenuButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adminMenuButton.sizePolicy().hasHeightForWidth())
        self.adminMenuButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(18)
        self.adminMenuButton.setFont(font)
        self.adminMenuButton.clicked.connect(self.handleAdminClickEvent)
        self.adminMenuButton.setStyleSheet(
                "border-width : 3px;"
                "border-color : blue;"
                "border-style : solid;"
                "border-radius : 30%;"
                "background-color : white;")
        self.adminMenuButton.setObjectName("adminMenuButton")
        self.horizontalLayout.addWidget(self.adminMenuButton)
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 26))
        self.menubar.setObjectName("menubar")
        MenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "MainWindow"))
        self.userMenuButton.setText(_translate("MenuWindow", "사용자 메뉴"))
        self.adminMenuButton.setText(_translate("MenuWindow", "관리자 메뉴"))