# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore


class Compiller(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)

        self.setGeometry(400, 400, 1200, 650)
        self.setWindowTitle('Lexical Analyzer by xiamin')
        self.statusBar().showMessage('Ready')

        self.center()

        self.initUI()

        # self.mymenubar()
        # self.mytoolbar()
        # self.mytext()
        # self.mylabel()
        # self.mybutton()

    # 窗体的整个布局
    def initUI(self):
        # 添加工具栏
        # exit = QtGui.QAction(QtGui.QIcon('../icons/exit.jpeg'), 'Exit', self)
        # exit.setShortcut('Ctrl+Q')
        # exit.setStatusTip('Exit Lexical Analyzer....')
        # self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        #
        # self.statusBar()
        #
        # # self.main_layout = QtGui.QVBoxLaout()
        #
        # self.toolbar = self.addToolBar('Exit')
        # self.toolbar.addAction(exit)

        # codeinput = QtGui.QLabel('输入C语言代码：')
        # codeinputEdit = QtGui.QLineEdit()
        #
        #
        # vbox = QtGui.QVBoxLayout()
        #
        # vbox.addWidget(codeinput)
        # vbox.addStretch(1)
        #
        # self.setLayout(vbox)

        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        #self.toolbar.setLayout(vbox)



    # 关闭窗口时确认信息
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 居中函数
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()

        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    # 添加菜单
    def mymenubar(self):
        exit = QtGui.QAction(QtGui.QIcon('../icons/exit.jpeg'),'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit Lexical Analyzer....')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menbar = self.menuBar()
        file = menbar.addMenu('&File')
        file.addAction(exit)

    # 添加工具栏
    def mytoolbar(self):
        self.exit = QtGui.QAction(QtGui.QIcon('../icons/exit.jpeg'), 'Exit',self)
        self.exit.setShortcut('Ctrl+Q')
        self.exit.setStatusTip('Exit Lexical Analyzer....')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit)

    # 添加文本输入框
    def mytext(self):
        textEdit = QtGui.QTextEdit()
        textEdit.resize(100, 100)
        self.setCentralWidget(textEdit)

    # 添加Label
    def mylabel(self):
        label = QtGui.QLabel('Lexical Analyzer',self)
        label.move(30, 50)

    # 添加按钮
    def mybutton(self):
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        # 框布局
        hbox=QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


app = QtGui.QApplication(sys.argv)
ec = Compiller()
ec.show()
sys.exit(app.exec_())
