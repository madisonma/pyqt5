'''
    滑块控件（QSilder）
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(800, 800)

        layout = QVBoxLayout()
        self.label = QLabel('你好，PyQt5')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.silder = QSlider(Qt.Horizontal)
        # 设置最小值
        self.silder.setMinimum(12)
        # 设置最大值
        self.silder.setMaximum(48)
        # 设置步长
        self.silder.setSingleStep(3)

        # 设置当前值
        self.silder.setValue(18)

        # 设置刻度的位置，刻度在下方
        self.silder.setTickPosition(QSlider.TicksBelow)
        # 设置刻度的间隔
        self.silder.setTickInterval(6)

        layout.addWidget(self.silder)

        self.silder.valueChanged.connect(self.valueChange)

        self.setLayout(layout)

    def valueChange(self):
        print('当前值：%s' % self.silder.value())
        size = self.silder.value()
        self.label.setFont(QFont('Arial', size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()

    sys.exit(app.exec_())