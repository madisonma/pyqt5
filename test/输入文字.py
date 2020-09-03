#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
   In this example, we receive data from
   a QInputDialog dialog

    author: mddison
    date: 2020.9.3

"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 20)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        # 这是显示一个输入框的代码。第一个参数是输入框的标题，第二个参数是输入框的占位符，对话框返回输入内容和一个布尔值如果点击的是OK按钮，布尔值就返回True

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())