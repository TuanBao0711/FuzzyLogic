import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


class Fuzzy():
    def __init__(self, gdp_value, unemploy_value, infla_value):

        self.gdp = ctrl.Antecedent(np.arange(700, 60100), 'Gross Domestic Product')
        self.gdp['low'] = fuzz.trapmf(self.gdp.universe,  [0, 6000, 10000, 13000])
        self.gdp['medium'] = fuzz.trapmf(self.gdp.universe,  [10000, 14000, 20000, 24000])
        self.gdp['high'] = fuzz.trapmf(self.gdp.universe,[20000, 25000, 100000, 120000])
        # gdp.view()

        self.unemp = ctrl.Antecedent(np.arange(0, 16), 'Unemployment Rate')
        self.unemp['low'] = fuzz.trapmf(self.unemp.universe, [0, 2, 3, 5])
        self.unemp['medium'] = fuzz.trapmf(self.unemp.universe, [3, 6, 7, 10])
        self.unemp['high'] = fuzz.trapmf(self.unemp.universe, [8, 10, 15, 30])
        # unemp.view()

        self.infla = ctrl.Antecedent(np.arange(0, 21), 'Inflation Rate')
        self.infla['low'] = fuzz.trapmf(self.infla.universe, [-20, 0, 3, 4])
        self.infla['medium'] = fuzz.trapmf(self.infla.universe, [3, 4, 8, 10])
        self.infla['high'] = fuzz.trapmf(self.infla.universe, [8, 10, 20, 1000])
        # infla.view()





        self.cmd = ctrl.Consequent(np.arange(0, 21), 'command')
        self.cmd['low'] = fuzz.trimf(self.cmd.universe,[0, 4, 8])
        self.cmd['medium'] = fuzz.trimf(self.cmd.universe, [6, 10, 14])
        self.cmd['high'] = fuzz.trimf(self.cmd.universe, [12, 16, 20])

        rule1 = ctrl.Rule(
            (self.gdp['low'] & self.unemp['low'] & self.infla['high']) |
            (self.gdp['low'] & self.unemp['medium'] & self.infla['medium']) |
            (self.gdp['low'] & self.unemp['medium'] & self.infla['high']) |
            (self.gdp['low'] & self.unemp['high'] & self.infla['low']) |
            (self.gdp['low'] & self.unemp['high'] & self.infla['medium']) |
            (self.gdp['low'] & self.unemp['high'] & self.infla['high']) |
            (self.gdp['medium'] & self.unemp['medium'] & self.infla['high']) |
            (self.gdp['medium'] & self.unemp['high'] & self.infla['medium']) |
            (self.gdp['medium'] & self.unemp['high'] & self.infla['high']), self.cmd['low']
        )

        rule2 = ctrl.Rule(
            (self.gdp['low'] & self.unemp['low'] & self.infla['low']) |
            (self.gdp['low'] & self.unemp['low'] & self.infla['medium']) |
            (self.gdp['low'] & self.unemp['medium'] & self.infla['low']) |
            (self.gdp['medium'] & self.unemp['low'] & self.infla['medium']) |
            (self.gdp['medium'] & self.unemp['low'] & self.infla['high']) |
            (self.gdp['medium'] & self.unemp['medium'] & self.infla['low']) |
            (self.gdp['medium'] & self.unemp['medium'] & self.infla['medium']) |
            (self.gdp['medium'] & self.unemp['high'] & self.infla['low']) |
            (self.gdp['high'] & self.unemp['low'] & self.infla['high']) |
            (self.gdp['high'] & self.unemp['medium'] & self.infla['medium']) |
            (self.gdp['high'] & self.unemp['medium'] & self.infla['high']) |
            (self.gdp['high'] & self.unemp['high'] & self.infla['low']) |
            (self.gdp['high'] & self.unemp['high'] & self.infla['medium']) |
            (self.gdp['high'] & self.unemp['high'] & self.infla['high']), self.cmd['medium']
            )

        rule3 = ctrl.Rule(
            (self.gdp['medium'] & self.unemp['low'] & self.infla['low']) |
            (self.gdp['high'] & self.unemp['low'] & self.infla['low']) |
            (self.gdp['high'] & self.unemp['low'] & self.infla['medium']) |
            (self.gdp['high'] & self.unemp['medium'] & self.infla['low']), self.cmd['high']
        )
        self.cmd_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
        self.cmd_output = ctrl.ControlSystemSimulation(self.cmd_ctrl)



        self.cmd_output.input['Gross Domestic Product'] = gdp_value
        self.cmd_output.input['Unemployment Rate'] = unemploy_value
        self.cmd_output.input['Inflation Rate'] = infla_value
        self.cmd_output.compute()
        
        self.gdp_membership_low = fuzz.interp_membership(self.gdp.universe, self.gdp['low'].mf, gdp_value)
        self.gdp_membership_medium = fuzz.interp_membership(self.gdp.universe, self.gdp['medium'].mf, gdp_value)
        self.gdp_membership_high = fuzz.interp_membership(self.gdp.universe, self.gdp['high'].mf, gdp_value)
        
        self.unemp_membership_low = fuzz.interp_membership(self.unemp.universe, self.unemp['low'].mf, unemploy_value)
        self.unemp_membership_medium = fuzz.interp_membership(self.unemp.universe, self.unemp['medium'].mf, unemploy_value)
        self.unemp_membership_high = fuzz.interp_membership(self.unemp.universe, self.unemp['high'].mf, unemploy_value)
        
        self.infla_membership_low = fuzz.interp_membership(self.infla.universe, self.infla['low'].mf, infla_value)
        self.infla_membership_medium = fuzz.interp_membership(self.infla.universe, self.infla['medium'].mf, infla_value)
        self.infla_membership_high = fuzz.interp_membership(self.infla.universe, self.infla['high'].mf, infla_value)
        
        self.membership_low = fuzz.interp_membership(self.cmd.universe, self.cmd['low'].mf, self.cmd_output.output['command'])
        self.membership_medium = fuzz.interp_membership(self.cmd.universe, self.cmd['medium'].mf, self.cmd_output.output['command'])
        self.membership_high = fuzz.interp_membership(self.cmd.universe, self.cmd['high'].mf, self.cmd_output.output['command'])
    def getResult(self):
        fig, ax = plt.subplots()
        self.cmd.view(sim = self.cmd_output, ax=ax)
        plt.close(fig)
        plt.savefig('img.png')
        plt.close()
        return round(self.cmd_output.output['command'], 5)
    
    def getMemberGDP(self):
        return [self.gdp_membership_low, self.gdp_membership_medium, self.gdp_membership_high]
    
    def getMemberUnemp(self):
        return [self.unemp_membership_low, self.unemp_membership_medium, self.unemp_membership_high]
    
    def getMemberInfla(self):
        return [self.infla_membership_low, self.infla_membership_medium, self.infla_membership_high]
    
    

# cmd.view(sim=cmd_output)

# plt.show()