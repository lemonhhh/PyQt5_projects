from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self,QMouseEvent):
        print("顶层窗口鼠标按下")
class MidWindow(QWidget):
    def mousePressEvent(self,QMouseEvent):
        print("中间控件被按下")
class Label(QLabel):
    def mousePressEvent(self,QMouseEvent):
        print("标签控件鼠标按下")




app = QApplication(sys.argv)


window = Window()

window.setWindowTitle("事件转发")
window.resize(500,500)

mid_window = MidWindow(window)
mid_window.resize(300,300)
mid_window.setAttribute(Qt.WA_StyledBackground,True)
mid_window.setStyleSheet("background-color:yellow;")

label = Label(mid_window)
label.setText("这是一个标签")
label.setStyleSheet("background-color:red;")
label.move(100,100)

btn = QPushButton(mid_window)
btn.setText("按钮嗷")
btn.move(50,50)

window.show()
sys.exit(app.exec_())