import sys
from PyQt5.Qt import *
from Menu import Window

# 创建一个应用对象
app = QApplication(sys.argv)

# 创建控件
window = Window()


# 展示控件
window.show()

# 执行应用程序
sys.exit(app.exec_())

