import sys
import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from pyqtui import Ui_MainWindow


class MyFigure(FigureCanvas):
    def __init__(self, width, height, dpi):
        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 创建一个Figure
        super(MyFigure, self).__init__(self.fig)  # 在父类中激活Figure窗口
        self.axes = self.fig.add_subplot(111)  # 调用Figure下面的add_subplot方法


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.test = MyFigure(width=3, height=2, dpi=100)
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.test, 0, 1)

    def plot(self):
        x = [i for i in range(11)]
        y = x
        self.test.axes.plot(x, y)
        self.test.fig.suptitle("hello word")  # 设置总标题
        self.test.axes.set_xlabel('X_Label')  # 设置x轴标题
        self.test.axes.set_ylabel('Y_Label')  # 设置Y轴标题


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('D:/Python/2021/pyqt/test/b.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.show()
    sys.exit(app.exec_())