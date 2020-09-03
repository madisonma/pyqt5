#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    In this example, we show how to
    emit a custom signal

    author: mddison
    date: 2020.9.3

"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

# Communicate 类创建了一个pyqtSignal()属性的信号


class Communicate(QObject):

    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)   # closeApp信号QMainWindow的close()方法绑定

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):   # 点击窗口的时候，发送closeApp信号，程序终止

        self.c.closeApp.emit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())