import sys
from PyQt5.Qt import *


class App(QApplication):
    def notify(self, receiver, evt):
        if(receiver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress):
            print(receiver, evt)

        return super().notify(receiver, evt)


class Btn(QPushButton):
    def event(self, evt):
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)

    def mousePressEvent(self,*args,**kwargs):
        print("鼠标被按下了")


app = App(sys.argv)

window = QWidget()
btn = QPushButton(window)
btn.setText("按钮")
btn.move(100, 100)


def cao():
    print("按钮被点击了")


btn.pressed.connect(cao)
window.show()
sys.exit(app.exec_())
