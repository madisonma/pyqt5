import layoyt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    v_compare = QVersionNumber(5, 6, 0)
    v_current, _ = QVersionNumber.fromString(QT_VERSION_STR)  # 获取当前Qt版本
    if QVersionNumber.compare(v_current, v_compare) <= 0:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
        app = QApplication(sys.argv)  #
        print('111')
    else:
        # 创建应用
        app = QApplication(sys.argv)
        font=QFont("宋体")
        font.setPixelSize(font.pointSize() * 90/52)
        app.setFont(font)
    # 创建一个主窗口
    mainWindow = QMainWindow()
    # 实例化
    ui = layoyt.Ui_MainWindow()

    # 向主窗口添加控件
    ui.setupUi(mainWindow)

    # 显示窗口
    mainWindow.show()

    # 主循环
    sys.exit(app.exec_())