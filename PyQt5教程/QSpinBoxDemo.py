'''
    计数器控件（QSpinBox）
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSpinBox演示')
        self.resize(100, 50)

        layout = QVBoxLayout()
        self.label = QLabel('当前值:')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.sb = QSpinBox()
        self.sb.setValue(18)
        self.sb.setRange(1, 100)
        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(self.valueChange)

        self.setLayout(layout)

    def valueChange(self):
        self.label.setText('当前值：' +  str(self.sb.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QSpinBoxDemo()
    win.show()

    sys.exit(app.exec_())

