# 0 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1 创建一个应用程序对象
app = QApplication(sys.argv)

# 2 控件的操作

# 2.1 创建控件
windows = QWidget()

# 2.2 设置控件
windows.setWindowTitle("Qlabel的学习")
windows.resize(600, 600)

label=QLabel(windows)
label.setText("xxx")
label.move(200, 200)

# 2.3 展示控件
windows.show()

# 3 应用程序的执行
sys.exit(app.exec_())
