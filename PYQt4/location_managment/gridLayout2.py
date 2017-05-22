# -*- coding: utf-8 -*-

# analyzer.py

import sys
from PyQt4 import QtGui


class Analyzer(QtGui.QWidget):

    def __init__(self):
        super(Analyzer, self).__init__()

        self.initUI()

    def initUI(self):
        self.grid_layout = QtGui.QGridLayout()

        self.label1 = QtGui.QLabel("label1")
        self.grid_layout.addWidget(self.label1, 0, 0, 1, 3)

        self.line_edit1 = QtGui.QLineEdit()
        self.grid_layout.addWidget(self.line_edit1, 1, 0, 1, 3)

        self.label2 = QtGui.QLabel("label2")
        self.grid_layout.addWidget(self.label1, 2, 0, 1, 3)

        self.line_edit2 = QtGui.QLineEdit()
        self.grid_layout.addWidget(self.line_edit2, 3, 0, 1, 3)

        self.button1 = QtGui.QPushButton("button1")
        self.button2 = QtGui.QPushButton("button2")
        self.button3 = QtGui.QPushButton("button3")

        self.grid_layout.addWidget(self.button1, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.button2, 4, 1, 1, 1)
        self.grid_layout.addWidget(self.button3, 4, 2, 1, 1)

        self.setLayout(self.grid_layout)

app = QtGui.QApplication(sys.argv)
az = Analyzer()
az.show()
sys.exit(app.exec_())