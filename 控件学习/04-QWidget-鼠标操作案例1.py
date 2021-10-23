from PyQt5.Qt import *
import sys

class MyLabel(QLabel):
    def enterEvent(self,*args,**kwargs):
        self.setText("欢迎光临～")

    def leaveEvent(self,*args,**kwargs):
        self.setText("谢谢惠顾～")

    def keyPressEvent(self,evt):
        print("xxx")
        if evt.key() == Qt.Key_Tab:
            print("用户点击了Tab~")
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            print("用户保存啦")


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("鼠标操作案例1")
window.resize(500,500)

label = MyLabel(window)
label.resize(200,200)
label.move(100,100)
label.setStyleSheet("background-color:cyan")
label.grabKeyboard()
window.show()
sys.exit(app.exec_())