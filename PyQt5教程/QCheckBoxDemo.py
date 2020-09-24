'''
    复选框控件（QCheckBox）

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框控件演示')
        layout = QHBoxLayout()

        self.checkbox1 = QCheckBox('复选框控件1')
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda: self.checkboxState(self.checkbox1))
        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox('复选框控件2')
        self.checkbox2.stateChanged.connect(lambda: self.checkboxState(self.checkbox2))
        layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox('半选中')
        self.checkbox3.stateChanged.connect(lambda: self.checkboxState(self.checkbox3))
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkbox3)

        self.setLayout(layout)

    def checkboxState(self, cb):
        check1Status = self.checkbox1.text() + ', isChecked=' + str(self.checkbox1.isChecked()) + ', checkState=' + str(self.checkbox1.checkState()) + '\n'
        check2Status = self.checkbox2.text() + ', isChecked=' + str(self.checkbox2.isChecked()) + ', checkState=' + str(self.checkbox2.checkState()) + '\n'
        check3Status = self.checkbox3.text() + ', isChecked=' + str(self.checkbox3.isChecked()) + ', checkState=' + str(self.checkbox3.checkState()) + '\n'
        print(check1Status + check2Status + check3Status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()

    sys.exit(app.exec_())