# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Fuzzy import Fuzzy
from Result import MyMplCanvas, ResulWindow
from Step1 import FuzzyPlotApp
from Step2 import TableWindow
from Step3 import FuzzyPlotAppStep3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 270, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 460, 211, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 90, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 270, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 460, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(750, 90, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(750, 270, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(750, 460, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1149, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # self.pushButton.clicked.connect(self.Run)
        self.pushButton2.clicked.connect(self.Step1)
        self.pushButton3.clicked.connect(self.Step2)
        self.pushButton4.clicked.connect(self.Step3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GDP đầu người"))
        self.label_2.setText(_translate("MainWindow", "Tỷ lệ thất nghiệp"))
        self.label_3.setText(_translate("MainWindow", "Lạm phát"))
        self.pushButton2.setText(_translate("MainWindow", "Bước 1"))
        self.pushButton3.setText(_translate("MainWindow", "Bước 2"))
        self.pushButton4.setText(_translate("MainWindow", "Bước 3"))

        
        

    def Step3(self):
        self.gdp_value = float(self.lineEdit.text())
        self.unemploy_value = float(self.lineEdit_2.text())
        self.infla_value = float(self.lineEdit_3.text())
        self.Fuzzy = Fuzzy(self.gdp_value, self.unemploy_value, self.infla_value)
        self.memberGDP = self.Fuzzy.getMemberGDP()
        self.memberUnemp = self.Fuzzy.getMemberUnemp()
        self.memberInfla = self.Fuzzy.getMemberInfla()
        
        self.resultUI = ResulWindow(self.gdp_value, self.unemploy_value, self.infla_value,self.Fuzzy.getResult(), self.memberGDP, self.memberUnemp, self.memberInfla, self.Fuzzy.membership_low, self.Fuzzy.membership_medium, self.Fuzzy.membership_high)
        
        # self.resultUI.plot_graph()
        self.resultUI.show()
        
    
    def Step1(self):
        self.step1 = FuzzyPlotApp()
        self.step1.show()
        
    def Step2(self):
        self.step2 = TableWindow()
        self.step2.show()
        
    # def Step3(self):
    #     self.step3 = FuzzyPlotAppStep3()
    #     self.step3.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
