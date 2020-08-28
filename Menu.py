from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        # 调用父类的init方法
        super().__init__()
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)

        self.setup_ui()

    # 设置子控件
    def setup_ui(self):
        label = QLabel(self)
        label.setText("Hello,World!")
        label.move(200, 200)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())