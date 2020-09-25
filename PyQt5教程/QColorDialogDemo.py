'''
    颜色对话框（QColorDialog）
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Font Dialog例子')

        # 垂直布局
        layout = QVBoxLayout()
        self.colorButton = QPushButton('请选择颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorButton2 = QPushButton('请选择背景颜色')
        self.colorButton2.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton2)

        self.colorLabel = QLabel('hello,测试颜色')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)


    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.colorLabel.setPalette(p)

    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QColorDialogDemo()
    win.show()

    sys.exit(app.exec_())
