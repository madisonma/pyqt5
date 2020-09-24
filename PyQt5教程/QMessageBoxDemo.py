'''

    消息对话框： QMessageBox
    1 关于对话框
    2 错误对话框
    3 警告对话框
    4 疑问对话框
    5 消息对话框

    有2点差异
        1 显示的对话框图标可能不同
        2 显示的按钮是不一样的
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox案例')
        self.resize(300, 400)




        # 关于对话框
        self.btn1 = QPushButton()
        self.btn1.setText('显示关于对话框')
        self.btn1.clicked.connect(self.showDialog)

        # 消息对话框
        self.btn2 = QPushButton()
        self.btn2.setText('显示消息对话框')
        self.btn2.clicked.connect(self.showDialog)

        # 警告对话框
        self.btn3 = QPushButton()
        self.btn3.setText('显示警告对话框')
        self.btn3.clicked.connect(self.showDialog)

        # 错误对话框
        self.btn4 = QPushButton()
        self.btn4.setText('显示错误对话框')
        self.btn4.clicked.connect(self.showDialog)

        # 提示对话框
        self.btn5= QPushButton()
        self.btn5.setText('显示提示对话框')
        self.btn5.clicked.connect(self.showDialog)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)

        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        if text == '显示消息对话框':
            reply = QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes| QMessageBox.No, QMessageBox.Yes)
            print(reply)
        if text == '显示警告对话框':
            reply = QMessageBox.warning(self, '消息', '这是一个警告对话框', QMessageBox.Yes| QMessageBox.No, QMessageBox.Yes)
        if text == '显示错误对话框':
            reply = QMessageBox.critical(self, '消息', '这是一个错误对话框', QMessageBox.Yes| QMessageBox.No, QMessageBox.Yes)
        if text == '显示提示对话框':
            reply = QMessageBox.question(self, '消息', '这是一个提问对话框', QMessageBox.Yes| QMessageBox.No, QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMessageBoxDemo()
    win.show()

    sys.exit(app.exec_())