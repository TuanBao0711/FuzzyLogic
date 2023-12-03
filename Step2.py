import sys
import skfuzzy as fuzz
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5 import QtGui, QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MyTable(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)

        self.setGeometry(0, 0, 600, 500)

        # Đặt tiêu đề cột
        column_headers = ['GDP Bình quân ', 'Tỷ lệ thất nghiệp', 'Tỷ lệ lạm phát', 'Mức độ phát triển kinh tế']
        self.setHorizontalHeaderLabels(column_headers)

        # Điền dữ liệu vào bảng
        data = [['Thấp', 'Thấp', 'Thấp', 'Trung bình'], ['Thấp', 'Thấp', 'Trung bình', 'Trung bình'], ['Thấp', 'Thấp', 'Cao', 'Thấp'], ['Thấp', 'Trung bình', 'Thấp', 'Trung Bình'], ['Thấp', 'Trung bình', 'Trung Bình', 'Thấp'], ['Thấp', 'Trung bình', 'Cao', 'Thấp'], ['Thấp', 'Cao', 'Thấp', 'Thấp'], ['Thấp', 'Cao', 'Trung Bình', 'Thấp'], ['Thấp', 'Cao', 'Cao', 'Thấp'], ['Trung bình', 'Thấp', 'Thấp', 'Cao'], ['Trung bình', 'Thấp', 'Trung Bình', 'Trung Bình'], ['Trung bình', 'Thấp', 'Cao', 'Trung Bình'], ['Trung bình', 'Trung Bình', 'Thấp', 'Trung Bình'], ['Trung bình', 'Trung Bình', 'Trung Bình', 'Trung Bình'], ['Trung bình', 'Trung Bình', 'Cao', 'Thấp'], ['Trung bình', 'Cao', 'Thấp', 'Trung Bình'], ['Trung bình', 'Cao', 'Trung Bình', 'Thấp'], ['Trung bình', 'Cao', 'Cao', 'Thấp'], ['Cao', 'Thấp', 'Thấp', 'Cao'], ['Cao', 'Thấp', 'Trung Bình', 'Cao'], ['Cao', 'Thấp', 'Cao', 'Trung Bình'], ['Cao', 'Trung Bình', 'Thấp', 'Cao'], ['Cao', 'Trung Bình', 'Trung Bình', 'Trung Bình'], ['Cao', 'Trung Bình', 'Cao', 'Trung Bình'], ['Cao', 'Cao', 'Thấp', 'Trung Bình'], ['Cao', 'Cao', 'Trung Bình', 'Trung Bình'], ['Cao', 'Cao', 'Cao', 'Trung Bình']]
        

        for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(col)
                self.setItem(i, j, item)

class FuzzyPlot(FigureCanvas):
    def __init__(self, parent=None  ):
        fig, ax = plt.subplots()
        
        x = np.arange(0, 22)
        low_membership = fuzz.trimf(x, [0, 4, 8])
        medium_membership =fuzz.trimf(x, [6, 10, 14])
        high_membership = fuzz.trimf(x, [12, 16, 20])

        ax.plot(x, low_membership, label='Low')
        ax.plot(x, medium_membership, label='Medium')
        ax.plot(x, high_membership, label='High')
        ax.set_title('Tieeu ddeef')
        ax.set_xlabel('command')
        ax.set_ylabel('Membership Value')
        ax.legend()


        super().__init__(fig)
        self.setParent(parent)


class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1200, 600)
        self.setWindowTitle('PyQt5 Table Example')

        # Tạo một đối tượng MyTable và thêm nó vào khung chính
        self.table = MyTable(27, 4)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QHBoxLayout(self.central_widget)

        # Tạo một layout riêng cho đồ thị và thêm nó vào layout chính
        graph_layout = QVBoxLayout()

        graph_layout.addWidget(self.table)
        label_layout = QVBoxLayout()
        

        # Thêm cả hai layout vào layout chính

        
        self.plot = FuzzyPlot()
        label_layout.addWidget(self.plot)
        layout.addLayout(graph_layout)
        layout.addLayout(label_layout)


