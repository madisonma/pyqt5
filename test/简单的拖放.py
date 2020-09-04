#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    本例使用了QLineEdit 和 QPushButton 把一个文本编辑框拖到按钮上，更新按钮上的标签文字

    This is a simple drag and drop example

    author: madison
    date: 2020.9.3

"""
import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QApplication


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('/text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    # sys.exit(app.exec_())
    ex.show()
    app.exec_()