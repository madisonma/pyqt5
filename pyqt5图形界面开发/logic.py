from PyQt5.QtWidgets import QMainWindow
import config, json, requests


class logic(QMainWindow):
    global username, userflag, reel, reelflag, terminal_id, cmd, reel, model, panelflag
    model = {}
    userflag = False
    reelflag = False
    panelflag = False

    def enter(self):
        global username, userflag, reel, reelflag, terminal_id, cmd, reel1, model, panelflag
        url = config.get("trace", "url1")
        text = self.label.text()
        input = self.lineEdit.text().strip()
        terminal_id = config.get("trace", "terminal_id")
        if len(input) == 0:
            return
        self.lineEdit.setFocus()
        if text == "请输入工号:":
            try:
                model = {}
                model["cmd"] = "0"
                model["username"] = input
                url = config.get("trace", "url1")
                data = json.dumps(model)
                R = requests.post(url, data, headers={'Content-Type': 'application/json'})
                res = json.loads(R.text)
                print(res)
                if res["data"]["result"]:
                    userflag = True
                    self.lineEdit.clear()
                    self.userNameValue.setText(res["data"]["message"])
                    self.userNameValue.setStyleSheet('''#userNameValue{color:blue;}''')
                    self.label.setText("请扫描REEL SN:")
                    username = input
                    self.logDisplay.setText(res["data"]["message"])
                    self.logDisplay.setStyleSheet('''QTextBrowser{color:blue;}''')
                else:
                    userflag = False
                    self.logDisplay.setText(res["data"]["message"])
                    self.logDisplay.setStyleSheet('''QTextBrowser{color:red;}''')
            except Exception as err:
                self.logDisplay.setText(str(err))
                self.logDisplay.setStyleSheet('''QTextBrowser{color:red;}''')
        elif text == "请扫描REEL SN:":
            try:
                model = {}
                model["username"] = username
                model["cmd"] = "0"
                model["reel_no"] = input
                url = config.get("trace", "url2")
                model["part_no"] = config.get("trace", "part_no").split(",")[0]

                data = json.dumps(model)
                R = requests.post(url, data, headers={'Content-Type': 'application/json'})
                res = json.loads(R.text)
                if res["data"]["result"]:
                    reelflag = True
                    self.lineEdit.clear()
                    self.lineEdit.setFocus()
                    self.label.setText("请扫描PANEL SN:")
                    reel = input
                    self.reelNumValue.setText(reel)
                    self.reelNumValue.setStyleSheet('''#reelNumValue{color:blue;}''')
                    #reelflag = True
                    self.reelRemainValue.setText(res["data"]["remain_count"])
                    self.reelRemainValue.setStyleSheet('''#reelRemainValue{color:blue;}''')
                    reel1 = res["data"]["remain_count"]
                    self.logDisplay.setText(res["data"]["message"])
                    self.logDisplay.setStyleSheet('''QTextBrowser{color:green;}''')
                else:
                    reelflag = False
                    print('failure')
                    self.logDisplay.setText(res["data"]["message"])
                    self.logDisplay.setStyleSheet('''QTextBrowser{color:red;}''')

            except Exception as err:
                self.logDisplay.setText(str(err))
                self.logDisplay.setStyleSheet('''QTextBrowser{color:red;}''')

        if text == "请扫描PANEL SN:":
            try:
                model = {}
                url = config.get("trace", "url2")
                model["cmd"] = "1"
                model["used_count"] = config.get("trace", "used_count")
                model["panel_sn"] = input
                model["terminal_id"] = int(terminal_id)
                model["reference"] = config.get("trace", "reference")
                model["reel_no"] = reel
                model["username"] = username

                data = json.dumps(model)
                R = requests.post(url, data, headers={'Content-Type': 'application/json'})
                res = json.loads(R.text)
                if res["data"]["result"]:
                    panelflag = True
                    self.lineEdit.clear()
                    self.lineEdit.setFocus()
                    if reel1 < 0:
                        self.label.setText("请扫描REEL SN:")
                    panelNumber = input
                    self.panelSnValue.setText(panelNumber)
                    self.panelSnValue.setStyleSheet('''#panelSnValue{color:blue;}''')
                    self.reelRemainValue.setText(res["data"]["remain_count"].split(",")[0])
                    self.reelRemainValue.setStyleSheet('''#reelRemainValue{color:blue;}''')
                    self.logDisplay.setText(res["data"]["message"])
                    self.logDisplay.setStyleSheet('''QTextBrowser{color:green;}''')
                else:
                    panelflag = False
                    self.logDisplay.setText(res["data"]["message"])
                    self.logDisplay.setStyleSheet('''QTextBrowser{color:red;}''')
            except Exception as err:
                self.logDisplay.setText(str(err))
                self.logDisplay.setStyleSheet('''QTextBrowser{color:red;}''')

        if userflag == False:
            self.label.setText("请输入工号:")
            self.lineEdit.clear()
            self.lineEdit.setFocus()
        elif reelflag == False:
            self.label.setText("请扫描REEL SN:")
            self.lineEdit.clear()
            self.lineEdit.setFocus()
        elif panelflag == False:
            self.label.setText("请扫描PANEL SN:")
            self.lineEdit.clear()
            self.lineEdit.setFocus()


    def btn_click(self):
        self.reelNumValue.setText("")
        self.reelRemainValue.setText("")
        self.label.setText("请扫描REEL SN:")