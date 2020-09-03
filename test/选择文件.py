#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    本例中有一个菜单栏，一个置中的文本框编辑，一个状态栏。点击菜单栏选项会弹出一个QtGui.QFileDialog对话框
    在这个对话框里，你能选择文件，然后文件的内容会显示在文本编辑里

    In this example, we select a file with a
    QFileDialog and display its contents
    in a QTextEdit

    author: madison
    date: 2020.9.3

"""
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('1.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')
        # 读取选中的文件，并显示在文本编辑框里（但是打开HTML文件时，是渲染后的结果）
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

