from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        # 调用父类的init方法
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)

        self.setup_ui()

    # 设置子控件
    def setup_ui(self):
        # self.QObject继承结构测试()
        self.QObject对象名称和属性的操作()


    def QObject继承结构测试(self):
        # QObject.__subclasses__()
        mros = QObject.mro()
        for mro in mros:
            print(mro)


    def QObject对象名称和属性的操作(self):
        # 测试API
        # obj = QObject()
        # obj.setObjectName("notice")
        # print(obj.objectName())
        #
        # obj.setProperty("notice_level", "error")
        # obj.setProperty("notice_level2", "warning")
        #
        # print(obj.property("notice_level"))
        #
        # print(obj.dynamicPropertyNames())

        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setText("社会我顺哥")
        label.move(50, 50)
        label.setObjectName("notice")
        label.setProperty("notice_level", "warnning")

        label2 = QLabel(self)
        label2.setText("人狠话不多")
        label2.setObjectName("notice")
        label2.move(100, 100)
        label2.setProperty("notice_level", "error")

        label3 = QLabel(self)
        label3.setText("xxx")
        label3.move(150, 150)

    def QObject对象的父子关系操作(self):
        obj1 = QObject()
        obj2 = QObject()
        obj1.setParent(obj2)
        obj1.parent()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())