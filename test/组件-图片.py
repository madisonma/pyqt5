#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    QPixmap 是处理图片的组件，我们使用QPixmap在窗口里显示一张图片

    In this example, we display an images on the window

    author: madison
    date: 2020.9.3

"""
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("1.png") # 创建一个QPixmap对象，接收一个文件作为参数

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)  #  把QPixmap实例放到QLabel组件里

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
