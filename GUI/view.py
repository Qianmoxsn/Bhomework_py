# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(40, 10, 371, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.title_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.title_label_2.setGeometry(QtCore.QRect(580, 30, 91, 28))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.title_label_2.setFont(font)
        self.title_label_2.setObjectName("title_label_2")
        self.time_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.time_lcd.setGeometry(QtCore.QRect(687, 20, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_lcd.sizePolicy().hasHeightForWidth())
        self.time_lcd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.time_lcd.setFont(font)
        self.time_lcd.setObjectName("time_lcd")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(681, 476, 104, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.next_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.next_button.setFont(font)
        self.next_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_button.setObjectName("next_button")
        self.verticalLayout.addWidget(self.next_button)
        self.auto_button = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.auto_button.setFont(font)
        self.auto_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.auto_button.setMouseTracking(True)
        self.auto_button.setObjectName("auto_button")
        self.verticalLayout.addWidget(self.auto_button)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(561, 100, 225, 191))
        self.layoutWidget1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.layoutWidget1.setAutoFillBackground(False)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.stations_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.stations_label.setFont(font)
        self.stations_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stations_label.setAutoFillBackground(False)
        self.stations_label.setObjectName("stations_label")
        self.gridLayout.addWidget(self.stations_label, 2, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.distance_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.distance_label.setFont(font)
        self.distance_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.distance_label.setAutoFillBackground(False)
        self.distance_label.setObjectName("distance_label")
        self.gridLayout.addWidget(self.distance_label, 3, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.stratedy_lable = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.stratedy_lable.setFont(font)
        self.stratedy_lable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stratedy_lable.setAutoFillBackground(False)
        self.stratedy_lable.setObjectName("stratedy_lable")
        self.gridLayout.addWidget(self.stratedy_lable, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.status_label = QtWidgets.QLabel(self.layoutWidget1)
        self.status_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.status_label.setFont(font)
        self.status_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_label.setAutoFillBackground(False)
        self.status_label.setObjectName("status_label")
        self.gridLayout.addWidget(self.status_label, 0, 1, 1, 2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(560, 310, 221, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.exp_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.exp_label.setFont(font)
        self.exp_label.setObjectName("exp_label")
        self.gridLayout_2.addWidget(self.exp_label, 0, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 2)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(560, 400, 239, 71))
        self.layoutWidget3.setMinimumSize(QtCore.QSize(239, 71))
        self.layoutWidget3.setMaximumSize(QtCore.QSize(239, 71))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.layoutWidget3.setFont(font)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setMinimumSize(QtCore.QSize(100, 31))
        self.label_14.setMaximumSize(QtCore.QSize(100, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_15.setMinimumSize(QtCore.QSize(100, 31))
        self.label_15.setMaximumSize(QtCore.QSize(100, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setMinimumSize(QtCore.QSize(100, 31))
        self.label_13.setMaximumSize(QtCore.QSize(100, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_12.setMinimumSize(QtCore.QSize(100, 31))
        self.label_12.setMaximumSize(QtCore.QSize(100, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.st9 = QtWidgets.QPushButton(self.centralwidget)
        self.st9.setGeometry(QtCore.QRect(530, 510, 40, 40))
        self.st9.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st9.setObjectName("st9")
        self.st1 = QtWidgets.QPushButton(self.centralwidget)
        self.st1.setGeometry(QtCore.QRect(130, 510, 40, 40))
        self.st1.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st1.setObjectName("st1")
        self.st10 = QtWidgets.QPushButton(self.centralwidget)
        self.st10.setGeometry(QtCore.QRect(580, 510, 40, 40))
        self.st10.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st10.setObjectName("st10")
        self.st2 = QtWidgets.QPushButton(self.centralwidget)
        self.st2.setGeometry(QtCore.QRect(180, 510, 40, 40))
        self.st2.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st2.setObjectName("st2")
        self.st3 = QtWidgets.QPushButton(self.centralwidget)
        self.st3.setGeometry(QtCore.QRect(230, 510, 40, 40))
        self.st3.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st3.setObjectName("st3")
        self.st4 = QtWidgets.QPushButton(self.centralwidget)
        self.st4.setGeometry(QtCore.QRect(280, 510, 40, 40))
        self.st4.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st4.setObjectName("st4")
        self.st5 = QtWidgets.QPushButton(self.centralwidget)
        self.st5.setGeometry(QtCore.QRect(330, 510, 40, 40))
        self.st5.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st5.setObjectName("st5")
        self.st6 = QtWidgets.QPushButton(self.centralwidget)
        self.st6.setGeometry(QtCore.QRect(380, 510, 40, 40))
        self.st6.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st6.setObjectName("st6")
        self.st7 = QtWidgets.QPushButton(self.centralwidget)
        self.st7.setGeometry(QtCore.QRect(430, 510, 40, 40))
        self.st7.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st7.setObjectName("st7")
        self.st8 = QtWidgets.QPushButton(self.centralwidget)
        self.st8.setGeometry(QtCore.QRect(480, 510, 40, 40))
        self.st8.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,0,255);/*背景色*/\n"
"}")
        self.st8.setObjectName("st8")
        self.con = QtWidgets.QPushButton(self.centralwidget)
        self.con.setGeometry(QtCore.QRect(70, 510, 40, 40))
        self.con.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(0,255,255,255);/*背景色*/\n"
"}")
        self.con.setObjectName("con")
        self.bus = QtWidgets.QPushButton(self.centralwidget)
        self.bus.setGeometry(QtCore.QRect(20, 510, 40, 40))
        self.bus.setStyleSheet("\n"
"QPushButton{/*默认显示*/\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(255,0,0,255);/*背景色*/\n"
"}")
        self.bus.setObjectName("bus")
        self.mm1 = QtWidgets.QLabel(self.centralwidget)
        self.mm1.setGeometry(QtCore.QRect(50, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.mm1.setFont(font)
        self.mm1.setObjectName("mm1")
        self.mm2 = QtWidgets.QLabel(self.centralwidget)
        self.mm2.setGeometry(QtCore.QRect(150, 460, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.mm2.setFont(font)
        self.mm2.setObjectName("mm2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.title_label.setText(_translate("MainWindow", "公交车调度系统动画演示界面（测试）"))
        self.title_label_2.setText(_translate("MainWindow", "运行时间："))
        self.next_button.setText(_translate("MainWindow", "NEXT"))
        self.auto_button.setText(_translate("MainWindow", "AutoRun"))
        self.label_3.setText(_translate("MainWindow", "当前配置文件"))
        self.label_4.setText(_translate("MainWindow", "总车站数："))
        self.stations_label.setText(_translate("MainWindow", "——"))
        self.label_6.setText(_translate("MainWindow", "车站间距："))
        self.distance_label.setText(_translate("MainWindow", "——"))
        self.label_8.setText(_translate("MainWindow", "调度策略："))
        self.stratedy_lable.setText(_translate("MainWindow", "——"))
        self.label.setText(_translate("MainWindow", "运行状态："))
        self.status_label.setText(_translate("MainWindow", "运行/停运"))
        self.label_10.setText(_translate("MainWindow", "预计运行时间"))
        self.exp_label.setText(_translate("MainWindow", "--"))
        self.label_14.setText(_translate("MainWindow", "——"))
        self.label_15.setText(_translate("MainWindow", "——"))
        self.label_13.setText(_translate("MainWindow", "车辆位置"))
        self.label_12.setText(_translate("MainWindow", "车辆位置"))
        self.st9.setText(_translate("MainWindow", "st9"))
        self.st1.setText(_translate("MainWindow", "st1"))
        self.st10.setText(_translate("MainWindow", "st10"))
        self.st2.setText(_translate("MainWindow", "st2"))
        self.st3.setText(_translate("MainWindow", "st3"))
        self.st4.setText(_translate("MainWindow", "st4"))
        self.st5.setText(_translate("MainWindow", "st5"))
        self.st6.setText(_translate("MainWindow", "st6"))
        self.st7.setText(_translate("MainWindow", "st7"))
        self.st8.setText(_translate("MainWindow", "st8"))
        self.con.setText(_translate("MainWindow", "con"))
        self.bus.setText(_translate("MainWindow", "bus"))
        self.mm1.setText(_translate("MainWindow", "型号：ZTZ-99A"))
        self.mm2.setText(_translate("MainWindow", "车长：王宇轩    炮手：汪镕彬    驾驶员：何杰聪"))
