from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon

class Stats:

    def __init__(self):

        #从文件中加载UI定义
        qfile = QFile("salaryCount.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        #从UI定义中动态创建一个相应的窗口对象
        #注意：里面的空间对象也成为窗口对象属性了
        #比如 self.ui.button, self.ui.textEdit

        self.ui = QUiLoader().load(qfile)
        self.ui.btn.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.TextEdit.toPlainText()

        # 薪资20000以上和以下的人员名单
        salary_above_20k = ''
        salary_below_20k = ''

        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.ui,
                      '统计结果',
                      f'''薪资20000以上的有:\n{salary_above_20k}
                      \n薪资20000以下的有：\n{salary_below_20k}'''
                      )

app = QApplication([])
app.setWindowIcon(QIcon('1.png'))
stats = Stats()
stats.ui.show()
app.exec_()