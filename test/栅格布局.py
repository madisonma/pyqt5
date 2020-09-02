#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    In this example, we create a skeleton
    of a calculator using a QGridLayOut

"""

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建栅格化的按钮
        grid = QGridLayout()
        self.setLayout(grid)

        names = [
            'Cls', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        # 创建按钮位置列表
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue

            # 创建按钮，并使用addWidget()方法把按钮放到布局里面
            button = QPushButton(name)
            grid.addWidget(button, *position)

            self.move(300, 150)
            self.setWindowTitle('Calculator')
            self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
