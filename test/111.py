from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import PYQT_VERSION_STR



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    print("PyQT5 Version is:{}".format(PYQT_VERSION_STR))


    sys.exit(app.exec_())