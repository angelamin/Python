#!/usr/bin/python
# -*- coding: utf-8 -*-

# analyzer.py

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot


class Analyzer(QtGui.QWidget):

    def __init__(self):
        super(Analyzer, self).__init__()

        self.initUI()

        self.center()

    # 设置窗口的布局
    def initUI(self):
        self.charFilename = ''
        self.commentFilename = ''
        self.numFilename = ''
        self.stringFilename = ''
        self.testFilename = ''


        DFACharButton = QtGui.QPushButton("import Char DFA")
        DFACommentButton = QtGui.QPushButton("import Comment DFA")
        DFANumButton = QtGui.QPushButton("import Number DFA")
        DFAStringButton = QtGui.QPushButton("import String DFA")
        testButton = QtGui.QPushButton("import Test File")


        label1 = QtGui.QLabel('Please input C code:')
        label2 = QtGui.QLabel('The results:')
        self.label3 = QtGui.QLabel('errors:')
        self.inputFiles = QtGui.QLabel('The DFA you imported:')

        self.codeInput = QtGui.QTextEdit()
        analazerOutput = QtGui.QTextEdit()
        self.errors = QtGui.QTextEdit()

        self.okButton = QtGui.QPushButton("Begin Analyzing")

        self.okButton.resize(100, 20)

        self.gridLayout = QtGui.QGridLayout()

        self.gridLayout.addWidget(DFACharButton, 0, 0, 1, 1)
        self.gridLayout.addWidget(DFAStringButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(DFANumButton, 0, 2, 1, 1)
        self.gridLayout.addWidget(DFACommentButton, 0, 3, 1, 1)
        self.gridLayout.addWidget(DFACommentButton, 0, 4, 1, 1)
        self.gridLayout.addWidget(testButton, 0, 5, 1, 1)

        self.gridLayout.addWidget(label1, 1, 1, 1, 1)
        self.gridLayout.addWidget(label2, 1, 4, 1, 1)

        self.gridLayout.addWidget(self.codeInput, 2, 0, 7, 3)
        self.gridLayout.addWidget(analazerOutput, 2, 3, 7, 4)

        self.gridLayout.addWidget(self.okButton, 9, 1, 1, 1)
        self.gridLayout.addWidget(self.label3, 9, 4, 1, 1)

        self.gridLayout.addWidget(self.inputFiles, 10, 0, 2, 3)
        self.gridLayout.addWidget(self.errors, 10, 3, 2, 4)


        self.setLayout(self.gridLayout)

        self.setWindowTitle('Lexical Analyzer by xiamin')
        self.resize(1200, 700)

        # 上传文件
        self.connect(DFACharButton, QtCore.SIGNAL('clicked()'), self.openchar)
        self.connect(DFACommentButton, QtCore.SIGNAL('clicked()'), self.opencomment)
        self.connect(DFANumButton, QtCore.SIGNAL('clicked()'), self.opennum)
        self.connect(DFAStringButton, QtCore.SIGNAL('clicked()'), self.openstring)
        self.connect(testButton, QtCore.SIGNAL('clicked()'), self.opentest)

        # 点击Begin Analyzing触发事件
        self.okButton.clicked.connect(self.compiller)

    # 点击Begin Analyzing触发的事件响应
    def compiller(self):
        if self.codeInput.toPlainText() == '':
            self.errors.setText('<h1>Error!</h1>'+'<h3>Please input C code to analyze!!!</h3>')
        elif self.testFilename == '':
            self.errors.setText('<h1>Error!</h1>'+'<h3>Please import a file to analyze!!!</h3>')
        elif self.charFilename == '' or self.commentFilename == '' or self.numFilename == '' or self.stringFilename == '':
            self.errors.setText('<h1>Error!</h1>'+'<h3>Please import all the DFA files!!!</h3>')
        else:
            self.errors.setText('')
            with open(self.testFilename, 'a') as f:
                f.write(self.codeInput.toPlainText())


    # 上传文件的实现
    def openchar(self):
        self.charFilename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.inputFiles.setText('Char DFA: ' + self.charFilename + '\n' + 'Comment DFA: ' + self.commentFilename + '\n' +
                                'Num DFA: ' + self.numFilename + '\n' + 'String DFA: ' + self.stringFilename + '\n'
                                + 'Test File: ' + self.testFilename + '\n')

    def opencomment(self):
        self.commentFilename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.inputFiles.setText(
            'Char DFA: ' + self.charFilename + '\n' + 'Comment DFA: ' + self.commentFilename + '\n' +
            'Num DFA: ' + self.numFilename + '\n' + 'String DFA: ' + self.stringFilename + '\n'
            + 'Test File: ' + self.testFilename + '\n')

    def opennum(self):
        self.numFilename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.inputFiles.setText(
                'Char DFA: ' + self.charFilename + '\n' + 'Comment DFA: ' + self.commentFilename + '\n' +
                'Num DFA: ' + self.numFilename + '\n' + 'String DFA: ' + self.stringFilename + '\n'
                + 'Test File: ' + self.testFilename + '\n')

    def openstring(self):
         self.stringFilename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
         self.inputFiles.setText(
                'Char DFA: ' + self.charFilename + '\n' + 'Comment DFA: ' + self.commentFilename + '\n' +
                'Num DFA: ' + self.numFilename + '\n' + 'String DFA: ' + self.stringFilename + '\n'
                + 'Test File: ' + self.testFilename + '\n')

    def opentest(self):
        self.testFilename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.inputFiles.setText(
                 'Char DFA: ' + self.charFilename + '\n' + 'Comment DFA: ' + self.commentFilename + '\n' +
                 'Num DFA: ' + self.numFilename + '\n' + 'String DFA: ' + self.stringFilename + '\n'
                 + 'Test File: ' + self.testFilename + '\n')
        # 将test文件放在QtextEdit
        self.testFile = open(self.testFilename, 'r').read()
        self.codeInput.setText(self.testFile)
        print 'sucess'

    # # 关闭窗口时确认信息
    # def closeEvent(self, event):
    #     reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes,
    #                                            QtGui.QMessageBox.No)
    #
    #     if reply == QtGui.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

     # 居中函数
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()

        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

def main():
    app = QtGui.QApplication(sys.argv)
    az = Analyzer()
    az.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()