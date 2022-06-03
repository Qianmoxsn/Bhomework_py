import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import funcs
import data
import gl_VAR
import GUI.test1 as gui

import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
#from pyqtui import Ui_MainWindow

import json

import numpy as np
import logging
import os

import time



if __name__ == '__main__':

    # 输入配置参数并配置
    gl_VAR.g_totsta, gl_VAR.g_stg, gl_VAR.g_dis = funcs.SET_CONFIG()
    data.CONFIG(nsta=gl_VAR.g_totsta, stg=gl_VAR.g_stg, dis=gl_VAR.g_dis)

    # 初始化data.py中的变量
    data.BUS_CON.setvar(0, 0, 0, '0' * gl_VAR.g_totsta)
    data.STA_CON.setvar('0' * gl_VAR.g_totsta, '0' * gl_VAR.g_totsta)

    # 删除先前文件
    f = open('GUI/outfile.txt', 'a')
    f.seek(0)
    f.truncate()

    # 运行
    funcs.OP_C(data.BUS_CON, data.STA_CON)  # 第一次运行，输出结果
    while True:
        code, instr = funcs.IP_C()
        if code == -2:
            continue

        if code == 1 or code == 2 or code == 3:
            # 执行ADD_SED函数
            state = funcs.ADD_SED(code, instr)
            if state == 'ST_BY':
                pass
            # 执行ADD_CON函数
            funcs.ADD_CON()
            # print("<-sedlst->\n", data.SED_LST)
        elif code == 0:
            # 执行BUS_MOV函数
            if funcs.BUS_MOV() == 'ST_BY':
                pass
            # 执行TIMR函数
            funcs.TIMR()
            # 执行OP_C函数
            # funcs.OP_C(data.BUS_CON, data.STA_CON)
            # 执行OP_C_F函数
            funcs.OP_C_F(data.BUS_CON)
        elif code == -1:
            # funcs.OP_C_E()
            # exit(-1)
            class MyFigure(FigureCanvas):
                def __init__(self, width, height, dpi):
                    self.fig = Figure(figsize=(width, height), dpi=dpi)  # 创建一个Figure
                    super(MyFigure, self).__init__(self.fig)  # 在父类中激活Figure窗口
                    self.axes = self.fig.add_subplot(111)  # 调用Figure下面的add_subplot方法


            class Window(QMainWindow, gui.Ui_MainWindow):
                def __init__(self, parent=None):
                    super(Window, self).__init__(parent)
                    self.setupUi(self)
                    self.test = MyFigure(width=3, height=2, dpi=100)
                    self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
                    self.gridlayout.addWidget(self.test, 0, 1)

                def plot(self):
                    x = [5.7735, 2.8868, -2.8868, -5.7735, -2.8868, 2.8868]
                    y = [0, -5, -5, 0, 5, 5]
                    self.test.axes.scatter(x, y)
                    self.test.fig.suptitle("hello word")  # 设置总标题
                    self.test.axes.set_xlabel('X_Label')  # 设置x轴标题
                    self.test.axes.set_ylabel('Y_Label')  # 设置Y轴标题

            # gui
            app = QApplication(sys.argv)
            MainWindow = QMainWindow()
            #app.setWindowIcon(QIcon('D:/Python/2021/pyqt/test/b.ico'))
            ui = gui.Ui_MainWindow()
            # 初始化页面控件
            ui.setupUi(MainWindow)
            # 设定进度条最大值（总时长）
            ui.set_progressbar(gl_VAR.g_time)
            # 设定配置文件（现实）
            ui.config(strategy=gl_VAR.g_stg, distance=str(gl_VAR.g_dis), stations=str(gl_VAR.g_totsta))
            # 设定总时间（显示）
            ui.set_GT(GT=str(gl_VAR.g_time))
            # 开启页面
            MainWindow.show()
            ui = Window()
            ui.show()
            sys.exit(app.exec_())
