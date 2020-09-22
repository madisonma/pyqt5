import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget

def onClick_Button():
    # print("onclick")
    print("=====================================1==============================")
    print("widget.x() = %d" % widget.x()) # 窗口横坐标
    print("widget.y() = %d" % widget.y()) # 窗口纵 坐标
    print("widget.width() = %d" % widget.width()) #工作区宽度
    print("widget.height() = %d" % widget.height()) #工作区高度

    print("=====================================2===============================")
    print("widget.geometry().x() = %d" % widget.geometry().x())
    print("widget.geometry().y() = %d" % widget.geometry().y())
    print("widget.geometry().width() = %d" % widget.geometry().width())
    print("widget.geometry().height() = %d" % widget.geometry().height())

    print("=====================================3================================")
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x())
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y())
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width())
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height())

app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)


btn.move(24,52)

widget.resize(300, 240)
widget.move(250, 200)
widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec())


