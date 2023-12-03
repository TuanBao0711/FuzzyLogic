import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QPixmap
from matplotlib.figure import Figure
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

from Fuzzy import Fuzzy

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=3, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MyMplCanvas, self).__init__(fig)
        

class ResulWindow(QMainWindow):
    def __init__(self, gdp, unem, infla, result,memberGDP, memberUnemp, memberInfla  ,  result_low, result_medium, result_high):
        super(ResulWindow, self).__init__()

        self.setGeometry(100, 100, 1600, 800)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QHBoxLayout(self.central_widget)

        # Tạo một layout riêng cho đồ thị và thêm nó vào layout chính
        graph_layout = QVBoxLayout()
        self.plot = FuzzyPlot(gdp, unem, infla, result,memberGDP, memberUnemp, memberInfla, result_low, result_medium, result_high)
        graph_layout.addWidget(self.plot)
        # graph_layout.addWidget(self.mpl_canvas)
        label_layout = QVBoxLayout()
        

        # Thêm cả hai layout vào layout chính

        self.label_img = QtWidgets.QLabel(self)
        self.label_img.setGeometry(QtCore.QRect(50,10, 250, 250))
        self.label_img.setPixmap(QPixmap('img.png'))
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 90, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.result = 'Mức phát triển thấp: {}\nMức phát triển trung bình: {}\nMức phát triển cao: {}'.format(round(result_low,4), round(result_medium,4),round(result_high,4))
        self.label.setText(str(self.result))

        label_layout.addWidget(self.label_img)
        label_layout.addWidget(self.label)
        layout.addLayout(graph_layout)
        layout.addLayout(label_layout)
        # self.plot_graph()


class FuzzyPlot(FigureCanvas):
    def __init__(self,gdp, unem, infla, result ,memberGDP, memberUnemp, memberInfla, result_low, result_medium, result_high, parent=None):
        fig, ax = plt.subplots()
        
        fig, ax = plt.subplots(2,2)
        
        x = np.arange(0, 60100)
        low_membership = fuzz.trapmf(x, [0, 6000, 10000, 13000])
        medium_membership = fuzz.trapmf(x, [10000, 14000, 20000, 24000])
        high_membership = fuzz.trapmf(x, [20000, 25000, 100000, 120000])
        ax[0][0].vlines(x=gdp, ymin=0, ymax=1, color='r', linestyle='--', label='GDP Index')
        ax[0][0].plot(x, low_membership, label='Low: {}'.format(round(memberGDP[0],4)) )
        ax[0][0].plot(x, medium_membership, label='Medium: {}'.format(round(memberGDP[1],4)))
        ax[0][0].plot(x, high_membership, label='High: {}'.format(round(memberGDP[2],4)))
        ax[0][0].set_title('Fuzzy Membership Functions for GDP')
        ax[0][0].set_xlabel('Gross Domestic Product')
        ax[0][0].set_ylabel('Membership Value')
        ax[0][0].legend()

        
        x = np.arange(0, 16)
        low_membership = fuzz.trapmf(x, [0, 2, 3, 5])
        medium_membership = fuzz.trapmf(x, [3, 6, 7, 10])
        high_membership = fuzz.trapmf(x, [8, 10, 15, 30])
        ax[0][1].vlines(x=unem, ymin=0, ymax=1, color='r', linestyle='--', label='Unemployment Index')
        ax[0][1].plot(x, low_membership, label='Low: {}'.format(round(memberUnemp[0],4)))
        ax[0][1].plot(x, medium_membership, label='Medium: {}'.format(round(memberUnemp[1],4)))
        ax[0][1].plot(x, high_membership, label='High: {}'.format(round(memberUnemp[2],4)))
        ax[0][1].set_title('Fuzzy Membership Functions for Unemployment Rate')
        ax[0][1].set_xlabel('Unemployment Rate')
        ax[0][1].set_ylabel('Membership Value')
        ax[0][1].legend()
        
        x = np.arange(0, 20)
        low_membership = fuzz.trapmf(x, [-20, 0, 3, 4])
        medium_membership = fuzz.trapmf(x, [3, 4, 8, 10])
        high_membership = fuzz.trapmf(x, [8, 10, 20, 1000])
        ax[1][0].vlines(x=infla, ymin=0, ymax=1, color='r', linestyle='--', label='Inflation Index')
        ax[1][0].plot(x, low_membership, label='Low: {}'.format(round(memberInfla[0],4)))
        ax[1][0].plot(x, medium_membership, label='Medium: {}'.format(round(memberInfla[1],4)))
        ax[1][0].plot(x, high_membership, label='High: {}'.format(round(memberInfla[2],4)))
        ax[1][0].set_title('Fuzzy Membership Functions for Inflation Rate')
        ax[1][0].set_xlabel('Inflation Rate')
        ax[1][0].set_ylabel('Membership Value')
        ax[1][0].legend()
        
        x = np.arange(0, 22)
        low_membership = fuzz.trimf(x, [0, 4, 8])
        medium_membership =fuzz.trimf(x, [6, 10, 14])
        high_membership = fuzz.trimf(x, [12, 16, 20])
        ax[1][1].vlines(x=result, ymin=0, ymax=1, color='r', linestyle='--', label='Cmd Value')
        ax[1][1].plot(x, low_membership, label='Low, Membership = {}'.format(round(result_low,4)))
        ax[1][1].plot(x, medium_membership, label='Medium, Membership = {}'.format(round(result_medium,4)))
        ax[1][1].plot(x, high_membership, label='High, Membership = {}'.format(round(result_high,4)))
        ax[1][1].set_title('Tieeu ddeef')
        ax[1][1].set_xlabel('command')
        ax[1][1].set_ylabel('Membership Value')
        ax[1][1].legend()


        super().__init__(fig)
        self.setParent(parent)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWin = MyMainWindow()
#     mainWin.show()
#     sys.exit(app.exec_())
