#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    In this example, we requirement an event handler
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        # 替换了事件处理函数KeyPressEvent() 此时如果按下ESC键程序就会退出
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
