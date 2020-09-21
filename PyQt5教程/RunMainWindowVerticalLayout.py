import sys
import MainWindowHorizontaLayout

from PyQt5.QtWidgets import QApplication, QMainWindow

# 只有在运行这个脚本才能执行，别的调用不会执行
if __name__ == '__main__':

    # 创建一个应用
    app = QApplication(sys.argv)

    # 创建一个窗口
    mainWindow = QMainWindow()

    # 创建实例
    ui = MainWindowHorizontaLayout.Ui_MainWindow()

    # 向主窗口中添加控件
    ui.setupUi(mainWindow)

    # 显示窗口
    mainWindow.show()

    # 循环执行
    sys.exit(app.exec_())

