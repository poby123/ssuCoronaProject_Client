# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TempInfoDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TempInfoWindow(object):
    def __init__(self, maxTemp, MenuEventHandler):
        self.maxTempPivot = maxTemp
        self.MenuEventHandler = MenuEventHandler

    def handleBackClickEvent(self):
        self.MenuEventHandler('backward')

    def setupUi(self, TempInfoWindow):
        TempInfoWindow.setObjectName("TempInfoWindow")
        TempInfoWindow.resize(780, 390)
        TempInfoWindow.setStyleSheet("background: white")
        self.centralwidget = QtWidgets.QWidget(TempInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 10, 561, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.handleBackClickEvent)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handleBackClickEvent)
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(18)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        self.nameValueLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(18)
        self.nameValueLabel.setFont(font)
        self.nameValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameValueLabel.setObjectName("nameValueLabel")
        self.horizontalLayout.addWidget(self.nameValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.statusLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.statusLabel.setFont(font)
        self.statusLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        TempInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TempInfoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 26))
        self.menubar.setObjectName("menubar")
        TempInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TempInfoWindow)
        self.statusbar.setObjectName("statusbar")
        TempInfoWindow.setStatusBar(self.statusbar)
        self.retranslateUi(TempInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(TempInfoWindow)

    def retranslateUi(self, TempInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        TempInfoWindow.setWindowTitle(_translate("TempInfoWindow", "MainWindow"))
        self.nameLabel.setText(_translate("TempInfoWindow", "이름 : "))
        self.pushButton.setText(_translate("WelcomeWindow", "뒤로가기"))
    
    def setName(self, nameValue):
        # self.nameValueLabel.setText(_translate("TempInfoWindow", nameValue))
        self.nameValueLabel.setText(nameValue)

    def setStatus(self, msg):
        # self.statusLabel.setText(_translate("TempInfoWindow", temp))
        defaultColor = {"background":"#87CEFA", "border":"#1E90FF"}
        warningColor = {"background":"red", "border":"red"}
        selectedColor = defaultColor
        if(type(msg) == float):
            if(msg > self.maxTempPivot):
                selectedColor = warningColor
            msg = str(msg); 
            msg += "°C"

        self.statusLabel.setText(msg)
        self.statusLabel.setStyleSheet(
            f"color: white;"
            f"background-color: {selectedColor['background']};" 
            "border-style: dashed;"
            "border-width: 3px;" 
            f"border-color: {selectedColor['border']}"
        )