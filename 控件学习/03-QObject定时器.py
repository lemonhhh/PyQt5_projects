from PyQt5.Qt import *
import sys


class MyObject(QObject):

    def timerEvent(self, evt):
        print(evt, "1")


class MyLabel(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) #调用父类方法

        self.move(100, 100)
        self.setStyleSheet("font-size:22px;")
        self.setText("10")



    def setSec(self,sec):
        self.setText(str(sec))

    def startMyTimer(self,ms):
        self.timer_id = self.startTimer(ms)

    def timerEvent(self, *args, **kwargs):

        current_sec = int(self.text()) #1.获取当前标签的内容
        current_sec -= 1
        self.setText(str(current_sec))
        if current_sec == 0:
            self.killTimer(self.timer_id)

class MyWidget(QWidget):
    def timerEvent(self, *args,**kwargs):
        current_w = self.width()
        current_h = self.height()
        self.resize(current_w+10,current_h+10)


app = QApplication(sys.argv)


window = MyWidget()
window.setWindowTitle("定时器的使用")
window.resize(500, 500)
window.startTimer(100)
# label = MyLabel(window)
# label.setSec(5)
# label.startMyTimer(500)


window.show()
sys.exit(app.exec_())
