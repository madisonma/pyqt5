from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        # 调用父类的init方法
        super().__init__()
        self.setWindowTitle("信号与槽的学习")
        self.resize(500, 500)

        self.setup_ui()

    # 设置子控件
    def setup_ui(self):
        self.QObject信号的操作()

    def QObject信号的操作(self):
        self.obj = QObject()
        # obj.destroyed()
        # obj.objectNameChanged()

        # def destroy_cao(obj):
        #     print("对象被释放了！", obj)
        #
        # self.obj.destroyed.connect(destroy_cao)
        #
        # del self.obj
        # def obj_name_cao(name):
        #     print("对象名称发生了改变",name)
        # self.obj.objectNameChanged.connect(obj_name_cao)
        #
        # self.obj.setObjectName("xxx")
        # # self.obj.objectNameChanged.disconnect()
        # self.obj.blockSignals(True)
        # self.obj.setObjectName("ooo")
        #
        # # self.obj.objectNameChanged.connect(obj_name_cao)
        # self.obj.blockSignals(False)
        # self.obj.setObjectName("xxxooo")

        btn = QPushButton(self)
        btn.setText("点我")

        def cao():
            print ("点我干啥！")

        def cao2(title):
            # print("窗口标题变化了！",title)
            window.windowTitleChanged.disconnect()
            window.setWindowTitle("聊客-"+title)

        window.windowTitleChanged.connect(cao2)

        window.setWindowTitle("Hello,madison")

        # btn.clicked.connect(cao)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())