'''
    下拉列表控件(QComboBox)
    如何添加
    如何获取

'''

import sys
from PyQt5.QtWidgets import *


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300, 100)
        # 垂直布局
        layout = QVBoxLayout()
        self.label = QLabel('请选择编程语言')

        # 创建一个下拉框
        self.cb = QComboBox()
        self.cb.addItem('C++')
        self.cb.addItem('VB')
        self.cb.addItem('Python')
        self.cb.addItems(['Java', 'C#', 'Ruby'])

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('current index', i, 'selection changed', self.cb.currentIndex())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()

    sys.exit(app.exec_())
