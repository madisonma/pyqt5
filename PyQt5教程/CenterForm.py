#QDeskWidget

import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow


class CenterForm(QMainWindow):

    def __init__(self):
        super(CenterForm, self).__init__()

        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口尺寸
        self.resize(400, 300)

    def center(self):
        # 获取屏幕的坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)




if __name__ == '__main__':
    # 创建一个应用
    app = QApplication(sys.argv)
    # 实例化一个窗口
    mainWindow = CenterForm()
    # 显示窗口
    mainWindow.show()
    # 循环
    sys.exit(app.exec_())
