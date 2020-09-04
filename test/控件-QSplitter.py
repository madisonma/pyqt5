#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Qsplitter组件能让用户通过拖拽分割线的方式改变子窗口的大小组件
    本例中我们展示用两个分隔线隔开的三个QFrame组件

    This example shows how to use QSplitter widget

    author: madison
    date: 2020.9.3

"""
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        spilitter1 = QSplitter(Qt.Horizontal)
        spilitter1.addWidget(topleft)
        spilitter1.addWidget(topright)

        spilitter2 = QSplitter(Qt.Vertical)
        spilitter2.addWidget(spilitter1)
        spilitter2.addWidget(bottom)

        hbox.addWidget(spilitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

