import sys
from PyQt4 import QtCore, QtGui

class QDataViewer(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        # Layout Init.
        self.setGeometry(650, 300, 600, 600)
        self.setWindowTitle('Data Viewer')
        self.quitButton = QtGui.QPushButton('QUIT', self)
        self.uploadButton = QtGui.QPushButton('UPLOAD', self)
        hBoxLayout = QtGui.QHBoxLayout()
        hBoxLayout.addWidget(self.quitButton)
        hBoxLayout.addWidget(self.uploadButton)
        self.setLayout(hBoxLayout)
        # Signal Init.
        self.connect(self.quitButton,   QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.connect(self.uploadButton, QtCore.SIGNAL('clicked()'), self.open)

    def open (self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        print 'Path file :', filename

def main():
    app = QtGui.QApplication(sys.argv)
    mw = QDataViewer()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()