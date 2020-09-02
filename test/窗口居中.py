#!/bin/python3
# -*- coding: utf-8 -*-

"""
This program centers a window on the screen

"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 得到了主窗口的大小

        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到中间点的位置

        qr.moveCenter(cp)  # 把自己的中心点放置到qr的中心点

        self.move(qr.topLeft())  # 把窗口的左上角的坐标设置为qr的矩形左上角的坐标，这样就把窗口居中了


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())