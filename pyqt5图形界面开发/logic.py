from PyQt5.QtWidgets import QMainWindow,QApplication
import config



class logic(QMainWindow):
    global model, model2, url, terminal_id

    def user_login(self):
        self.label.setText("输入工号:")

    def reel_input(self):
        self.label.setText("扫描REEL SN:")

    def panel_input(self):
        self.label.setText("扫描PANEL SN:")

    def enter(self):
        global terminal_id, reelNum, reelNumValue,url
        url = config.get('trace', 'url')
        terminal_id = config.get('trace', 'terminal_id')
