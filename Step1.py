import sys
import numpy as np
import skfuzzy as fuzz
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class FuzzyPlotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fuzzy Plot with Text")
        self.setGeometry(200, 200, 1200, 600)

        # Tạo widget chính
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Tạo layout cho widget chính
        layout = QVBoxLayout(central_widget)

        # Tạo biểu đồ và thêm vào layout
        fuzzy_plot = FuzzyPlot()
        layout.addWidget(fuzzy_plot)

        # Tạo một QLabel với văn bản và thêm vào layout
        # text_label = QLabel("Additional Text Below the Plot", self)
        # text_label.setAlignment(Qt.AlignCenter)
        # layout.addWidget(text_label)
        
class FuzzyPlot(FigureCanvas):
    def __init__(self, parent=None):
        fig, ax = plt.subplots(1,3)
        
        x = np.arange(0, 60100)
        low_membership = fuzz.trapmf(x, [0, 6000, 10000, 13000])
        medium_membership = fuzz.trapmf(x, [10000, 14000, 20000, 24000])
        high_membership = fuzz.trapmf(x, [20000, 25000, 100000, 120000])
        # ax[0].vlines(x=7500, ymin=0, ymax=1, color='r', linestyle='--', label='GDP Index')
        ax[0].plot(x, low_membership, label='Low')
        ax[0].plot(x, medium_membership, label='Medium')
        ax[0].plot(x, high_membership, label='High')
        ax[0].set_title('Fuzzy Membership Functions for GDP')
        ax[0].set_xlabel('Gross Domestic Product')
        ax[0].set_ylabel('Membership Value')
        ax[0].legend()

        
        x = np.arange(0, 16)
        low_membership = fuzz.trapmf(x, [0, 2, 3, 5])
        medium_membership = fuzz.trapmf(x, [3, 6, 7, 10])
        high_membership = fuzz.trapmf(x, [8, 10, 15, 30])
        # ax[1].vlines(x=7, ymin=0, ymax=1, color='r', linestyle='--', label='Unemployment Index')
        ax[1].plot(x, low_membership, label='Low')
        ax[1].plot(x, medium_membership, label='Medium')
        ax[1].plot(x, high_membership, label='High')
        ax[1].set_title('Fuzzy Membership Functions for Unemployment Rate')
        ax[1].set_xlabel('Unemployment Rate')
        ax[1].set_ylabel('Membership Value')
        ax[1].legend()
        
        x = np.arange(0, 20)
        low_membership = fuzz.trapmf(x, [-20, 0, 3, 4])
        medium_membership = fuzz.trapmf(x, [3, 4, 8, 10])
        high_membership = fuzz.trapmf(x, [8, 10, 20, 1000])
        # ax[2].vlines(x=7.5, ymin=0, ymax=1, color='r', linestyle='--', label='Inflation Index')
        ax[2].plot(x, low_membership, label='Low')
        ax[2].plot(x, medium_membership, label='Medium')
        ax[2].plot(x, high_membership, label='High')
        ax[2].set_title('Fuzzy Membership Functions for Inflation Rate')
        ax[2].set_xlabel('Inflation Rate')
        ax[2].set_ylabel('Membership Value')
        ax[2].legend()
        
        
        super().__init__(fig)
        self.setParent(parent)

