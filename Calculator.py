import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic

class Calculator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.ui = uic.loadUi("Calculator_Gorodov.ui")

        self.ui.DB1_1.valueChanged.connect(self.update)
        self.ui.DB2_1.valueChanged.connect(self.update)
        self.ui.DB3_1.valueChanged.connect(self.update)
        self.ui.DB2_2.valueChanged.connect(self.update)
        self.ui.DB4_3.valueChanged.connect(self.update)
        self.ui.DB5_3.valueChanged.connect(self.update)
        self.ui.DB3_2.valueChanged.connect(self.update)
        self.ui.DB4_2.valueChanged.connect(self.update)
        self.ui.DB5_1.valueChanged.connect(self.update)
        self.ui.DB4_1.valueChanged.connect(self.update)
        self.ui.DB5_2.valueChanged.connect(self.update)

        self.ui.RB1_1.setCheckable(True)
        self.ui.RB2_1.setCheckable(True)
        self.ui.RB3_1.setCheckable(True)
        self.ui.RB4_1.setCheckable(True)
        self.ui.RB5_1.setCheckable(True)
        self.ui.RB1_2.setCheckable(True)
        self.ui.RB2_2.setCheckable(True)
        self.ui.RB3_2.setCheckable(True)
        self.ui.RB4_2.setCheckable(True)
        self.ui.RB5_2.setCheckable(True)

        self.ui.RB1_1.toggled.connect(self.update)
        self.ui.RB2_1.toggled.connect(self.update)
        self.ui.RB3_1.toggled.connect(self.update)
        self.ui.RB4_1.toggled.connect(self.update)
        self.ui.RB5_1.toggled.connect(self.update)
        self.ui.RB1_2.toggled.connect(self.update)
        self.ui.RB2_2.toggled.connect(self.update)
        self.ui.RB3_2.toggled.connect(self.update)
        self.ui.RB4_2.toggled.connect(self.update)
        self.ui.RB5_2.toggled.connect(self.update)

        self.ui.show()

    def update(self):
        D1 = self.ui.DB1_1.value()
        D2 = self.ui.DB2_1.value()
        D3 = self.ui.DB3_1.value()
        H1 = self.ui.DB2_2.value()
        H2 = self.ui.DB4_3.value()
        H3 = self.ui.DB5_3.value()
        L1 = self.ui.DB3_2.value()
        L2 = self.ui.DB4_2.value()
        L3 = self.ui.DB5_1.value()
        W1 = self.ui.DB4_1.value()
        W2 = self.ui.DB5_2.value()
        steel = 7.85
        aluminum = 2.6
        copper = 8.93
        if self.ui.RB1_1.isChecked or self.ui.RB2_1.isChecked or self.ui.RB3_1.isChecked or self.ui.RB4_1.isChecked or self.ui.RB5_1.isChecked:
            a = steel
        elif self.ui.RB1_2.isChecked or self.ui.RB2_2.isChecked or self.ui.RB3_2.isChecked or self.ui.RB4_2.isChecked or self.ui.RB5_2.isChecked:
            a = aluminum
        else:
            a = copper
        sphere = 3.14 * D1 ** 3 / 6000 * a
        cone = 3.14 * D2 ** 2 * H1 / 12000 * a
        cylinder = 3.14 * D3 ** 2 * L1 / 4000 * a
        pyramid = 3.14 * W1 * L2 * H2 / 3000 * a
        parallelepiped = 3.14 * W2 * L3 * H3 / 1000 * a
        self.ui.LCDnumber1.display(sphere)
        self.ui.LCDnumber2.display(cone)
        self.ui.LCDnumber3.display(cylinder)
        self.ui.LCDnumber4.display(pyramid)
        self.ui.LCDnumber5.display(parallelepiped)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec())