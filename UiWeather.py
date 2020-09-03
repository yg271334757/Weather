# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\27133\Desktop\Weather\weather.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WeatherCheck(object):
    def setupUi(self, WeatherCheck):
        WeatherCheck.setObjectName("WeatherCheck")
        WeatherCheck.resize(576, 401)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/UiRecourses/images/weather.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WeatherCheck.setWindowIcon(icon)
        WeatherCheck.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(WeatherCheck)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(30, 30))
        self.label.setStyleSheet("image: url(:/UiRecourses/images/city.png);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(0)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_city = QtWidgets.QLabel(self.centralwidget)
        self.label_city.setStyleSheet("\n"
"background-image: url(:/UiRecourses/images/city.png);")
        self.label_city.setObjectName("label_city")
        self.horizontalLayout.addWidget(self.label_city)
        self.lineEdit_city = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.horizontalLayout.addWidget(self.lineEdit_city)
        self.pushButton_inquire = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/UiRecourses/images/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_inquire.setIcon(icon1)
        self.pushButton_inquire.setObjectName("pushButton_inquire")
        self.horizontalLayout.addWidget(self.pushButton_inquire)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit_show = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_show.setReadOnly(True)
        self.textEdit_show.setObjectName("textEdit_show")
        self.verticalLayout.addWidget(self.textEdit_show)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_clearall = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/UiRecourses/images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clearall.setIcon(icon2)
        self.pushButton_clearall.setObjectName("pushButton_clearall")
        self.horizontalLayout_3.addWidget(self.pushButton_clearall)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        WeatherCheck.setCentralWidget(self.centralwidget)

        self.retranslateUi(WeatherCheck)
        self.pushButton_clearall.clicked.connect(self.textEdit_show.clear)
        self.pushButton_clearall.clicked.connect(self.lineEdit_city.clear)
        self.pushButton_inquire.clicked.connect(WeatherCheck.querWeather)
        QtCore.QMetaObject.connectSlotsByName(WeatherCheck)


    def retranslateUi(self, WeatherCheck):
        _translate = QtCore.QCoreApplication.translate
        WeatherCheck.setWindowTitle(_translate("WeatherCheck", "WeatherCheck"))
        self.label_city.setText(_translate("WeatherCheck", "城市:"))
        self.pushButton_inquire.setText(_translate("WeatherCheck", "查询"))
        self.pushButton_clearall.setText(_translate("WeatherCheck", "清空"))
import resources_rc
