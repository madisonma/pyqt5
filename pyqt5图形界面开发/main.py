from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.QtCore import QFile
from PyQt5 import uic
from logic import logic
from Trace import Ui_MainWindow
from PyQt5.Qt import QIcon
import config
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):

        #从文件中加载UI定义
        #qfile = QFile("traceData-single.ui")
        #qfile.open(QFile.ReadOnly)
        #qfile.close()
        #self.ui = uic.loadUi("Trace.ui")
        #从UI定义中动态创建一个相应的窗口对象
        #注意：里面的空间对象也成为窗口对象属性了
        #比如 self.ui.button, self.ui.textEdit
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('logo.png'))
        self.terminalIdValue.setText(config.get("trace", "terminal_id"))
        self.terminalIdValue.setStyleSheet('''#terminalIdValue{color:blue;}''')
        self.lineEdit.setFocus()
        # self.ui.btn.clicked.connect(self.handleCalc)

        self.btn.clicked.connect(lambda: logic.btn_click(self))
        self.lineEdit.returnPressed.connect(lambda: logic.enter(self))



# 创建应用
app = QApplication(sys.argv)
# 创建一个窗口
window = MainWindow()
# 显示窗口
window.show()
#win.ui.show()
# 循环输出
sys.exit(app.exec_())