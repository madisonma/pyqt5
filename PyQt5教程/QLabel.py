'''

    QLabel控件
    setAlignment():  设置文本的对齐方式
    setIndent():    设置文本缩进
    text():         获取文本内容
    setBuddy():     设置伙伴关系
    setText():      设置文本内容
    selectedText(): 返回所选择的字符
    setWordWrap():  设置是否允许换行
    
    QLabel常用的信号（事件）
    1 当鼠标滑过QLabel控件时触发： linkHovered
    2 当鼠标单击QLabel控件时触发：linkActivated

'''

import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QMainWindow, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def linkHovered(self):
        print('当鼠标滑过lable2标签时，触发事件')

    def linkClicked(self):
        print("当鼠标点击label4时，触发事件")

    def initUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('QLabel控件演示')
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=red>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter) #设置文字的对齐方式

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap('1.png'))

        label4.setOpenExternalLinks(False) #如果设置为True用浏览器打开网页，如果设置False调用槽函数
        label4.setText("<a href='http://www.baidu.com'>百度一下</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个链接")

        # 布局（垂直）
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)



        self.setLayout(vbox)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()

    sys.exit(app.exec_())


