from PyQt5.QtWidgets import QWidget, QApplication
from design import Ui_Form as Design
from PyQt5 import QtCore
import csv
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QSpinBox
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        mass = []
        with open(QFileDialog.getOpenFileName()[0], encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                mass.append(row)
        self.tableWidget.setRowCount(len(mass))
        self.tableWidget.setColumnCount(3)
        self.counters = []
        self.mass = mass
        for i in range(len(mass)):
            for j in range(3):
                if j != 2:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(mass[i][j])))
                else:
                    self.counters.append(QSpinBox())
                    self.tableWidget.setCellWidget(i, j, self.counters[-1])
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(1)

    def updater(self):
        self.label_2.setText(str(sum([int(self.counters[i].value()) * int(self.mass[i][1])
                                      for i in range(len(self.counters))])) + ' руб.')


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())