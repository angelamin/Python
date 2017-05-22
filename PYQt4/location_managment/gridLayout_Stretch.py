#!/usr/bin/python
# -*- coding: utf-8 -*-

# analyzer.py

import sys
from PyQt4 import QtGui


class Analyzer(QtGui.QWidget):

    def __init__(self):
        super(Analyzer, self).__init__()

        self.initUI()

        self.center()

    # 设置窗口的布局
    def initUI(self):
        label1 = QtGui.QLabel('Please input C code:')
        label2 = QtGui.QLabel('The results:')
        label3 = QtGui.QLabel('errors:')

        codeInput = QtGui.QTextEdit()
        analazerOutput = QtGui.QTextEdit()
        errors = QtGui.QTextEdit()

        okButton = QtGui.QPushButton("Begin Analyzing")

        okButton.resize(100, 20)

        self.gridLayout = QtGui.QGridLayout()

        self.gridLayout.addWidget(label1, 0, 0)
        self.gridLayout.addWidget(label2, 0, 1)
        self.gridLayout.addWidget(label3, 2, 1)

        self.gridLayout.addWidget(codeInput, 1, 0)
        self.gridLayout.addWidget(analazerOutput, 1, 1)
        self.gridLayout.addWidget(errors, 3, 1, 3, 2)

        self.gridLayout.addWidget(okButton, 2, 0)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 9)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 3)

        self.setLayout(self.gridLayout)

        self.setWindowTitle('Lexical Analyzer by xiamin')
        self.resize(1200, 700)

    # 关闭窗口时确认信息
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes,
                                               QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

            # 居中函数

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()

        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

app = QtGui.QApplication(sys.argv)
az = Analyzer()
az.show()
sys.exit(app.exec_())