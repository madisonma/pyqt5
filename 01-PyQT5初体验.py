# 0 导入需要的包和模块
from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)

# 2.1 创建控件
windows = QWidget()

# 2.2 设置控件
windows.setWindowTitle("Qlabel的学习")
# windows.resize(200, 200)

label=QLabel(windows)
label.setText("这是一个文本！")
label.adjustSize()
label.setGeometry(QRect(328, 240, 329, 27*4));
label.setWordWrap(True)
# label.move(50, 50)

# 2.3 展示控件
windows.show()

# 3 应用程序的执行
sys.exit(app.exec_())
