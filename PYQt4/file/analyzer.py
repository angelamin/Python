#!/usr/bin/python
# -*- coding: utf-8 -*-

# analyzer.py

import sys
import string
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
        self.analyzerOutput = QtGui.QTextEdit()
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
        self.gridLayout.addWidget(self.analyzerOutput, 2, 3, 7, 4)

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
            with open(self.testFilename, 'w') as f:
                f.write(self.codeInput.toPlainText())

            self._key = ("auto", "break", "case", "char", "const", "continue", "default",

                    "do", "double", "else", "enum", "extern", "float", "for",

                    "goto", "if", "int", "long", "register", "return", "short",

                    "signed", "static", "sizeof", "struct", "switch", "typedef", "union",

                    "unsigned", "void", "volatile", "while")  # c语言的32个关键字

            self._abnormalChar = '@#$%^&*~'  # 标识符中可能出现的非法字符

            self._syn = ''  # 单词的种别码
            self._p = 0  # 下标
            self._value = ''  # 存放词法分析出的单词
            self._content = ''  # 程序内容
            self._mstate = '0'  # 字符串的状态
            self._cstate = '0'  # 字符的状态
            self._dstate = '0'  # 整数和浮点数的状态
            self._line = 1  # 代码的第几行
            self._mysymbol = []  # 符号表

            self.symbolTableFile = open(
                r'/Users/xiamin/Downloads/Python_study/Compilers_Experiment/Experiment_one/temp3/symbol_table.txt', 'w')
            self.tokenFile = open(
                r'/Users/xiamin/Downloads/Python_study/Compilers_Experiment/Experiment_one/temp3/token.txt', 'w')
            self.mistakesFile = open(
                r'/Users/xiamin/Downloads/Python_study/Compilers_Experiment/Experiment_one/temp3/mistakes.txt', 'w')
            self.getMyProm()
            self.outOfComment()

            while self._p != len(self._content):
                self.analysis()
                if self._syn == '@-1':
                    self._line += 1  # 记录程序的行数
                elif self._syn == '@-2':
                    self.mistakesFile.write('String ' + self._value + ' Not closed! Error in line ' + str(self._line) + '\n')
                elif self._syn == '@-3':
                    self.mistakesFile.write('Number ' + self._value + ' wrong，can not begin with number 0! Error in line ' + str(self._line) + '\n')
                elif self._syn == '@-4':
                    self.mistakesFile.write('Char ' + self._value + ' Not closed! Error in line ' + str(self._line) + '\n')
                elif self._syn == '@-5':
                    self.mistakesFile.write('Number ' + self._value + ' Illegal! Error in line ' + str(self._line) + '\n')
                elif self._syn == '@-6':
                    self.mistakesFile.write('Identifier' + self._value + ' can not include illegal char!Error in line ' + str(self._line) + '\n')
                elif self._syn == '@-7':
                    self.mistakesFile.write('Number ' + self._value + ' Illegal!,inclede char! Error in line ' + str(self._line) + '\n')
                else:  # 若程序中无词法错误的情况
                    if self._syn == 'IDN':
                        self.tokenFile.write(self._value + '\t\t\t< ' + str(self._syn) + ' , ' + self._value + ' >\t' + '\n')
                    elif self._syn == 'DIGIT':
                        self.tokenFile.write(self._value + '\t\t\t< ' + str(self._syn) + ' , ' + self._value + ' >\t' + '\n')
                    elif self._syn == 'FRACTION':
                        self.tokenFile.write(self._value + '\t\t\t< ' + str(self._syn) + ' , ' + self._value + ' >\t' + '\n')
                    else:
                        self.tokenFile.write(self._value + '\t\t\t< ' + str(self._syn) + ' , ' + '_' + ' >\t' + '\n')

            self.tokenFile.close()
            self.symbolTableFile.write('入口地址\t变量名\n')
            i = 0
            for symbolItem in self._mysymbol:
                self.symbolTableFile.write(str(i) + '\t\t\t' + symbolItem + '\n')
                i += 1
            self.symbolTableFile.close()

            self.outputFileContent = open(r'/Users/xiamin/Downloads/Python_study/Compilers_Experiment/Experiment_one/temp3/token.txt', 'r').read()
            self.analyzerOutput.setText(self.outputFileContent)

            self.errorsOutput = open(r'/Users/xiamin/Downloads/Python_study/Compilers_Experiment/Experiment_one/temp3/mistakes.txt', 'r').read()
            self.errors.setText(self.errorsOutput)

    def outOfComment(self):
        '''去除代码中的注释'''
        state = '0'
        index = -1
        _cline = 1
        ####--------------------------------将注释内容写到单独一个文件夹
        self.noteFile = open(r'/Users/xiamin/Downloads/Python_study/Compilers_Experiment/Experiment_one/temp3/note.txt','w')
        DFACommentFile = open(self.commentFilename, 'r')
        line = DFACommentFile.next()
        line1 = DFACommentFile.next()
        line2 = DFACommentFile.next()
        line3 = DFACommentFile.next()
        for c in self._content:
            if c == '\n':
                _cline += 1
            index = index + 1

            if state == line[0]:
                if c == line[1]:
                    state = line[2]
                    startIndex = index

            elif state == line1[0]:
                if c == line1[1]:
                    state = line1[2]
                    _fline = _cline

                else:
                    state = line1[3]

            elif state == line2[0]:
                if c == line2[1]:
                        state = line2[2]
                else:
                    pass


            elif state == line3[0]:
                if c == line3[1]:
                    endIndex = index + 1
                    comment = self._content[startIndex:endIndex]
                    self.noteFile.write(comment + '\n')  # ----------------------------写入注释
                    self._content = self._content.replace(comment, '')  # 将注释替换为空，并且将下标移动
                    index = startIndex - 1
                    state = line[0]


                elif c == line3[2]:
                    _fline = _cline
                    pass
                else:
                    state = line3[3]
        ##--------------------------------注释内容有错，不闭合时，形成错误信息
        if state == '2' or state == '3':
            self.mistakesFile.write('note Not closed！Error in line ' + str(_fline) + '\n')  # ----------------------------写入注释
            comment = self._content[startIndex:len(self._content)]
            self.noteFile.write(comment + '\n')
            self._content = self._content.replace(comment, '')

    def getMyProm(self):
        '''从文件中获取代码片段'''
        myPro = open(self.testFilename, 'r')

        for line in myPro:
            if line != '\n':
                self._content = "%s%s" % (self._content, line.lstrip())  # 效率更高的字符串拼接方法
            else:
                self._content = "%s%s" % (self._content, line)
        myPro.close()

    def analysis(self):
        '''分析目标代码，生成token'''

        self._value = ''
        ch = self._content[self._p]
        self._p += 1
        while ch == ' ':
            ch = self._content[self._p]
            self._p += 1
        if ch in string.letters or ch == '_':  ###############letter(letter|digit)*
            while ch in string.letters or ch in string.digits or ch == '_' or ch in self._abnormalChar:
                self._value += ch
                ch = self._content[self._p]
                self._p += 1
            self._p -= 1

            for abnormal in self._abnormalChar:
                if abnormal in self._value:
                    self._syn = '@-6'  # 错误代码，标识符中含有非法字符
                    break
                else:
                    self._syn = 'IDN'  # IDN

            for s in self._key:
                if cmp(s, self._value) == 0:
                    self._syn = self._value.upper()  #############关键字
                    break
            if self._syn == 'IDN':
                self.inSymbolTable()

        elif ch == '\"':  #############字符串
            while ch in string.letters or ch in '\"% ':
                self._value += ch

                DFAStringFile = open(self.stringFilename,'r')
                stringLine = DFAStringFile.next()
                stringLine1 = DFAStringFile.next()
                stringLine2 = DFAStringFile.next()
                if self._mstate == stringLine[0]:
                    if ch == stringLine[1]:
                        self._mstate = stringLine[2]
                elif self._mstate == stringLine1[0]:
                    if ch == stringLine1[1]:
                        self._mstate = stringLine1[2]

                ch = self._content[self._p]
                self._p += 1

            if self._mstate == stringLine1[0]:
                self._syn = '@-2'  # 错误代码，字符串不封闭
                self._mstate = stringLine[0]

            elif self._mstate == stringLine2[0]:
                self._mstate = stringLine[0]
                self._syn = 'STRING'

            self._p -= 1

        elif ch in string.digits:
            while ch in string.digits or ch == '.' or ch in string.letters:
                self._value += ch
                DFANumFile = open(self.numFilename, 'r')
                numLine = DFANumFile.next()
                numLine1 = DFANumFile.next()
                numLine2 = DFANumFile.next()
                numLine3 = DFANumFile.next()
                if self._dstate == numLine[0]:
                    if ch == numLine[1]:
                        self._dstate = numLine[2]
                    else:
                        self._dstate = numLine[3]

                elif self._dstate == numLine1[0]:
                    if ch == numLine1[1]:
                        self._dstate = numLine1[2]
                    else:
                        self._dstate = numLine1[3]

                elif self._dstate == numLine2[0]:
                    if ch == numLine2[1]:
                        self._dstate = numLine2[2]

                ch = self._content[self._p]
                self._p += 1

            for char in string.letters:
                if char in self._value:
                    self._syn = '@-7'  # 错误代码，数字和字母混合，如12AB56等
                    self._dstate = numLine[0]

            if self._syn != '@-7':
                if self._dstate == numLine3[0]:
                    self._syn = '@-3'  # 错误代码，数字以0开头
                    self._dstate = numLine[0]
                else:
                    self._dstate = numLine[0]
                    if '.' not in self._value:
                        self._syn = 'DIGIT'  ##################digit digit*
                    else:
                        if self._value.count('.') == 1:
                            self._syn = 'FRACTION'  ################## 浮点数
                        else:
                            self._syn = '@-5'  # 错误代码，浮点数中包含多个点，如1.2.3
            self._p -= 1


        elif ch == '\'':  ################## 字符
            while ch in string.letters or ch in '@#$%&*\\\'\"':
                self._value += ch
                DFACharFile = open(self.charFilename, 'r')
                charLine = DFACharFile.next()
                charLine1 = DFACharFile.next()
                charLine2 = DFACharFile.next()
                charLine3 = DFACharFile.next()
                charLine4 = DFACharFile.next()
                if self._cstate == charLine[0]:
                    if ch == charLine[1]:
                        self._cstate = charLine[2]

                elif self._cstate == charLine1[0]:
                    if ch == charLine1[1]:
                        self._cstate = charLine1[2]
                    elif ch in string.letters or ch in '@#$%&*':
                        self._cstate = charLine1[3]

                elif self._cstate == charLine2[0]:
                    if ch in 'nt':
                        self._cstate = charLine2[1]

                elif self._cstate == charLine3[0]:
                    if ch == charLine3[1]:
                        self._cstate = charLine3[2]
                ch = self._content[self._p]
                self._p += 1

            self._p -= 1
            if self._cstate == charLine4[0]:
                self._syn = 'CHARACTER'
                self._cstate = charLine[0]
            else:
                self._syn = '@-4'  # 错误代码，字符不封闭
                self._cstate = charLine[0]

        elif ch == '<':
            self._value = ch
            ch = self._content[self._p]

            if ch == '=':  ###########  '<='
                self._value += ch
                self._p += 1
                self._syn = 'LE'
            else:  ###########  '<'
                self._syn = 'L'

        elif ch == '>':
            self._value = ch
            ch = self._content[self._p]

            if ch == '=':  ########### '>='
                self._value += ch
                self._p += 1
                self._syn = 'ME'
            else:  ########## '>'
                self._syn = 'M'

        elif ch == '!':
            self._value = ch
            ch = self._content[self._p]

            if ch == '=':  ########## '!='
                self._value += ch
                self._p += 1
                self._syn = 'NE'
            else:  ########## '!'
                self._syn = 'N'


        elif ch == '+':
            self._value = ch
            ch = self._content[self._p]

            if ch == '+':  ############ '++'
                self._value += ch
                self._p += 1
                self._syn = 'PP'
            else:  ############ '+'
                self._syn = 'P'

        elif ch == '-':
            self._value = ch
            ch = self._content[self._p]

            if ch == '-':  ########### '--'
                self._value += ch
                self._p += 1
                self._syn = 'DD'
            else:  ########### '-'
                self._syn = 'D'

        elif ch == '=':
            self._value = ch
            ch = self._content[self._p]

            if ch == '=':  ########### '=='
                self._value += ch
                self._p += 1
                self._syn = 'EE'
            else:  ########### '='
                self._syn = 'E'

        elif ch == '&':
            self._value = ch
            ch = self._content[self._p]

            if ch == '&':  ########### '&&'
                self._value += ch
                self._p += 1
                self._syn = 'UN'
            else:  ########### '&'
                self._syn = 'AND'

        elif ch == '|':
            self._value = ch
            ch = self._content[self._p]

            if ch == '|':  ########## '||'
                self._value += ch
                self._p += 1
                self._syn = 'OO'
            else:  ########## '|'
                self._syn = 'O'

        elif ch == '*':  ########## '*'
            self._value = ch
            self._syn = 'MT'

        elif ch == '/':  ########## '/'
            self._value = ch
            self._syn = 'ST'

        elif ch == ';':  ########## ';'
            self._value = ch
            self._syn = 'SC'

        elif ch == '(':  ##########  '('
            self._value = ch
            self._syn = 'SLP'

        elif ch == ')':  ########### ')'
            self._value = ch
            self._syn = 'SRP'

        elif ch == '{':  ########### '{'
            self._value = ch
            self._syn = 'LP'

        elif ch == '}':  ########### '}'
            self._value = ch
            self._syn = 'RP'

        elif ch == '[':  ########### '['
            self._value = ch
            self._syn = 'ZLP'

        elif ch == ']':  ########### ']'
            self._value = ch
            self._syn = 'ZRP'

        elif ch == ',':  ########## ','
            self._value = ch
            self._syn = 'CM'
        elif ch == '\n':
            self._syn = '@-1'

    def inSymbolTable(self):
        '''将关键字和标识符存进符号表'''
        if self._value not in self._mysymbol:
            self._mysymbol.append(self._value)

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