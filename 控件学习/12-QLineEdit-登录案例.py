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
        self.pwd_le.setEchoMode(QLineEdit.Passworda)
        self.log_btn = QPushButton(self)
        self.log_btn.setText("登录")


    def resizeEvent(self, evt):
        # 添加3个控件
        widget_w = 150
        widget_h = 40
        margin = 60

        self.account_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.log_btn.resize(widget_w, widget_h)


        x = (self.width() - widget_w) / 2

        self.account_le.move(x, self.height() / 5)
        self.pwd_le.move(x, self.account_le.y()+widget_h+margin)
        self.log_btn.move(x,self.pwd_le.y()+widget_h +margin)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

