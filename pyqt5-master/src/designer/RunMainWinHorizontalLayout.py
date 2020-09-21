import sys
import MainWinHorizontalLayout
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':

    # 创建一个应用
    app = QApplication(sys.argv)
    # 创建一个主窗口
    mainWindow = QMainWindow()
    # 创建实例
    ui = MainWinHorizontalLayout.Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainWindow)
    # 显示窗口
    mainWindow.show()
    # 主循环
    sys.exit(app.exec_())