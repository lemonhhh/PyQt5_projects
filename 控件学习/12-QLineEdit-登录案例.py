from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QLineEdit学习")
        self.resize(500,500)
        self.setMinimumSize(400,400)
        self.setup_ui()



    def setup_ui(self):
        self.account_le = QLineEdit(self)
        self.pwd_le = QLineEdit(self)

        #密文
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.log_btn = QPushButton(self)
        self.log_btn.setText("登录")

        self.account_le.setPlaceholderText("请输入账号")
        self.pwd_le.setPlaceholderText("请输入密码")
        #自动清空

        self.pwd_le.setClearButtonEnabled(True)

        def change():
            if(self.pwd_le.echoMode() == QLineEdit.Normal):
                self.pwd_le.setEchoMode(QLineEdit.Normal) #明文
                action.setIcon(QIcon("../source/hidden.png"))
            else:
                self.pwd_le.setEchoMode(QLineEdit.Password)  # 密文
                action.setIcon(QIcon("../source/open.png"))

        action = QAction(self.pwd_le)
        action.setIcon(QIcon("../source/view.png"))
        self.pwd_le.addAction(action,QLineEdit.TrailingPosition)

        action.triggered.connect(change)
        self.log_btn.clicked.connect(self.login_cao)


    def login_cao(self):
        account = self.account_le.text()
        passwd = self.pwd_le.text()



    def resizeEvent(self, evt):
        # 添加3个控件
        widget_w = 150
        widget_h = 40
        margin = 60

        self.account_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.log_btn.resize(widget_w, widget_h)


        x = (self.width() - widget_w) / 2

        # self.account_le.move(x, self.height() / 5)
        # self.pwd_le.move(x, self.account_le.y()+ widget_h + margin)
        # self.log_btn.move(x,self.pwd_le.y()+ widget_h + margin)

        self.account_le.move(50, 10)
        self.pwd_le.move(50, 60)
        self.log_btn.move(50, 110)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

