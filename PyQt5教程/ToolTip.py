import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期二</b>')
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('设置控件提示消息')

        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮, Are you ok?')

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    # 创建一个应用
    app = QApplication(sys.argv)

    #创建一个窗口
    main = TooltipForm()
    # 显示窗口
    main.show()
    # 循环
    sys.exit(app.exec_())
