#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    QLineEdit 组件提供了编辑文本的功能，自带了撤销，重做，剪贴，拖拽等功能

    This example shows text which is entered in a QLineEdit in a QLabel widget

    author: madison
    date: 2020.9.3

"""
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
